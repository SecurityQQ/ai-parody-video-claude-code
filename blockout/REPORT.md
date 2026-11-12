# Blockout report

> In this public copy: paths under `renders/`, `review/judge_run*/` (with its `evidence/` and `eyes/`),
> `refs/apple-opener/`, `refs/style/` and `sound/audition/` point to files kept in the private working project.
> They are not in this repo.

The whole film blocked once in world time (metres, 24 fps), each shot a camera on it. Three.js through the
code-to-video-previz skill; the scene is data (`staging.json`, written by `make_staging.py` from `../sound/beats.json`).

FORMAT: 16:9, to the end-card cut, 24 fps. TOOL: Three.js, because rough placement is all the two video shots and
the coded shots need, and it renders about 870 frames in 15 to 23 s.

## Beats (seconds and metres)

| Shot | What | Camera, lens | Its job |
|---|---|---|---|
| s1 | A 1.70 m figure walks 4.2 m left to right along a bridge 6 m up, 24 m from the camera | locked, 24 mm, 7.2 m high | scale: a big building, a small man |
| s2 | The same walker passes at 1.4 m/s, 1.5 m from the lens | 14 cm above the floor, tracks right at 0.82 of his speed, 35 mm | the feet drift across frame while the camera follows |
| s3a | He walks 5.5 m up a 3.3 m wide corridor and stops 1.5 m from the lens | 1.55 m high, 15 cm push, 35 mm | the reveal |
| s3b | He stands; nothing moves but him | same axis, 50 mm, 20 cm push | the exchange, closer |
| s3c | Held | same axis, 85 mm, locked | "No." lands on his face |
| s3d | The jacket (a 0.6 m box) leaves him, rises to 2.4 m and lands 9.9 m back on a second, 1.83 m figure who walked in from the right; he edges 0.5 m left | same axis, 35 mm, locked | the handoff, in depth |
| s4 | The second figure walks 5.3 m toward the lens and stops on the right third | 1.5 m high, locked, 28 mm | the new man arrives small in a wide, bright place |
| s5 | He holds a 0.3 m card at 1.45 m; the first figure steps in 1.05 m to his left | same axis, 40 mm, 10 cm push | the pitch, and the old opener at his elbow |

One camera idea that was not asked for: s3c, the 85 mm close-up on the beat after "No."

## Checks

- Numbers (`check_staging.py`): "check ok" on v004. Round 1 had 9 errors: every one was a figure jumping between sets
  on the frame of a cut (keys moved to one millisecond before the cut), plus s2, where the head is out of frame on
  purpose (the shot is of feet, so no subject is audited there).
- Looked at, four sheets (`stills/contact_v001.jpg` to `v004.jpg`). Round 1: the feet shot sat on the edge of the
  bridge with no floor (it got its own set); the card floated through s4 (a key was missing); the catch happened at
  the edge of the doorway (moved in). Round 2: clean. Round 3 re-timed everything to the slower voice takes and
  brought the second figure in from the right; on its sheet a sliver of him showed at the edge of the 85 mm close-up,
  before the jacket had left. Round 4 keeps him behind the wall until the focus pull; on its sheet he first appears
  in the middle frame of s3d. That is one round past the guide's three: rounds 3 and 4 came from a re-time, not from
  a staging problem that would not move. `blockout_v005.mp4` and `contact_v005.jpg` are the same staging on the final
  clock (two cuts moved by two frames and five frames); that sheet was rendered and not looked at.
- Not done: a fresh agent's review of the blockout, and the 50% overlay on the reference.

## What it fed

- `renders/guide_sh020_grey.mp4`: the 5 s greyscale guide clip for sh020 (the one shot where a video model had to
  obey a camera path). The take came back with the same sideways track and no grey solids.
- The coded shots take their positions and timing from the same event list, not from the pixels: sh030's eye line,
  the 1/distance growth of the walk-up and the jacket's arc are the same numbers.
- Where the edit left the blockout: in s4 the edit ends with the figure at about 60% of frame height (the blockout
  has him near full height), and in s5 the old opener leans in lower than the blockout's standing figure.

Which parts need a person: play `renders/blockout_v005.mp4` once for the rhythm of the cuts. Stills cannot show it.
The stop for notes before rendering was passed without a person (the request was a standing goal).
