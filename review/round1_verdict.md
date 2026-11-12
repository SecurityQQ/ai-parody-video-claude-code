# Verdict: film_v001.mp4

> In this public copy: paths under `renders/`, `review/judge_run*/` (with its `evidence/` and `eyes/`),
> `refs/apple-opener/`, `refs/style/` and `sound/audition/` point to files kept in the private working project.
> They are not in this repo.

self-judged: no. A fresh agent judged it and opened no prompts, scripts, notes or build files.
File judged: `renders/film_v001.mp4`, 5,075,959 bytes, sha1 `177a5a89aff773a2e94a05dd8e1ede13b7b7591d`, 854x480, 24 fps, 894 frames, 37.25 s.
Sound: measured, not heard.

## State

**Needs a look.** 0 blockers, 2 major flags, 4 minor.

## Counts

- Judge tool: 36 checks ran, 8 more are numbers with no pass or fail, 0 could not run.
- As measured: 21 clear, 15 flagged (4 blocker, 4 major, 7 minor).
- After opening every flag: 12 overturned, 3 kept (1 major, 2 minor).
- Added by eyes: 3 (1 major, 2 minor).
- Result: 33 of 36 clear, 0 blockers, 2 major, 4 minor.
- Brief checks (a) to (e): 5 run, 5 hold, with one open point in (e).

## Table

| Severity | Time | Where | Measured | Evidence | Fix | Cost |
|---|---|---|---|---|---|---|
| major | 27.50-33.75 s | The card and his raised fist, right of his head | After the fold the card (x 640-695, y 174-243) hangs 15-20 px above the fist (top at y about 260) for 150 frames. Before the fold it overlaps the sleeve. The fold is a one-frame swap, 53x115 px to 44x57 px, f659 to f660 | `eyes/card_not_in_hand_f600_f659_f660_f700.jpg` | Move the folded card about 20 px down and left so its lower edge overlaps the fist, or raise the fist layer 20 px | edit |
| major | 5.58-8.08 s and 33.75-37.25 s | Dark corridor walls; blurred end-card background | CAMBI corridor 5.23 in the file, 5.41 (max 6.52) after the 2048 kbps upload copy, 7.52 (max 8.88) at 832 kbps. End card 8.80 in the file, 8.72 (max 9.30) after. Limits 5 dark, 7.5 bright. Video stream is 884 kbps | `evidence/banding_2.jpg`, `evidence/banding_9.jpg`, `eyes/banding_8x_stretch.jpg` | Add grain over those two backgrounds and export the master at a higher bitrate, then run the same command again and make one private upload | edit |
| minor | whole film | PARODY badge, OPENER and NEW OPENER tags, credits line | Badge capitals 12.2 px = 2.55% of the height, floor 2.6%. Both tags 12.2 px. Credits capitals 10 px = 2.08%, lower case 7.5 px = 1.56%. Badge is 90x25 px = 0.55% of the frame | `eyes/text_crops_4x.jpg` | Scale the badge and the two tags by 1.1 or more, the credits line by 1.3 | edit |
| minor | 13.958 s, 26.708 s, 29.458 s | The jaw | Mouth wide open for one frame (42 ms) between smaller states at f335, f641, f707. 8 one-frame states in Tim's lines in shot 8 | `eyes/jaw_one_frame_f331-339.jpg` | Hold every mouth state at least 2 frames | edit |
| minor | 4.417-6.333 s | Caption "...before revealing our main character." | 39 characters on screen 46 frames = 20.3 characters per second, limit 20 | `eyes/caption_runs_frames.json` | Keep it up 2 more frames, to 6.417 s. The next caption starts at 6.750 s | edit |
| minor | 0.00-3.00 s | First shot | 30 attention peaks, top share 0.16. Flag is 8 or more peaks with under 0.3. The top peak sits on the walking figure | `evidence/attention_sheet.jpg` | None proposed: the reference's first shot is the same wide. To pass the number, dim the lit side windows | edit |

## What stays as it is

- PARODY badge: same place in 894 of 894 frames.
- Frame 0: full picture, title readable.
- 31 of 31 expected lines on screen, 0 misspelt.
- 19 captions match the voice script word for word.
- No caption or label on a speaking mouth.
- Sound on cuts: median +19.5 ms, 0 late.
- Loudness -14.1 LUFS, true peak -1.8 dBTP, 0 clipped runs, 0 dropouts.
- Twelve flags overturned, reasons in `overrides.json`.

## Not checked

Hearing the sound. A real upload to X. Likeness, parody law and photo licences. The later renders.
