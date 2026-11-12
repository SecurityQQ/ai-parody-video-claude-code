#!/usr/bin/env python3
"""Write sound/plan.md from sound/beats.json, sound/cues.json and sound/check.json, so the plan never drifts from the mix.
  python3 tools/write_sound_plan.py"""
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sound"))
b = json.load(open("beats.json"))
ev = {e["id"]: e["time_on_grid"] for e in b["events"]}
L = {l["id"]: l for l in b["lines"]}
c = json.load(open("cues.json"))
chk = json.load(open("check.json"))
music = [t for t in c["tracks"] if t["id"] == "keynote"][0]
t = lambda k: f"{ev[k]:.2f}"
rows = [
    ("0.00-" + t("cut_s2"), "Atrium, a small figure crosses", "DIRECTOR: Cut to an interior. Camera follows a mysterious figure...", "tension pulse, low", "footsteps, far", "-", "-"),
    (t("cut_s2") + "-" + t("cut_s3"), "Sneakers at floor height", "...before revealing our main character.", "tension", "footsteps, close", "-", "-"),
    (t("cut_s3") + "-" + t("lights_up"), "He walks up out of the dark; the strip finds his eyes", "JENSEN: Hello, and welcome to N-", "tension, cut dead on N-", "light swell, its click on the eyes", "-", "-"),
    (t("lights_up") + "-" + f'{L["D2"]["end"]:.2f}', "Lights up, punch in, surprised head", "DIRECTOR: No, no, no, no, no. Not you.", "none", "breaker clunk on the first no", "room tone", "-"),
    (f'{L["J2"]["start"]:.2f}-{L["J3"]["end"]:.2f}', "The exchange, one framing", "Is this about the model? / It's about the model. / The language model?", "none", "none", "room tone", "0.4 s before his first question"),
    (t("punch_no") + "-" + t("wide_jacket"), "Close on the smile; it stays; he sags", "DIRECTOR: No.", "none", "none", "room tone", "0.9 s after 'No.': the beat"),
    (t("wide_jacket") + "-" + t("catch"), "Wide; the jacket unzips, leaves, flies; focus moves back", "DIRECTOR: Jacket.", "none", "zip and whoosh", "room tone", "-"),
    (t("catch") + "-" + t("cut_s4"), "The man behind the glass catches it", "DIRECTOR: That's your opener.", "bright cue starts on the catch, 0.4 s before the line", "catch thump", "room tone", "-"),
    (t("cut_s4") + "-" + t("cut_s5"), "Daylight; he walks up and waves", "TIM: Good morning! And welcome to Nvidia.", "bright cue, ducked 10 dB under him", "none", "room tone", "-"),
    (t("cut_s5") + "-" + t("jensen_in"), "Closer; the card, the fold, two tags", "This is the new RTX. It folds. / The power cable is sold separately.", "bright cue, ducked", "snap on the fold, a pop per tag", "room tone", "0.8 s inside the first line, before 'It folds.'"),
    (t("jensen_in") + "-" + t("cut_end"), "Jensen leans in", "Can I have my jacket back? / It's a subscription now.", "bright cue, ducked; its last bar ends on the cut", "none", "room tone", "0.4 s after the last word"),
    (t("cut_end") + "-" + t("end"), "End card: the old name struck, the new one stamped", "-", "the tail of the last chord", "a pop on the stamp", "room tone", "-"),
]
tab = "\n".join("| " + " | ".join(r) + " |" for r in rows)
checks = "\n".join(f'| {x["check"]} | {x["value"]} | {x["target"]} | {"pass" if x["pass"] else "FAIL"} |' for x in chk["checks"])
open("plan.md", "w").write(f"""# Sound plan

The picture is cut to this. Times come from `beats.json` (written by `tools/build_sound.py`); the mix is `mix.wav`,
built from `cues.json` by the video-sound skill's `sound.py mix`. This file is written by `tools/write_sound_plan.py`.

Film length: {b["duration"]} s ({round(b["duration"] * 24)} frames at 24 fps).

## Beat by beat

| time | picture | voice | music | effects | ambience | silence |
|---|---|---|---|---|---|---|
{tab}

Never more than four layers at once: voice, one music cue, one effect, room tone.

## Voices (three stock voices, no clones)

| Role | Voice | Why | Measured on the audition line |
|---|---|---|---|
| Director, off screen | Brian | The lowest of the six auditioned: median pitch 91 Hz, so he sits under both men | 2.32 s for "No, no, no, no, no. Not you." |
| Jensen | Eric | The lightest: 143 Hz, 52 Hz above the director, so the two never blur in the exchange | 1.44 s for "Is this about the model?" |
| Tim | Will | The slowest read of the greeting: 132 words a minute with two pauses, 114 Hz | 2.72 s for "Good morning! And welcome to Nvidia." |

Auditioned and not used: Bill (director, 131 Hz), Chris (Jensen, 103 Hz: too close to the director), George (Tim: 160 Hz,
and British). Files in `audition/`. The pick was made on pitch, pace and the library's description. **Nobody has
listened.** The first thing a person should do with this film is play it and judge the three voices.

Four lines were re-recorded after `voice_check.py` measured them at 194-245 words a minute; see `lines.md`. Three of the
new takes had their one written pause shortened in the silence (never inside a word).

## Music and effects

| Cue | File | Made with | Used |
|---|---|---|---|
| Tension pulse | `music/tension.mp3` | eleven_music_v2_5, 12 s asked, instrumental | 0.00-{t("lights_up")}, then cut dead |
| Bright cue | `{music["file"]}` | eleven_music_v2_5, 20 s asked, instrumental, 112 BPM measured; played {(17.15 / (ev["cut_end"] - ev["catch"]) - 1) * 100:.1f}% faster | from the catch at {t("catch")}; its last bar ends on the end-card cut at {t("cut_end")} and the tail rings under the badge |
| 9 effects and a room tone | `sfx/*.mp3` | eleven_sound_effects_v3 | each has its visible moment in `cues.json`; the paper pop is used three times |

No melody, voice or artist was named in any prompt.

## Check (`sound.py check`, on the mix)

| Check | Measured | Target | Result |
|---|---|---|---|
{checks}

The mix is mastered to -14 LUFS with a true peak near -3 dBTP, lower than the usual -1.5: the AAC encode in the
second render lifted peaks by 0.7 dB and put that file 0.2 dB over the limit.
Measured, not heard: every row above is a number from a script.
""")
print("sound/plan.md written for", b["duration"], "s")
