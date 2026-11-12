# Timing

Source: `apple-opener/apple_opener_2026-09.mp4` (20.78 s). Cuts by `ffmpeg scdet=t=8`. Word starts by Whisper
small.en (`apple-opener/transcript/transcript.json`); Whisper runs late and long on this clip (it reports 22.36 s for
a 20.78 s file), so word times are marked "loose": trust them to about half a second. Our film runs at 24 fps.

## The reference

| Beat | Seconds | What moves first | Source |
|---|---|---|---|
| S1 wide, figure crosses | 0.00-3.14 | The figure, left to right. Camera locked | measured (scdet) |
| VO "Cut to an interior." | starts 0.04 | - | loose |
| S2 sneakers | 3.14-6.24 | Feet enter top right; camera tracks with them | measured |
| VO "Camera follows a mysterious figure / before revealing our main character." | 2.0-7.9 | The line runs across both cuts | loose |
| S3 silhouette walks in | 6.24-about 9.5 | The silhouette grows; the light strip lands on the eyes | measured cut, by eye inside |
| "No, no, no, no, no." | about 9.9-11.5 | Head shake starts with the first "no" | loose |
| "Not me. That's your guy." | about 11.5-14.0 | Thumb over the shoulder on "your guy" | loose |
| Rack focus to the background | about 13.8-14.8 | Foreground blurs, he leans out of frame left | by eye |
| VO "That's your opener." | about 14.7-16.5 | Background figure walks left to right behind the glass | loose |
| S4 daylight, walk to camera | 16.82-20.78 | Presenter walks 3 steps, stops, opens both hands | measured cut |
| "Hello, and welcome to Apple Park." | about 18.1-20.6 | Hands open on "welcome" | loose |

Shot lengths: 3.14 / 3.10 / 10.58 / 3.96 s. The long third shot carries the joke; the others are short and equal.
Reference loudness: -19.9 LUFS integrated, peak -3.6 dBFS (ebur128 on the X file).

## Ours (target, before sound is recorded; the locked numbers come from `sound/beats.json`)

| Beat | Target | Change from the reference |
|---|---|---|
| S1 wide | 3.0 s | Same |
| S2 sneakers | 3.0 s | Same |
| S3 reveal and the "Not you" exchange | about 10.5 s | Same length; the director talks back, so the lines alternate |
| S3b rack focus, jacket handed over | about 3 s | Was inside S3 in the reference; the jacket crossing the frame is new |
| S4 daylight greeting | about 4 s | Same |
| S5 tag: it folds, cable, subscription | about 8 s | New. The reference ends on the greeting |
| End card | 1.5 s | New |
