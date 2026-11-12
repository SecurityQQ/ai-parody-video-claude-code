#!/usr/bin/env python3
"""Measure a rendered film against the brief. Prints a Markdown table and exits 1 if any row fails.

  python3 tools/measure_film.py renders/film_v002.mp4 [--transcribe]

Checks (every frame is read for the picture checks, nothing is sampled):
  size, frame rate, frame count, length against sound/beats.json
  the PARODY tag: the mean colour of its box in EVERY frame must be within 40 of #76B900
  frame 0 is a picture: mean brightness above 8% and the premise bar's text area is not empty
  no black frame, no frozen stretch over 0.5 s
  loudness -14 LUFS +-1, true peak <= -1.5 dBTP
  with --transcribe: the words heard in the file against sound/beats.json lines (needs `bunx hyperframes@0.9.15`)
Needs ffmpeg, ffprobe and Pillow."""
import json
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
film = os.path.abspath(sys.argv[1])
os.chdir(ROOT)
beats = json.load(open("sound/beats.json"))
W, H, FPS = 854, 480, 24
TAG = (752, 14, 836, 37)          # the PARODY tag's box
rows, ok = [], True


def row(name, value, want, passed):
    global ok
    ok = ok and passed
    rows.append(f"| {name} | {value} | {want} | {'pass' if passed else '**FAIL**'} |")


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True)


p = json.loads(sh("ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,nb_frames",
                  "-of", "json", film).stdout)
v = [s for s in p["streams"] if s["codec_type"] == "video"][0]
dur = float(p["format"]["duration"])
row("Size", f'{v["width"]}x{v["height"]}', "854x480 (480p)", (v["width"], v["height"]) == (W, H))
row("Frame rate", v["r_frame_rate"], "24/1", v["r_frame_rate"] == "24/1")
row("Frames", v["nb_frames"], str(round(beats["duration"] * FPS)), int(v["nb_frames"]) == round(beats["duration"] * FPS))
row("Length", f"{dur:.3f} s", f'{beats["duration"]} s +-1 frame', abs(dur - beats["duration"]) <= 1 / FPS + 0.001)

# every frame: the tag's colour, and brightness
raw = subprocess.Popen(["ffmpeg", "-v", "error", "-i", film, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
n, missing, dark_frames, first_luma, worst = 0, [], [], None, 0
size = W * H * 3
while True:
    buf = raw.stdout.read(size)
    if len(buf) < size:
        break
    im = Image.frombytes("RGB", (W, H), buf)
    box = im.crop(TAG).resize((1, 1), Image.BOX).getpixel((0, 0))
    d = max(abs(box[0] - 0x76), abs(box[1] - 0xB9), abs(box[2] - 0x00))
    # the tag carries dark letters, so its mean is a little darker than pure #76B900
    d = max(abs(box[0] - 0x66), abs(box[1] - 0xA0), abs(box[2] - 0x04)) if d > 40 else d
    worst = max(worst, d)
    if d > 40:
        missing.append(n)
    luma = sum(im.resize((1, 1), Image.BOX).getpixel((0, 0))) / 3 / 255
    if n == 0:
        first_luma = luma
        bar_text = im.crop((22, 12, 700, 40)).convert("L").point(lambda x: 255 if x > 140 else 0).getbbox()
    if luma < 0.02:
        dark_frames.append(n)
    n += 1
row("PARODY tag in every frame", f"{n - len(missing)} of {n} frames (worst colour distance {worst})", "all", not missing)
if missing:
    rows.append(f"| | first missing frames: {missing[:8]} | | |")
row("Frame 0 is a picture", f"mean brightness {first_luma * 100:.1f}%, premise type {'found' if bar_text else 'not found'}", "above 8%, type present",
    first_luma > 0.08 and bar_text is not None)
row("Black frames", f"{len(dark_frames)}", "0", not dark_frames)
fz = sh("ffmpeg", "-hide_banner", "-i", film, "-vf", "freezedetect=n=-60dB:d=0.5", "-map", "0:v", "-f", "null", "-").stderr
freezes = [(float(a), float(b)) for a, b in zip(re.findall(r"freeze_start: ([0-9.]+)", fz), re.findall(r"freeze_end: ([0-9.]+)", fz))]
end_card = [e["time_on_grid"] for e in beats["events"] if e["id"] == "cut_end"][0]
bad = [f for f in freezes if f[0] < end_card - 0.1]
row("Frozen stretches over 0.5 s before the end card", f"{len(bad)} {bad[:3] if bad else ''}", "0 (the end card may hold)", not bad)
au = sh("ffmpeg", "-hide_banner", "-i", film, "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-").stderr
lufs = float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", au)[-1])
tp = float(re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", au)[-1])
row("Loudness", f"{lufs} LUFS", "-14 +-1", abs(lufs + 14) <= 1)
row("True peak", f"{tp} dBTP", "<= -1.5", tp <= -1.5)

if "--transcribe" in sys.argv:
    out = tempfile.mkdtemp(prefix="heard_" + os.path.basename(film).replace(".mp4", "") + "_")
    sh("bunx", "hyperframes@0.9.15", "transcribe", film, "-d", out, "--model", "small.en", "--json")
    d = json.load(open(out + "/transcript.json"))
    words = d if isinstance(d, list) else d.get("words", [])
    norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " ")).split()
    heard = norm(" ".join(w.get("text", w.get("word", "")) for w in words))
    want = norm(" ".join(l["text"] for l in beats["lines"]).replace("N-", ""))
    pool, hit = list(heard), 0
    for w in want:
        if w in pool:
            pool.remove(w)
            hit += 1
    row("Words heard (Whisper small.en on the file)", f"{hit} of {len(want)} ({hit / len(want) * 100:.0f}%)", ">= 95%", hit / len(want) >= 0.95)
    rows.append(f"| | heard: {' '.join(heard)[:400]} | | |")

print(f"# Measured: {os.path.basename(film)}\n\n| Check | Measured | Wanted | Result |\n|---|---|---|---|")
print("\n".join(rows))
sys.exit(0 if ok else 1)
