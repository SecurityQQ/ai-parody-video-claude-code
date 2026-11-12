#!/usr/bin/env python3
"""Lay the recorded voice lines on the film's clock and write the sound plan as data.

  python3 tools/build_sound.py          (needs ffmpeg and ffprobe)

Reads   sound/vo/<take>.wav (the take chosen per line, below)
Writes  sound/cues.json   every sound with its time, for `sound.py mix` and `sound.py check`
        sound/beats.json  every picture event with its time and its frame at 24 fps, and every line with start and end
        sound/lines.md    the lines as sent, the take used, measured length

The picture is cut to this file. Change a gap here, run it, then rebuild the mix, the blockout and the edit."""
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.join(ROOT, "sound"))
FPS = 24

# line id -> (who, stock voice, text as sent, take file, note)
LINES = {
    "D1": ("DIRECTOR", "Brian", "Cut to an interior. Camera follows a mysterious figure... before revealing our main character.", "D1.wav", ""),
    "J1": ("JENSEN", "Eric", "Hello, and welcome to Nvidia!", "J1.wav", "cut 0.13 s into the last word: he gets as far as N-"),
    "D2": ("DIRECTOR", "Brian", "No, no, no, no, no. Not you.", "D2.wav", ""),
    "J2": ("JENSEN", "Eric", "Is this... about the model?", "J2_t02.wav", "take 2: take 1 ran at 245 words a minute"),
    "D3": ("DIRECTOR", "Brian", "It's about the model.", "D3.wav", ""),
    "J3": ("JENSEN", "Eric", "The language model?", "J3.wav", ""),
    "D4": ("DIRECTOR", "Brian", "No.", "D4.wav", ""),
    "D5": ("DIRECTOR", "Brian", "Jacket.", "D5.wav", ""),
    "D6": ("DIRECTOR", "Brian", "That's your opener.", "D6.wav", ""),
    "T1": ("TIM", "Will", "Good morning! And welcome to Nvidia.", "T1.wav", ""),
    "T2": ("TIM", "Will", "This is the new R-T-X. It folds.", "T2.wav", ""),
    "T3": ("TIM", "Will", "The power cable... is sold separately.", "T3_t02.wav", "take 2: take 1 ran at 198 words a minute"),
    "J4": ("JENSEN", "Eric", "Can I... have my jacket back?", "J4_t02.wav", "take 2: take 1 ran at 238; this one hesitates, 134"),
    "T4": ("TIM", "Will", "It's a subscription... now.", "T4_t02.wav", "take 2: a 0.58 s pause before 'now'; take 1 ran at 194"),
}
SCRIPT_TEXT = {"J1": "Hello, and welcome to N-", "J2": "Is this about the model?", "T2": "This is the new RTX. It folds.",
               "T3": "The power cable is sold separately.", "J4": "Can I have my jacket back?", "T4": "It's a subscription now."}


def probe(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def lufs(f):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-af", "ebur128=framelog=quiet", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[0-9.]+) LUFS", out)[-1])


def pauses(f, db=-35, d=0.12):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-af", f"silencedetect=n={db}dB:d={d}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return [(float(a), float(b)) for a, b in zip(re.findall(r"silence_start: ([0-9.]+)", out), re.findall(r"silence_end: ([0-9.]+)", out))]




def tighten(take, keep):
    """Shorten the one written pause inside a take to `keep` seconds. The cut is made inside the silence, with 8 ms
    fades on both sides, so no word is touched. Writes <take>_tight.wav and returns its name."""
    ps = pauses("vo/" + take, db=-38, d=0.2)
    if not ps or ps[0][1] - ps[0][0] <= keep + 0.05:
        return take
    a, b = ps[0]
    out = take.replace(".wav", "_tight.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "vo/" + take, "-filter_complex",
                    f"[0]atrim=0:{a + keep / 2:.3f},afade=t=out:st={a + keep / 2 - 0.008:.3f}:d=0.008[x];"
                    f"[0]atrim={b - keep / 2:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.008[y];[x][y]concat=n=2:v=0:a=1",
                    "vo/" + out], check=True)
    return out


TIGHT = {"T3": 0.36, "J4": 0.30, "T4": 0.36}   # seconds of pause kept (takes came back with 0.54, 0.63 and 0.58)
for k, keep in TIGHT.items():
    v = LINES[k]
    LINES[k] = (v[0], v[1], v[2], tighten(v[3], keep), v[4] + f"; its pause shortened to {keep} s, cut inside the silence")
dur = {k: probe(f"vo/{v[3]}") for k, v in LINES.items()}
dur["J1"] = 1.42
g = lambda t: round(round(t * FPS) / FPS, 4)  # the nearest frame

S, E = {}, {}  # line starts, picture events


def say(k, t):
    S[k] = round(t, 3)
    return S[k] + dur[k]


end = say("D1", 0.30)
E["premise_type_on"] = 0.0
E["cut_s2"] = 3.0
E["cut_s3"] = g(end - 0.54)                  # the cut comes inside "our main character", as in the reference
E["strip_on_eyes"] = g(E["cut_s3"] + 0.96)
end = say("J1", E["strip_on_eyes"] + 0.21)
E["jensen_cut_off"] = round(end, 3)
E["lights_up"] = g(end - 0.09)
end = say("D2", E["lights_up"] + 0.017)
E["head_surprised"] = g(E["lights_up"] + 0.17)
end = say("J2", end + 0.43)
end = say("D3", end + 0.32)
E["head_smile"] = g(end + 0.28)
end = say("J3", E["head_smile"] + 0.09)
E["punch_no"] = g(end + 0.50)
end = say("D4", E["punch_no"] + 0.035)
E["sag"] = g(end + 0.56)
E["wide_jacket"] = g(E["sag"] + 0.33)
end = say("D5", E["wide_jacket"] + 0.017)
E["jacket_off"] = g(end + 0.16)
E["rack_focus"] = g(E["jacket_off"] + 0.25)
E["catch"] = g(E["jacket_off"] + 1.085)
end = say("D6", E["catch"] + 0.42)      # the music hits first, then he speaks
E["cut_s4"] = g(end + 0.19)
end = say("T1", E["cut_s4"] + 0.46)
E["wave"] = g(S["T1"] + 0.05)
E["cut_s5"] = g(end + 0.29)
end = say("T2", E["cut_s5"] + 0.09)
E["fold"] = g(end + 0.03)
E["tag_1"] = g(E["fold"] + 0.125)
end = say("T3", E["tag_1"] + 0.33)
p3 = pauses("vo/" + LINES["T3"][3])
E["tag_2"] = g(S["T3"] + (p3[0][1] if p3 else 0.9) + 0.25)   # on "sold"
E["jensen_in"] = g(end + 0.18)
end = say("J4", E["jensen_in"] + 0.30)
end = say("T4", end + 0.34)
E["cut_end"] = g(end + 0.41)
E["stamp"] = g(E["cut_end"] + 0.5417)     # the new name is stamped on the badge
E["end"] = g(E["cut_end"] + 4.5)
DUR = E["end"]

WHAT = {"premise_type_on": "type on screen at frame 0", "cut_s2": "cut to sneakers", "cut_s3": "cut to the dark corridor",
        "strip_on_eyes": "green strip crosses his eyes", "jensen_cut_off": "his line is cut on N-",
        "lights_up": "house lights, music stops, punch in", "head_surprised": "head swaps to the surprised photo",
        "head_smile": "head swaps to the smile", "punch_no": "punch in on the smile for 'No.'", "sag": "he sags",
        "wide_jacket": "back to the wide for 'Jacket.'", "jacket_off": "jacket leaves him",
        "rack_focus": "focus starts moving to the room behind", "catch": "the jacket is caught; bright music starts",
        "cut_s4": "cut to daylight", "wave": "he waves on 'Good morning'", "cut_s5": "punch in, card comes up",
        "fold": "the card folds", "tag_1": "IT FOLDS", "tag_2": "POWER CABLE: SOLD SEPARATELY",
        "jensen_in": "Jensen leans in from the left", "cut_end": "end card", "stamp": "NVIDIA is stamped on the name badge", "end": "last frame"}
events = [{"id": k, "time": v, "frame": round(v * FPS), "time_on_grid": g(v), "what": WHAT[k]}
          for k, v in sorted(E.items(), key=lambda kv: kv[1])]
lines = [{"id": k, "who": f"{LINES[k][0]} ({LINES[k][1]})", "text": SCRIPT_TEXT.get(k, LINES[k][2]).replace("...", "..."),
          "file": f"vo/{LINES[k][3]}", "start": S[k], "end": round(S[k] + dur[k], 3)} for k in S]
json.dump({"fps": FPS, "duration": DUR, "events": events, "lines": lines, "music_grid": "music/beats.json",
           "note": "'time' is where the sound puts the event; 'time_on_grid' is the nearest 24 fps frame and is what the "
                   "picture uses. The two differ by at most half a frame (21 ms)."}, open("beats.json", "w"), indent=1)

tracks = []
for k in S:
    t = {"id": k, "role": "voice", "file": f"vo/{LINES[k][3]}", "start": S[k], "gain_db": round(-17 - lufs(f"vo/{LINES[k][3]}"), 1)}
    if k == "J1":
        t.update({"length": 1.42, "fade_out": 0.03})
    tracks.append(t)
lu, ca, c4 = E["lights_up"], E["catch"], E["cut_s4"]
FULL = probe("music/keynote.mp3")
LAST_ACCENT_ENDS = 17.15         # seconds into keynote.mp3 where its last bar ends and only the tail is left (measured: the level falls from -17 to -29 dB there)
tempo = LAST_ACCENT_ENDS / (E["cut_end"] - ca)
if not 0.96 <= tempo <= 1.04:
    raise SystemExit(f"the music would need a tempo change of {tempo:.3f}; re-time or re-cut it instead")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "music/keynote.mp3", "-af", f"atempo={tempo:.5f}", "music/keynote_cut.wav"], check=True)
KEYNOTE, KEYNOTE_LEN = "music/keynote_cut.wav", min(DUR - ca, FULL / tempo)   # its last bar now ends on the end-card cut
tracks += [
    {"id": "tension", "role": "music", "file": "music/tension.mp3", "start": 0, "length": round(lu + 0.017, 3), "gain_db": 10, "fade_in": 0.04, "fade_out": 0.03},
    {"id": "keynote", "role": "music", "file": KEYNOTE, "start": ca, "gain_db": -9, "length": round(min(DUR - ca, KEYNOTE_LEN), 3)},
    {"id": "room", "role": "ambience", "file": "sfx/room_tone.mp3", "start": round(lu, 3), "length": round(c4 - lu, 3), "loop": True, "gain_db": 12, "fade_out": 0.3},
    {"id": "room_day", "role": "ambience", "file": "sfx/room_tone.mp3", "start": c4, "length": round(DUR - c4, 3), "loop": True, "gain_db": 9, "fade_in": 0.2},
    {"id": "steps_far", "role": "sfx", "file": "sfx/steps_far.mp3", "start": 0.04, "length": 2.9, "gain_db": 12, "fade_out": 0.1, "moment": "the small figure walks across the bridge"},
    {"id": "steps_close", "role": "sfx", "file": "sfx/steps_close.mp3", "start": 3.00, "length": round(E["cut_s3"] - 3.0, 3), "gain_db": 10, "fade_out": 0.1, "moment": "sneakers pass the camera"},
    {"id": "light_strip", "role": "sfx", "file": "sfx/light_strip.mp3", "start": round(E["strip_on_eyes"] - 1.30, 3), "at": round(E["strip_on_eyes"] - 1.02, 3), "trim_lead": False, "gain_db": 8,
     "moment": "the strip starts to glow as he walks into it; its click lands on his eyes"},
    {"id": "house_lights", "role": "sfx", "file": "sfx/house_lights.mp3", "start": round(lu + 0.017, 3), "gain_db": 10, "moment": "the lights come up on the first 'no'"},
    {"id": "zip_whoosh", "role": "sfx", "file": "sfx/zip_whoosh.mp3", "start": round(E["jacket_off"] - 0.108, 3), "gain_db": 2, "moment": "the zip opens, then the jacket leaves him and flies back"},
    {"id": "catch", "role": "sfx", "file": "sfx/catch.mp3", "start": ca, "gain_db": 16, "moment": "the figure behind the glass catches the jacket"},
    {"id": "fold_snap", "role": "sfx", "file": "sfx/fold_snap.mp3", "start": E["fold"], "gain_db": 5, "moment": "the card shuts like a flip phone"},
    {"id": "tag_pop_1", "role": "sfx", "file": "sfx/tag_pop.mp3", "start": E["tag_1"], "gain_db": 8, "moment": "the IT FOLDS tag pops up"},
    {"id": "tag_pop_2", "role": "sfx", "file": "sfx/tag_pop.mp3", "start": E["tag_2"], "gain_db": 8, "moment": "the SOLD SEPARATELY tag pops up"},
    {"id": "stamp", "role": "sfx", "file": "sfx/tag_pop.mp3", "start": E["stamp"], "gain_db": 9, "moment": "NVIDIA is stamped on the name badge"},
]
cuts = [E[k] for k in ("cut_s2", "cut_s3", "lights_up", "punch_no", "wide_jacket", "cut_s4", "cut_s5", "cut_end")]
json.dump({"duration": DUR, "fps": FPS, "platform": "x", "target": {"lufs": -14, "true_peak": -2.6},
           "duck": {"depth_db": 10, "ramp": 0.15}, "checks": {"voice_over_music_db": 10}, "cuts": cuts,
           "silences": [{"start": round(S["D4"] + dur["D4"], 2), "end": round(S["D5"], 2), "why": "the beat after 'No.': his smile hangs, room tone only"},
                        {"start": round(S["D2"] + dur["D2"], 2), "end": round(S["J2"], 2), "why": "he takes it in"},
                        {"start": round(S["T4"] + dur["T4"], 2), "end": E["cut_end"], "why": "the last line lands before the end card"}],
           "tracks": tracks}, open("cues.json", "w"), indent=1)

rows = "\n".join(f"| {k} | {LINES[k][0]} ({LINES[k][1]}) | {LINES[k][2]} | `{LINES[k][3]}` | {S[k]:.2f} | {S[k] + dur[k]:.2f} | "
                 f"{round(len(SCRIPT_TEXT.get(k, LINES[k][2]).replace('...', ' ').split()) / dur[k] * 60)} | {LINES[k][4]} |" for k in S)
open("lines.md", "w").write(
    "# Lines\n\nText exactly as sent to the voice model (eleven_v3). Times are on the film's clock. Pace is words a minute over the\n"
    "whole take, pauses included. Written by `tools/build_sound.py`.\n\n"
    "| id | who (stock voice) | text as sent | take | start | end | wpm | note |\n|---|---|---|---|---|---|---|---|\n" + rows +
    "\n\nNo voice here is a clone or an impression: three stock library voices, picked for pitch and pace (see plan.md).\n"
    "Checked by machine: a transcript of the 14 first takes, joined, read word for word as the script (Whisper small.en).\n"
    "Not checked by ear: nobody has listened yet. Accent, tone and whether a joke lands need a person.\n")
print(f"duration {DUR}s, {round(DUR * FPS)} frames; cuts {cuts}")
print("music:", KEYNOTE, "tempo x%.4f" % tempo, "for", round(KEYNOTE_LEN, 3), "s")
