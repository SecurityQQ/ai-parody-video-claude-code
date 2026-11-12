#!/usr/bin/env python3
"""Build the HyperFrames edit in edit/ from the project's text and media.

  python3 tools/build_edit.py            (needs Pillow and ffmpeg)

Reads   sound/beats.json, sound/cues.json, sound/vo/*.wav, sound/mix.wav, cast/cutouts/*, look/stills/*,
        shots/sh010 and sh020 (the approved take named in each shot.md)
Writes  edit/assets/** (copies and baked variants: outline, dark, blurred) and edit/index.html + edit/compositions/*.html

Every number on screen is a function of timeline time. Jaw positions come from the measured loudness of each voice
line, held on twos (12 poses a second) for the paper look. Nothing here calls a model."""
import json
import math
import os
import shutil
import struct
import subprocess

from PIL import Image, ImageChops, ImageEnhance, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
W, H, FPS = 854, 480, 24
F = 1 / FPS
beats = json.load(open("sound/beats.json"))
EV = {e["id"]: e["time_on_grid"] for e in beats["events"]}
LINES = {l["id"]: l for l in beats["lines"]}
DUR = beats["duration"]
A = "edit/assets"
for d in ("cut", "plates", "audio", "video"):
    os.makedirs(f"{A}/{d}", exist_ok=True)
os.makedirs("edit/compositions", exist_ok=True)

# ---------------------------------------------------------------- assets


def outline(piece, stroke):
    a = piece.split()[3]
    grown = a.filter(ImageFilter.MaxFilter(stroke * 2 + 1)).filter(ImageFilter.GaussianBlur(0.7))
    out = Image.new("RGBA", piece.size, (0, 0, 0, 0))
    out.paste(Image.new("RGBA", piece.size, (250, 248, 242, 255)), (0, 0), grown)
    out.alpha_composite(piece)
    return out


def dark(piece, k=0.12):
    r, g, b, a = piece.split()
    return Image.merge("RGBA", (*ImageEnhance.Brightness(Image.merge("RGB", (r, g, b))).enhance(k).split(), a))


def blurred(piece, radius):
    pad = int(radius * 3)
    big = Image.new("RGBA", (piece.width + pad * 2, piece.height + pad * 2), (0, 0, 0, 0))
    big.paste(piece, (pad, pad))
    r, g, b, a = big.split()
    rgb = Image.merge("RGB", (r, g, b))
    # premultiply so the transparent surround does not darken the blurred edge
    pm = Image.composite(rgb, Image.new("RGB", big.size, (60, 60, 60)), a).filter(ImageFilter.GaussianBlur(radius))
    out = Image.merge("RGBA", (*pm.split(), a.filter(ImageFilter.GaussianBlur(radius))))
    return out.crop((pad, pad, pad + piece.width, pad + piece.height))


BODIES = {}
for key in ("jensen_jacket", "jensen_tee", "tim_jacket", "tim_jacket_arm_up"):
    im = outline(Image.open(f"cast/cutouts/body_{key}.png").convert("RGBA"), 6)
    im.save(f"{A}/cut/body_{key}.png")
    dark(im).save(f"{A}/cut/body_{key}_dark.png")
    blurred(im, 9).save(f"{A}/cut/body_{key}_blur.png")
    a = im.split()[3].point(lambda v: 255 if v > 128 else 0)
    raw = Image.open(f"cast/cutouts/body_{key}.png").split()[3].point(lambda v: 255 if v > 128 else 0)
    top = raw.getbbox()[1]
    band = raw.crop((0, top, raw.width, top + int(0.03 * raw.height)))
    bx = band.getbbox()
    meta = {"w": im.width, "h": im.height, "neck": [(bx[0] + bx[2]) / 2, top + 0.012 * raw.height]}
    if key.endswith("arm_up"):
        hand = raw.crop((int(0.80 * raw.width), 0, raw.width, int(0.30 * raw.height))).getbbox()
        meta["hand"] = [0.80 * raw.width + (hand[0] + hand[2]) / 2, hand[1] + 0.10 * raw.height]
    BODIES[key] = meta

HEADS = {}
for key in ("tim", "jensen_smile", "jensen_surprised"):
    HEADS[key] = json.load(open(f"cast/cutouts/{key}.json"))
    for part in ("head", "jaw", "head_full"):
        stem = f"head_{key}_full" if part == "head_full" else f"{part}_{key}"
        for suffix in ("", "_dark"):
            shutil.copy(f"cast/cutouts/{stem}{suffix}.png", f"{A}/cut/{stem}{suffix}.png")
        blurred(Image.open(f"cast/cutouts/{stem}.png").convert("RGBA"), 8).save(f"{A}/cut/{stem}_blur.png")

for key in ("jacket", "card"):
    im = outline(Image.open(f"cast/cutouts/prop_{key}.png").convert("RGBA"), 5)
    im.save(f"{A}/cut/prop_{key}.png")
card = Image.open(f"{A}/cut/prop_card.png")
card.crop((0, 0, card.width, card.height // 2)).save(f"{A}/cut/prop_card_top.png")
card.crop((0, card.height // 2, card.width, card.height)).save(f"{A}/cut/prop_card_bottom.png")
CARD = {"w": card.width, "h": card.height}
JACKET = dict(zip(("w", "h"), Image.open(f"{A}/cut/prop_jacket.png").size))

def grain(im, sigma):
    """fine noise, the same in all three channels, so smooth dark areas do not break into bands when re-encoded"""
    n = Image.effect_noise(im.size, sigma)
    return ImageChops.add(im, Image.merge("RGB", (n, n, n)), 1, -128)


corr = Image.open("look/stills/corridor_dark_gpt_a.png").convert("RGB")
corr.save(f"{A}/plates/corridor_sharp.jpg", quality=92)
soft = corr.filter(ImageFilter.GaussianBlur(2.6))
grain(soft, 5).save(f"{A}/plates/corridor_soft.jpg", quality=95)


def lights_on(im):
    return ImageEnhance.Contrast(ImageEnhance.Brightness(im).enhance(2.3)).enhance(0.92)


grain(lights_on(soft), 4).save(f"{A}/plates/corridor_lit_soft.jpg", quality=95)
lit_sharp = lights_on(corr)
grain(lit_sharp, 3).save(f"{A}/plates/corridor_lit_sharp.jpg", quality=95)
WALL_X = 618  # canvas x where the right corridor wall begins; a strip of it is laid back over the background figure
sx = corr.width / W
lit_sharp.crop((int(WALL_X * sx), 0, corr.width, corr.height)).save(f"{A}/plates/corridor_wall_r.jpg", quality=92)
day = Image.open("look/stills/corridor_day_gpt.png").convert("RGB")
day.save(f"{A}/plates/day.jpg", quality=92)
grain(ImageEnhance.Brightness(day.filter(ImageFilter.GaussianBlur(3))).enhance(0.34), 6).save(f"{A}/plates/day_dim.jpg", quality=95)
shutil.copy("sound/mix.wav", f"{A}/audio/mix.wav")

TAKES = {}
for shot in ("sh010", "sh020"):
    md = open(f"shots/{shot}/shot.md").read()
    take = [l.split("approved:")[1].strip() for l in md.splitlines() if l.startswith("approved:")][0]
    media_start = float([l.split("media_start:")[1].strip() for l in md.splitlines() if l.startswith("media_start:")][0])
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"shots/{shot}/takes/{take}", "-vf",
                    "scale=854:480:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,format=yuv420p", "-an", "-c:v", "libx264", "-crf", "14",
                    "-g", "24", f"{A}/video/{shot}.mp4"], check=True)
    TAKES[shot] = media_start

# ---------------------------------------------------------------- jaw: loudness per frame, held on twos


def envelope(line_id, length=None):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", "sound/" + LINES[line_id].get("file", f"vo/{line_id}.wav"), "-ac", "1", "-ar", "24000",
                          "-f", "s16le", "-"], capture_output=True).stdout
    x = struct.unpack("<%dh" % (len(raw) // 2), raw)
    start = LINES[line_id]["start"]
    end = start + (length or len(x) / 24000)
    rms = {}
    n = math.floor(start * FPS)
    while n * F < end:
        a = max(0, int((n * F - start) * 24000))
        b = min(len(x), int(((n + 1) * F - start) * 24000), int((end - start) * 24000))
        seg = x[a:b]
        rms[n] = math.sqrt(sum(v * v for v in seg) / len(seg)) if len(seg) > 40 else 0.0
        n += 1
    ref = sorted(rms.values())[int(0.9 * (len(rms) - 1))] or 1
    poses = []
    frames = sorted(rms)
    first = frames[0] - (frames[0] % 2)
    for n in range(first, frames[-1] + 2, 2):
        r = max(rms.get(n, 0), rms.get(n + 1, 0)) / ref
        o = min(1.0, max(0.0, (r - 0.14) / 0.62))
        poses.append((n, round(round(o * 3) / 3, 3)))  # four mouth shapes
    poses.append((frames[-1] + 2 - (frames[-1] % 2), 0.0))
    out = []
    for n, o in poses:
        if not out or out[-1][1] != o:
            out.append((n, o))
    return out


def jaw_calls(line_id, selectors, t0, length=None, face=None):
    """tl.set lines that move the jaw(s) for one voice line. selectors: [(css, max_drop_px)].
    face: css of the head piece that nods with the voice (a turn of up to 2 degrees and a 3 px lift, on twos)."""
    js = []
    poses = envelope(line_id, length)
    opened = [n for n, o in poses if o > 0]
    if opened:   # the uncut head hides from the first open pose to the last closing one
        for sel, _ in selectors:
            full = sel.replace("-jaw-", "-full-")
            js.append(f'ST("{full}", {{opacity: 0}}, {max(0, opened[0] * F - t0):.4f});')
            js.append(f'ST("{full}", {{opacity: 1}}, {max(0, poses[-1][0] * F - t0):.4f});')
    for i, (n, o) in enumerate(poses):
        at = max(0, n * F - t0)
        for sel, drop in selectors:
            js.append(f'ST("{sel}", {{y: {o * drop:.2f}}}, {at:.4f});')
        if face:
            turn = (1 if i % 2 else -1) * (0.5 + 1.5 * o) if o else 0
            js.append(f'ST("{face}", {{rotation: {turn:.2f}, y: {-3 * o:.2f}}}, {at:.4f});')
    return "\n".join(js)


def sway(sel, t0, t1, amount=0.7, period=2.6, phase=0.0):
    """a slow lean left and right, held on fours, so a standing figure is never a still image"""
    out = []
    n0, n1 = math.ceil(t0 * FPS / 4) * 4, int(t1 * FPS)
    for n in range(n0, n1, 4):
        out.append(f'ST("{sel}", {{rotation: {amount * math.sin(2 * math.pi * (n * F / period + phase)):.3f}}}, {n * F:.4f});')
    return "\n".join(out)


# ---------------------------------------------------------------- puppet markup

BODY_H, HEAD_H = 300.0, 200.0


def puppet(pid, cls, bodies, heads, suffix="", extra="", hide=False):
    """bodies/heads: [(key, shown_at_start)]. The puppet's origin is the top of the neck."""
    out = [f'<div id="{pid}" class="pup {cls}" data-layout-ignore{" style=\"opacity:0\"" if hide else ""}><div class="pup-in {cls}-in">']
    for key, on in bodies:
        m = BODIES[key]
        s = BODY_H / m["h"]
        out.append(f'<img id="{pid}-b-{key}" class="{cls}-b-{key}" src="assets/cut/body_{key}{suffix}.png" alt="" '
                   f'style="left:{-m["neck"][0] * s:.1f}px;top:{-m["neck"][1] * s:.1f}px;width:{m["w"] * s:.1f}px;'
                   f'height:{m["h"] * s:.1f}px;opacity:{1 if on else 0}">')
    out.append(extra)
    out.append(f'<div class="pup-head {cls}-head">')
    for key, on in heads:
        m = HEADS[key]
        s = HEAD_H / m["head_height"]
        st = (f'left:{-m["neck"][0] * s:.1f}px;top:{-m["neck"][1] * s + 7:.1f}px;width:{m["size"][0] * s:.1f}px;'
              f'height:{m["size"][1] * s:.1f}px')
        out.append(f'<div id="{pid}-h-{key}" class="pup-face {cls}-h-{key}" style="opacity:{1 if on else 0}">'
                   f'<img src="assets/cut/head_{key}{suffix}.png" alt="" style="{st}">'
                   f'<img class="{cls}-jaw-{key}" src="assets/cut/jaw_{key}{suffix}.png" alt="" style="{st}">'
                   f'<img class="{cls}-full-{key}" src="assets/cut/head_{key}_full{suffix}.png" alt="" style="{st}"></div>')
    out.append("</div></div></div>")
    return "\n".join(out)


def jaw_px(key):
    return HEADS[key]["jaw_max_drop"] * HEAD_H / HEADS[key]["head_height"]


PUP_CSS = """
.pup{position:absolute;left:0;top:0;width:0;height:0}
.pup-in,.pup-head,.pup-face{position:absolute;left:0;top:0;width:0;height:0}
.pup img{position:absolute;max-width:none;display:block}
.plate{position:absolute;left:0;top:0;width:854px;height:480px;object-fit:cover}
"""


def scene(cid, css, body, js):
    return f"""<template>
<style>
#root{{position:absolute;inset:0;overflow:hidden;background:#090C0D}}
{PUP_CSS}{css}
</style>
<div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
{body}
</div>
<script>
(function(){{
const tl = gsap.timeline({{ paused: true }});
// fromTo that leaves the element alone until its time comes
const FT = (sel, from, to, at) => tl.fromTo(sel, from, Object.assign({{ immediateRender: false }}, to), at);
// a set that lands 4 ms before its frame: rounding can then never push a pose one frame late
const ST = (sel, props, at) => tl.set(sel, props, Math.max(0, at - 0.004));
{js}
window.__timelines["{cid}"] = tl;
}})();
</script>
</template>
"""


def steps(sel, t0, t1, fn, every=2):
    """tl.set calls every `every` frames between two scene times; fn(u) -> props for u in 0..1"""
    n0, n1 = round(t0 * FPS), round(t1 * FPS)
    out = []
    for n in range(n0, n1 + 1, every):
        u = (n - n0) / max(1, n1 - n0)
        props = ", ".join(f"{k}: {v:.3f}" for k, v in fn(min(1.0, u)).items())
        if n == 0:
            out.append(f'gsap.set("{sel}", {{{props}}});')
        out.append(f'ST("{sel}", {{{props}}}, {n * F:.4f});')
    return "\n".join(out)


# ---------------------------------------------------------------- scene 3: the dark corridor
S3 = EV["cut_s3"]
S3_END = EV["cut_s4"]


def L(t):  # film time -> scene 3 time
    return t - S3


EYE_Y, CX = 196.0, 427.0
NECK = 104.0  # eyes to the top of the neck, at puppet scale 1 (measured on the head cut-outs)
BIG = 1.15
jen_bodies = [("jensen_jacket", True), ("jensen_tee", False)]
jen_heads = [("jensen_smile", True), ("jensen_surprised", False)]
s3_body = f"""
<div id="s3-cam" data-layout-ignore>
  <img id="s3-plate-dark" class="plate" src="assets/plates/corridor_soft.jpg" alt="">
  <img id="s3-plate-lit" class="plate" style="opacity:0" src="assets/plates/corridor_lit_soft.jpg" alt="">
  <img id="s3-plate-sharp" class="plate" style="opacity:0" src="assets/plates/corridor_lit_sharp.jpg" alt="">
  {puppet("s3-timbg-dark", "timbg", [("tim_jacket", True)], [("tim", True)], "_dark", hide=True)}
  {puppet("s3-timbg-lit", "timbg", [("tim_jacket", True)], [("tim", True)], hide=True)}
  <img id="s3-wall" src="assets/plates/corridor_wall_r.jpg" alt="" style="position:absolute;left:{WALL_X}px;top:0;width:{W - WALL_X}px;height:480px;opacity:0">
  {puppet("s3-jen-lit", "jen", jen_bodies, jen_heads)}
  <div id="s3-holed" style="position:absolute;inset:0;-webkit-mask-image:linear-gradient(to bottom,#000 0,#000 {EYE_Y - 30}px,transparent {EYE_Y - 17}px,transparent {EYE_Y + 15}px,#000 {EYE_Y + 28}px,#000 100%);mask-image:linear-gradient(to bottom,#000 0,#000 {EYE_Y - 30}px,transparent {EYE_Y - 17}px,transparent {EYE_Y + 15}px,#000 {EYE_Y + 28}px,#000 100%)">
    {puppet("s3-jen-holed", "jen", [("jensen_jacket", True)], [("jensen_smile", True)], "_dark")}
  </div>
  {puppet("s3-jen-dark", "jen", [("jensen_jacket", True)], [("jensen_smile", True)], "_dark")}
  {puppet("s3-jen-blur", "jen", [("jensen_tee", True)], [("jensen_surprised", True)], "_blur", hide=True)}
  <div id="s3-strip" style="position:absolute;left:0;top:{EYE_Y - 16}px;width:854px;height:30px;background:linear-gradient(to bottom,rgba(118,185,0,0),rgba(118,185,0,.30) 45%,rgba(118,185,0,.30) 55%,rgba(118,185,0,0));mix-blend-mode:screen;opacity:0"></div>
  <img id="s3-jacket" src="assets/cut/prop_jacket.png" alt="" style="position:absolute;left:{-JACKET['w'] * 0.25:.1f}px;top:{-JACKET['h'] * 0.25:.1f}px;width:{JACKET['w'] * 0.5:.1f}px;height:{JACKET['h'] * 0.5:.1f}px;opacity:0">
</div>
"""


def walk_in(u):  # perspective: 7.0 m away down to 1.5 m, eyes stay on the horizon
    d = 7.0 - 5.5 * u
    s = BIG * 1.5 / d
    return {"x": CX, "y": EYE_Y + NECK * s + (2.5 * s if round(u * 7) % 2 else 0), "scale": s}


walk_end = EV["strip_on_eyes"] + 0.2083
tb = 0.2  # the background figure's size
catch = EV["catch"]
jx0, jy0 = CX, EYE_Y + NECK * BIG + 80 * BIG       # the jacket starts on his chest
jx1, jy1 = 548.0, EYE_Y + NECK * tb + 26   # and ends on the background figure


def jacket_path(u):
    e = u * u * (3 - 2 * u)
    return {"x": jx0 + (jx1 - jx0) * e, "y": jy0 + (jy1 - jy0) * e - 150 * math.sin(math.pi * e),
            "scale": 0.82 + (0.17 - 0.82) * e, "rotation": -200 * e}


def tim_walk(u):
    return {"x": 668 - (668 - 548) * u, "y": EYE_Y + NECK * tb + (0.8 if round(u * 5) % 2 else 0), "scale": tb}


s3_js = f"""
gsap.set("#s3-cam", {{transformOrigin: "{CX}px {EYE_Y}px", scale: 1}});
gsap.set(".jen", {{x: {CX}, y: {EYE_Y + NECK * 0.246:.1f}, scale: 0.246}});
gsap.set(".timbg", {{x: 668, y: {EYE_Y + NECK * tb:.1f}, scale: {tb}}});
gsap.set("#s3-jacket", {{x: {jx0:.1f}, y: {jy0:.1f}, scale: 0.82}});
gsap.set(".jen-head", {{rotation: 0, y: 0}});
gsap.set(".jen-in, .timbg-in", {{scale: 1, y: 0, rotation: 0}});
gsap.set(".jen-h-jensen_smile, .jen-h-jensen_surprised", {{rotation: 0, y: 0}});
gsap.set(".jen-b-jensen_jacket", {{transformOrigin: "50% 0%", rotation: 0}});
// he walks up out of the dark, on twos
{steps(".jen", 0, L(walk_end), walk_in)}
FT("#s3-cam", {{scale: 1}}, {{scale: 1.035, duration: {L(EV["lights_up"]) - 0.02:.4f}, ease: "none"}}, 0.01);
{sway(".jen-in", L(walk_end), L(EV["rack_focus"]))}
// the strip of light finds his eyes
FT("#s3-strip", {{opacity: 0}}, {{opacity: 1, duration: 0.9, ease: "power2.in"}}, {L(EV["strip_on_eyes"]) - 0.95:.4f});
FT("#s3-jen-dark", {{opacity: 1}}, {{opacity: 0, duration: 0.125, ease: "none"}}, {L(EV["strip_on_eyes"]) - 0.04:.4f});
{jaw_calls("J1", [(".jen-jaw-jensen_smile", jaw_px("jensen_smile"))], S3, 1.42, face=".jen-h-jensen_smile")}
// "No": the lights come up and the camera punches in
ST("#s3-plate-lit", {{opacity: 1}}, {L(EV["lights_up"]):.4f});
ST("#s3-holed, #s3-strip", {{opacity: 0}}, {L(EV["lights_up"]):.4f});
ST("#s3-cam", {{scale: 1.22}}, {L(EV["lights_up"]):.4f});
FT("#s3-cam", {{scale: 1.22}}, {{scale: 1.3, duration: {EV["punch_no"] - EV["lights_up"] - 0.05:.4f}, ease: "none"}}, {L(EV["lights_up"]) + 0.01:.4f});
ST(".jen-h-jensen_smile", {{opacity: 0}}, {L(EV["head_surprised"]):.4f});
ST(".jen-h-jensen_surprised", {{opacity: 1}}, {L(EV["head_surprised"]):.4f});
FT(".jen-head", {{y: -9, rotation: -3}}, {{y: 0, rotation: 0, duration: 0.25, ease: "power2.out"}}, {L(EV["head_surprised"]):.4f});
{jaw_calls("J2", [(".jen-jaw-jensen_surprised", jaw_px("jensen_surprised"))], S3, face=".jen-h-jensen_surprised")}
FT(".jen-in", {{scale: 1}}, {{scale: 1.05, duration: 1.1, ease: "power1.out"}}, {L(LINES["J2"]["start"]):.4f});
// hope
ST(".jen-h-jensen_surprised", {{opacity: 0}}, {L(EV["head_smile"]):.4f});
ST(".jen-h-jensen_smile", {{opacity: 1}}, {L(EV["head_smile"]):.4f});
FT(".jen-head", {{rotation: 0}}, {{rotation: 5, duration: 0.2, ease: "back.out(2)"}}, {L(EV["head_smile"]):.4f});
{jaw_calls("J3", [(".jen-jaw-jensen_smile", jaw_px("jensen_smile"))], S3, face=".jen-h-jensen_smile")}
// "No.": hold on the smile, close
ST("#s3-cam", {{scale: 1.95}}, {L(EV["punch_no"]):.4f});
FT("#s3-cam", {{scale: 1.95}}, {{scale: 2.02, duration: {EV["wide_jacket"] - EV["punch_no"] - 0.05:.4f}, ease: "none"}}, {L(EV["punch_no"]) + 0.01:.4f});
ST(".jen-h-jensen_smile", {{opacity: 0}}, {L(EV["sag"]):.4f});
ST(".jen-h-jensen_surprised", {{opacity: 1}}, {L(EV["sag"]):.4f});
FT(".jen-head", {{rotation: 5, y: 0}}, {{rotation: -7, y: 9, duration: 0.25, ease: "power2.in"}}, {L(EV["sag"]):.4f});
// "Jacket.": wide again; it unzips, leaves him and flies to the man behind the glass
ST("#s3-cam", {{scale: 1}}, {L(EV["wide_jacket"]):.4f});
FT("#s3-cam", {{scale: 1}}, {{scale: 1.05, duration: {EV["cut_s4"] - EV["wide_jacket"] - 0.05:.4f}, ease: "none"}}, {L(EV["wide_jacket"]) + 0.01:.4f});
ST(".jen-in", {{scale: 1}}, {L(EV["wide_jacket"]):.4f});
ST(".jen-b-jensen_jacket", {{rotation: -2.5, transformOrigin: "50% 0%"}}, {L(EV["jacket_off"]) - 0.125:.4f});
ST(".jen-b-jensen_jacket", {{rotation: 2.5}}, {L(EV["jacket_off"]) - 0.0833:.4f});
ST(".jen-b-jensen_jacket", {{rotation: 0, opacity: 0}}, {L(EV["jacket_off"]):.4f});
ST(".jen-b-jensen_tee", {{opacity: 1}}, {L(EV["jacket_off"]):.4f});
ST("#s3-jacket", {{opacity: 1}}, {L(EV["jacket_off"]):.4f});
{steps("#s3-jacket", L(EV["jacket_off"]), L(catch), jacket_path, every=1)}
ST("#s3-jacket", {{opacity: 0}}, {L(catch):.4f});
// focus moves to the room behind
ST("#s3-timbg-dark, #s3-wall", {{opacity: 1}}, {L(EV["rack_focus"]):.4f});
{steps(".timbg", L(EV["rack_focus"]), L(catch), tim_walk)}
FT("#s3-plate-sharp", {{opacity: 0}}, {{opacity: 1, duration: 0.7, ease: "power1.inOut"}}, {L(EV["rack_focus"]):.4f});
FT("#s3-jen-blur", {{opacity: 0}}, {{opacity: 1, duration: 0.5, ease: "power1.in"}}, {L(EV["rack_focus"]):.4f});
FT("#s3-jen-lit", {{opacity: 1}}, {{opacity: 0, duration: 0.3, ease: "none"}}, {L(EV["rack_focus"]) + 0.4:.4f});
FT(".jen", {{x: {CX}}}, {{x: 232, duration: 0.9, ease: "power2.inOut"}}, {L(EV["rack_focus"]) + 0.25:.4f});
ST("#s3-timbg-dark", {{opacity: 0}}, {L(catch):.4f});
ST("#s3-timbg-lit", {{opacity: 1}}, {L(catch):.4f});
FT(".timbg-in", {{y: -7}}, {{y: 0, duration: 0.3, ease: "bounce.out"}}, {L(catch):.4f});
"""
open("edit/compositions/s3.html", "w").write(scene("s3", "#s3-cam{position:absolute;inset:0}", s3_body, s3_js))

# ---------------------------------------------------------------- scene 4: daylight
S4 = EV["cut_s4"]
S4_END = EV["cut_end"]


def M(t):
    return t - S4


TS = 0.62
TX, TY = 560.0, 245.0
arm = BODIES["tim_jacket_arm_up"]
sb = BODY_H / arm["h"]
hx, hy = (arm["hand"][0] - arm["neck"][0]) * sb, (arm["hand"][1] - arm["neck"][1]) * sb
ch = 150.0
cs = ch / CARD["h"]
card_html = f"""<div id="s4-card" class="tim-card" style="position:absolute;left:{hx + 14:.1f}px;top:{hy:.1f}px;width:0;height:0;opacity:0">
<img id="s4-card-top" src="assets/cut/prop_card_top.png" alt="" style="left:{-CARD['w'] * cs / 2:.1f}px;top:{-ch * 0.86:.1f}px;width:{CARD['w'] * cs:.1f}px;height:{ch / 2:.1f}px">
<img id="s4-card-bottom" src="assets/cut/prop_card_bottom.png" alt="" style="left:{-CARD['w'] * cs / 2:.1f}px;top:{-ch * 0.36:.1f}px;width:{CARD['w'] * cs:.1f}px;height:{ch / 2:.1f}px">
<div id="s4-card-back" style="position:absolute;left:{-CARD['w'] * cs / 2 + 2:.1f}px;top:{-ch * 0.86 + 2:.1f}px;width:{CARD['w'] * cs - 4:.1f}px;height:{ch / 2 - 2:.1f}px;box-sizing:border-box;background:#24282b;border:3px solid #f7f5ef;border-radius:5px;background-image:linear-gradient(#3a4044,#3a4044),linear-gradient(#3a4044,#3a4044),radial-gradient(circle,#8f979b 0 2px,transparent 2.5px),radial-gradient(circle,#8f979b 0 2px,transparent 2.5px);background-repeat:no-repeat;background-size:60% 3px,60% 3px,8px 8px,8px 8px;background-position:50% 30%,50% 46%,12% 82%,88% 82%"></div>
</div>"""
s4_body = f"""
<div id="s4-cam" data-layout-ignore>
  <img id="s4-plate" class="plate" src="assets/plates/day.jpg" alt="">
  {puppet("s4-jen", "jen4", [("jensen_tee", True)], [("jensen_smile", True)])}
  {puppet("s4-tim", "tim4", [("tim_jacket", True), ("tim_jacket_arm_up", False)], [("tim", True)], extra=card_html)}
</div>
<div id="s4-tag1" class="tag" data-layout-ignore><span>IT FOLDS</span></div>
<div id="s4-tag2" class="tag" data-layout-ignore><span>POWER CABLE:<br>SOLD SEPARATELY</span></div>
"""


def tim_in(u):
    e = 1 - (1 - u) ** 2
    s = 0.34 + (TS - 0.34) * e
    return {"x": 640 - (640 - TX) * e, "y": 232 + (TY - 232) * e + (2.2 if round(u * 6) % 2 else 0), "scale": s}


wave = "\n".join(
    f'ST(".tim4-b-tim_jacket", {{opacity: {0 if up else 1}}}, {M(t):.4f});\n'
    f'ST(".tim4-b-tim_jacket_arm_up", {{opacity: {1 if up else 0}, rotation: {(-4 if i % 4 == 0 else 3) if up else 0}, transformOrigin: "40% 15%"}}, {M(t):.4f});'
    for i, (t, up) in enumerate((EV["wave"] - 0.04 + k * 0.1667, k % 2 == 0) for k in range(6)))
s4_css = """
#s4-cam{position:absolute;inset:0}
.tag{position:absolute;left:0;top:0;background:#FBF9F2;color:#090C0D;word-spacing:.14em;font-family:'Oswald',sans-serif;font-weight:700;font-size:17px;
 line-height:1.12;letter-spacing:.03em;padding:6px 11px 7px;border:2px solid #090C0D;border-radius:3px;text-align:center;white-space:nowrap}
"""
s4_js = f"""
gsap.set("#s4-cam", {{transformOrigin: "540px 230px", scale: 1}});
gsap.set(".tim4", {{x: 640, y: 232, scale: 0.34}});
gsap.set(".jen4", {{x: -200, y: 305, scale: {TS}, rotation: 14}});
gsap.set("#s4-card", {{rotation: 10, y: 46, scale: 0.7}});
gsap.set("#s4-card-bottom", {{transformOrigin: "50% 0%", scaleY: 1}});
gsap.set("#s4-card-back", {{transformOrigin: "50% 100%", scaleY: 0}});
gsap.set("#s4-card-top", {{y: 0}});
gsap.set("#s4-tag1", {{x: 706, y: 62, rotation: 5, scale: 0}});
gsap.set("#s4-tag2", {{x: 654, y: 300, rotation: -4, scale: 0}});
gsap.set(".tim4-head, .jen4-head, .tim4-in, .jen4-in, .tim4-h-tim, .jen4-h-jensen_smile", {{rotation: 0, y: 0}});
gsap.set(".tim4-b-tim_jacket_arm_up", {{transformOrigin: "40% 15%", rotation: 0}});
FT("#s4-cam", {{scale: 1}}, {{scale: 1.04, duration: {M(EV["cut_s5"]) - 0.02:.4f}, ease: "none"}}, 0.01);
{sway(".tim4-in", M(EV["wave"]) + 0.3, M(S4_END), 0.6, 2.8)}
{sway(".jen4-in", M(EV["jensen_in"]) + 0.3, M(S4_END), 0.8, 2.2, 0.3)}
// he walks up and waves
{steps(".tim4", 0, M(EV["wave"]) + 0.25, tim_in)}
{wave}
FT(".tim4-head", {{rotation: 0}}, {{rotation: -5, duration: 0.2, ease: "power2.out"}}, {M(EV["wave"]):.4f});
tl.to(".tim4-head", {{rotation: 0, duration: 0.3, ease: "power2.inOut"}}, {M(EV["wave"]) + 0.9:.4f});
{jaw_calls("T1", [(".tim4-jaw-tim", jaw_px("tim"))], S4, face=".tim4-h-tim")}
// closer: the card comes up
ST("#s4-cam", {{scale: 1.5}}, {M(EV["cut_s5"]):.4f});
FT("#s4-cam", {{scale: 1.5}}, {{scale: 1.58, duration: {S4_END - EV["cut_s5"] - 0.05:.4f}, ease: "none"}}, {M(EV["cut_s5"]) + 0.01:.4f});
ST(".tim4-b-tim_jacket", {{opacity: 0}}, {M(EV["cut_s5"]):.4f});
ST(".tim4-b-tim_jacket_arm_up", {{opacity: 1, rotation: 0}}, {M(EV["cut_s5"]):.4f});
ST("#s4-card", {{opacity: 1}}, {M(EV["cut_s5"]):.4f});
FT("#s4-card", {{y: 46, scale: 0.7}}, {{y: 0, scale: 1, duration: 0.33, ease: "back.out(1.6)"}}, {M(EV["cut_s5"]):.4f});
{jaw_calls("T2", [(".tim4-jaw-tim", jaw_px("tim"))], S4, face=".tim4-h-tim")}
// it folds
FT("#s4-card-bottom", {{scaleY: 1}}, {{scaleY: 0.02, duration: 0.0833, ease: "power2.in"}}, {M(EV["fold"]) - 0.1667:.4f});
ST("#s4-card-bottom", {{opacity: 0}}, {M(EV["fold"]) - 0.0833:.4f});
FT("#s4-card-back", {{scaleY: 0}}, {{scaleY: 1, duration: 0.0833, ease: "power2.out"}}, {M(EV["fold"]) - 0.0833:.4f});
FT("#s4-card", {{y: 0}}, {{y: {0.40 * ch:.1f}, duration: 0.1667, ease: "power1.inOut"}}, {M(EV["fold"]) - 0.1667:.4f});
FT("#s4-card", {{scale: 1}}, {{scale: 1.12, duration: 0.0833, ease: "power2.out", yoyo: true, repeat: 1}}, {M(EV["fold"]):.4f});
FT("#s4-tag1", {{scale: 0}}, {{scale: 1, duration: 0.25, ease: "back.out(2.4)"}}, {M(EV["tag_1"]):.4f});
{jaw_calls("T3", [(".tim4-jaw-tim", jaw_px("tim"))], S4, face=".tim4-h-tim")}
FT("#s4-tag2", {{scale: 0}}, {{scale: 1, duration: 0.25, ease: "back.out(2.4)"}}, {M(EV["tag_2"]):.4f});
// the old opener leans in
FT(".jen4", {{x: -200, rotation: 14}}, {{x: 312, rotation: 8, duration: 0.3, ease: "power3.out"}}, {M(EV["jensen_in"]):.4f});
{jaw_calls("J4", [(".jen4-jaw-jensen_smile", jaw_px("jensen_smile"))], S4, face=".jen4-h-jensen_smile")}
{jaw_calls("T4", [(".tim4-jaw-tim", jaw_px("tim"))], S4, face=".tim4-h-tim")}
FT(".jen4-head", {{rotation: 0}}, {{rotation: 9, duration: 0.3, ease: "power2.in"}}, {M(LINES["T4"]["end"]) - 0.1:.4f});
"""
open("edit/compositions/s4.html", "w").write(scene("s4", s4_css, s4_body, s4_js))

# ---------------------------------------------------------------- end card
credits = "Photos: Tessa Bury · Presidential Office, Taiwan · The White House · CC BY"
end_css = """
#end-bg{position:absolute;left:0;top:0;width:854px;height:480px;object-fit:cover}
#end-badge{position:absolute;left:197px;top:88px;width:460px;height:206px;background:#FBF9F2;border-radius:16px;overflow:hidden;
 border:3px solid #FBF9F2;font-family:'Oswald',sans-serif;text-align:center}
#end-hello{background:#C8102E;color:#fff;height:74px;padding-top:6px}
#end-hello b{display:block;font-size:34px;letter-spacing:.14em;line-height:38px;font-weight:700}
#end-hello i{display:block;font-style:normal;font-size:16px;letter-spacing:.2em;word-spacing:.3em;line-height:20px;font-weight:600}
#end-name{color:#090C0D;font-size:48px;font-weight:700;line-height:122px;letter-spacing:.02em;word-spacing:.22em;white-space:nowrap}
#end-old{position:relative;display:inline-block;color:#8a8f8c}
#end-strike{position:absolute;left:-4px;right:-4px;top:58px;height:6px;background:#C8102E;border-radius:3px}
#end-new{display:inline-block;color:#4d7a00}
#end-parody{position:absolute;left:0;top:326px;width:854px;text-align:center;font-family:'Oswald',sans-serif;font-weight:700;
 font-size:27px;letter-spacing:.06em;word-spacing:.14em;color:#fff}
#end-parody span{color:#76B900}
#end-credits{position:absolute;left:40px;top:400px;width:774px;text-align:center;font-family:'Oswald',sans-serif;font-weight:500;letter-spacing:.03em;
 font-size:18px;line-height:24px;word-spacing:.2em;color:#dbe3e0}
"""
end_body = f"""
<img id="end-bg" src="assets/plates/day_dim.jpg" alt="" data-layout-allow-overflow>
<div id="end-badge"><div id="end-hello"><b>HELLO</b><i>MY NAME IS</i></div>
<div id="end-name">TIM <span id="end-old">APPLE<span id="end-strike"></span></span> <span id="end-new">NVIDIA</span></div></div>
<div id="end-parody"><span>PARODY.</span> NOBODY SAID THIS.</div>
<div id="end-credits" data-layout-allow-caption-zone>{credits}</div>
"""
end_js = """
gsap.set("#end-badge", {scale: 0.86, rotation: -5});
gsap.set("#end-strike", {scaleX: 0, transformOrigin: "0% 50%"});
gsap.set("#end-new", {scale: 0, rotation: -8});
gsap.set("#end-parody", {y: 14});
FT("#end-badge", {scale: 0.86, rotation: -5}, {scale: 1, rotation: -2, duration: 0.3, ease: "back.out(1.8)"}, 0);
FT("#end-strike", {scaleX: 0, transformOrigin: "0% 50%"}, {scaleX: 1, duration: 0.2, ease: "power2.out"}, 0.35);
FT("#end-new", {scale: 0, rotation: -8}, {scale: 1, rotation: -3, duration: 0.2, ease: "back.out(2.2)"}, STAMP_AT);
FT("#end-parody", {y: 14}, {y: 0, duration: 0.3, ease: "power3.out"}, 0.0);
gsap.set("#end-bg", {scale: 1, transformOrigin: "50% 50%"});
FT("#end-bg", {scale: 1}, {scale: 1.09, duration: END_LEN, ease: "none"}, 0.01);
FT("#end-badge", {scale: 1, rotation: -2}, {scale: 1.05, rotation: -1, duration: BADGE_LEN, ease: "none"}, 0.82);
"""
open("edit/compositions/end.html", "w").write(scene("end", end_css, end_body, end_js.replace("STAMP_AT", f"{EV['stamp'] - EV['cut_end'] - 0.02:.4f}").replace("END_LEN", f"{DUR - EV['cut_end'] - 0.03:.3f}").replace("BADGE_LEN", f"{DUR - EV['cut_end'] - 0.86:.3f}")))

# ---------------------------------------------------------------- labels: premise, the parody tag, lower thirds
lab_css = """
#root{background:transparent}
#lab-premise{position:absolute;left:0;top:0;width:854px;height:50px;background:#090C0D;color:#fff;word-spacing:.12em;font-family:'Oswald',sans-serif;
 font-weight:700;font-size:25px;line-height:50px;letter-spacing:.035em;padding-left:22px;white-space:nowrap}
#lab-premise span{color:#76B900}
#lab-parody{position:absolute;left:750px;top:13px;width:88px;height:25px;background:#76B900;color:#090C0D;font-family:'Oswald',sans-serif;
 font-weight:700;font-size:16px;line-height:25px;letter-spacing:.15em;text-align:center;border-radius:2px}
.lt{position:absolute;left:38px;top:316px;font-family:'Oswald',sans-serif;white-space:nowrap}
.lt b{display:block;background:#FBF9F2;color:#090C0D;font-weight:700;font-size:28px;line-height:37px;padding:0 12px;letter-spacing:.04em;word-spacing:.14em}
.lt i{display:inline-block;position:relative;font-style:normal;background:#76B900;color:#090C0D;font-weight:700;font-size:19px;line-height:26px;word-spacing:.14em;
 padding:0 11px;letter-spacing:.14em}
.lt u{position:absolute;left:6px;right:6px;top:11px;height:5px;background:#C8102E;text-decoration:none}
"""
jl0, jl1 = LINES["J1"]["start"] - 0.05, LINES["D2"]["end"] + 0.1
tl0, tl1 = EV["wave"] + 0.15, EV["cut_s5"]
lab_body = f"""
<div id="lab-premise" class="clip" data-start="0" data-duration="{EV['cut_s2']}" data-layout-allow-overlap>NVIDIA'S KEYNOTE OPENER, <span>AFTER THE MODEL INCIDENT</span></div>
<div id="lab-parody" class="clip" data-start="0" data-duration="{DUR}" data-layout-allow-overlap>PARODY</div>
<div id="lab-jensen" class="clip lt" data-start="{jl0:.4f}" data-duration="{jl1 - jl0:.4f}"><b>JENSEN HUANG</b><i>OPENER<u id="lab-jensen-strike"></u></i></div>
<div id="lab-tim" class="clip lt" data-start="{tl0:.4f}" data-duration="{tl1 - tl0:.4f}"><b>TIM COOK</b><i>NEW OPENER</i></div>
"""
lab_js = f"""
gsap.set("#lab-jensen, #lab-tim", {{x: -30, opacity: 0}});
gsap.set("#lab-jensen-strike", {{scaleX: 0, transformOrigin: "0% 50%"}});
FT("#lab-premise", {{y: 0}}, {{y: -52, duration: 0.2, ease: "power2.in"}}, {EV['cut_s2'] - 0.21:.4f});
FT("#lab-jensen", {{x: -30, opacity: 0}}, {{x: 0, opacity: 1, duration: 0.3, ease: "power3.out"}}, {jl0:.4f});
FT("#lab-jensen-strike", {{scaleX: 0, transformOrigin: "0% 50%"}}, {{scaleX: 1, duration: 0.2, ease: "power2.out"}}, {EV['head_surprised']:.4f});
FT("#lab-jensen", {{opacity: 1}}, {{opacity: 0, duration: 0.2, ease: "power1.in"}}, {jl1 - 0.22:.4f});
FT("#lab-tim", {{x: -30, opacity: 0}}, {{x: 0, opacity: 1, duration: 0.3, ease: "power3.out"}}, {tl0:.4f});
"""
open("edit/compositions/labels.html", "w").write(scene("labels", lab_css, lab_body, lab_js))

# ---------------------------------------------------------------- captions: one group per spoken phrase
CAPS = [
    ("D", "Cut to an interior.", LINES["D1"]["start"], LINES["D1"]["start"] + 1.32),
    ("D", "Camera follows a mysterious figure...", LINES["D1"]["start"] + 1.70, LINES["D1"]["start"] + 3.75),
    ("D", "...before revealing our main character.", LINES["D1"]["start"] + 4.11, LINES["D1"]["end"] + 0.30),
    ("J", "Hello, and welcome to N-", LINES["J1"]["start"], LINES["J1"]["end"]),
    ("D", "No, no, no, no, no.", LINES["J1"]["end"], LINES["D2"]["start"] + 1.52),
    ("D", "Not you.", LINES["D2"]["start"] + 1.64, LINES["D2"]["end"] + 0.18),
    ("J", "Is this about the model?", LINES["J2"]["start"], LINES["J2"]["end"] + 0.2),
    ("D", "It's about the model.", LINES["D3"]["start"], LINES["D3"]["end"] + 0.25),
    ("J", "The language model?", LINES["J3"]["start"], LINES["J3"]["end"] + 0.3),
    ("D", "No.", LINES["D4"]["start"], LINES["D4"]["end"] + 0.45),
    ("D", "Jacket.", LINES["D5"]["start"], LINES["D5"]["end"] + 0.3),
    ("D", "That's your opener.", LINES["D6"]["start"], min(LINES["D6"]["end"] + 0.2, EV["cut_s4"])),
    ("T", "Good morning! And welcome to Nvidia.", LINES["T1"]["start"], LINES["T1"]["end"] + 0.2),
    ("T", "This is the new RTX.", LINES["T2"]["start"] + 0.05, LINES["T2"]["start"] + 1.90),
    ("T", "It folds.", LINES["T2"]["start"] + 2.57, LINES["T2"]["end"] + 0.28),
    ("T", "The power cable is sold separately.", LINES["T3"]["start"], LINES["T3"]["end"] + 0.15),
    ("J", "Can I have my jacket back?", LINES["J4"]["start"], LINES["J4"]["end"] + 0.2),
    ("T", "It's a subscription now.", LINES["T4"]["start"], LINES["T4"]["end"] + 0.3),
]
cap_css = """
#root{background:transparent}
.cap{position:absolute;left:0;top:414px;width:854px;text-align:center;word-spacing:.1em;font-family:'Oswald',sans-serif;font-weight:600;font-size:25px;
 line-height:34px;letter-spacing:.02em}
.cap span{display:inline-block;background:rgba(9,12,13,.86);padding:1px 13px 3px;border-radius:3px}
.cap-D span{color:#FFFFFF;font-style:italic}
.cap-D b{font-style:normal;font-weight:700;font-size:16px;letter-spacing:.14em;color:#a9bab5;margin-right:11px;position:relative;top:-2px}.cap-J span{color:#B4F03A}.cap-T span{color:#CFE4EE}
"""
cap_body = "\n".join(
    f'<div id="cap-{i:02d}" class="clip cap cap-{who}" data-start="{a:.4f}" data-duration="{b - a:.4f}"><span>{"<b>DIRECTOR</b>" if who == "D" else ""}{txt}</span></div>'
    for i, (who, txt, a, b) in enumerate(CAPS))
open("edit/compositions/captions.html", "w").write(scene("captions", cap_css, cap_body, ""))
json.dump([{"who": w, "text": t, "start": round(a, 3), "end": round(b, 3)} for w, t, a, b in CAPS],
          open("edit/captions.json", "w"), indent=1)

# ---------------------------------------------------------------- the root
index = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: #090C0D; }}
      #root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; }}
      #sh010, #sh020 {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; object-fit: cover; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}">
      <video id="sh010" class="clip" src="assets/video/sh010.mp4" data-start="0" data-duration="{EV['cut_s2']}" data-media-start="{TAKES['sh010']}" data-track-index="0" muted playsinline style="z-index:1"></video>
      <video id="sh020" class="clip" src="assets/video/sh020.mp4" data-start="{EV['cut_s2']}" data-duration="{EV['cut_s3'] - EV['cut_s2']:.4f}" data-media-start="{TAKES['sh020']}" data-track-index="0" muted playsinline style="z-index:2"></video>
      <div id="s3" data-composition-id="s3" data-composition-src="compositions/s3.html" data-start="{S3}" data-duration="{S3_END - S3:.4f}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:3"></div>
      <div id="s4" data-composition-id="s4" data-composition-src="compositions/s4.html" data-start="{S4}" data-duration="{S4_END - S4:.4f}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:4"></div>
      <div id="end" data-composition-id="end" data-composition-src="compositions/end.html" data-start="{EV['cut_end']}" data-duration="{DUR - EV['cut_end']:.4f}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:5"></div>
      <div id="labels" data-composition-id="labels" data-composition-src="compositions/labels.html" data-start="0" data-duration="{DUR}" data-track-index="2" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:6"></div>
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{DUR}" data-track-index="3" data-track-kind="captions" data-width="{W}" data-height="{H}" style="z-index:7"></div>
      <audio id="mix" class="clip" src="assets/audio/mix.wav" data-start="0" data-duration="{DUR}" data-track-index="4" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const main = gsap.timeline({{ paused: true }});
      gsap.set("#sh010", {{ transformOrigin: "24% 30%", scale: 1 }});
      main.fromTo("#sh010", {{ scale: 1 }}, {{ scale: 1.14, duration: {EV['cut_s2'] - 0.02:.4f}, ease: "none", immediateRender: false }}, 0.01);
      window.__timelines["main"] = main;
    </script>
  </body>
</html>
"""
open("edit/index.html", "w").write(index)
print("built edit/: scenes s3, s4, end, labels, captions;", len(CAPS), "caption groups; hand anchor", round(hx, 1), round(hy, 1))
