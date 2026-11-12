# Review

> In this public copy: paths under `renders/`, `review/judge_run*/` (with its `evidence/` and `eyes/`),
> `refs/apple-opener/`, `refs/style/` and `sound/audition/` point to files kept in the private working project.
> They are not in this repo.

The maker did not judge its own film. Three separate agents, each with a fresh context and only the film, the brief,
the reference clip and the expected lines, measured it and then opened every flag. Their run folders are
`judge_run/` (film_v001, with `verdict.md`), `judge_run_v004/` and `judge_run_v007/`. The maker ran the measuring
tool alone on v003, v005 and v006: those folders hold numbers, not readings.

**Current film: `renders/film_v008.mp4`** (854x480, 24 fps, 980 frames, 40.83 s). It is film_v007, the render the
last judge read, with one line changed: the photo credit on the end card (see "After the rounds").
Sound was measured in every round and heard in none.

## Round 1: film_v001

State it gave: **needs a look**. After opening all 15 tool flags: 0 blockers, 2 major, 4 minor; 12 flags overturned.

| Severity | Finding (measured) | What was done | In |
|---|---|---|---|
| major | After the fold the card hung 15-20 px above the fist for 150 frames; the fold was a one-frame swap | The lower half now shuts over the upper half across 4 frames (its back shows), and the shut card drops 60 px into the hand | v005 |
| major | Banding: CAMBI 5.41 (max 6.52) in the dark corridor after the upload copy, 8.72 on the end card; limits 5 and 7.5 | Grain baked into the dark plates and the end-card plate | v003 |
| minor | Small type: tag capitals 2.55% of the height (floor 2.6%), credits capitals 2.08% | PARODY 16 px, lower-third roles 19 px, credits 18 px | v004, v005 |
| minor | Mouth states lasting one frame at f335, f641, f707 and 8 more in Tim's lines | Cause: a pose set exactly on a frame time could land one frame late. Sets now land 4 ms early | v003 |
| minor | Caption "...before revealing our main character." at 20.3 characters a second (limit 20) | Held 3 frames longer | v005 |
| minor | First shot: 30 attention peaks, top share 0.16 | A slow push toward the walker (scale 1 to 1.14). Still under the tool's 0.3 line; left, because the reference opens on the same kind of wide | v003 |

From its hints: the off-screen voice's captions now carry a DIRECTOR tag (for viewers with the sound off); every held
shot has a slow push; the name stamp has a sound; the audio no longer starts in digital silence. Not done: moving the
PARODY tag away from the top edge.

## Round 2: film_v004

State it gave: **no measured defect** at blocker or major level. 12 tool flags opened, 10 overturned, 4 minor rows.

| Severity | Finding (measured) | What was done | In |
|---|---|---|---|
| minor | The music stopped 263 ms after the end-card cut, on no visible event; no sound on the strike or the stamp | The music now plays 1.9% faster so its last bar ends on the cut and its tail rings under the badge; the stamp has a pop | v005, v007 |
| minor | End card: 26 words in 3.29 s; the credit line could not be read without pausing | Cut to 23 words (the tool counts 17, limit 18) and held 4.5 s instead of 3.3 | v006, v007 |
| minor | The cut to daylight landed 77 ms after the music's strongest accent | Moved two frames earlier; the caption before it now ends on the cut | v007 |
| minor | Jensen's glasses and side light change with each head swap (two photos) | Left. The two photos are how his expression changes, and no model may redraw his face | - |

Also from its notes: a hairline rectangle around the chin in the close-up (the jaw's slot). Since v007 the uncut head
is shown whenever he is silent, so the slot only exists while he speaks. The maker looked at a 4x crop of the close-up
in v007: no line.

## Round 3: film_v007

An independent final pass on thirteen named checks. State it gave: **no measured defect on the 13 checks**; six
minor notes; nothing major or blocker. Evidence crops are in `judge_run_v007/crops/`.

| # | Check | Measured | Result |
|---|---|---|---|
| 1 | PARODY label | On all 980 frames, same place; capitals 13 px = 2.70% of the height; contrast 7.7:1 | pass (0.5 px over the floor) |
| 2 | Frame 0 | Full atrium picture, mean brightness 49.3 of 255, no fade; reads "NVIDIA'S KEYNOTE OPENER, AFTER THE MODEL INCIDENT" | pass |
| 3 | Frozen stretch of 0.4 s or more | 0, the end card included; the stillest 0.42 s window still changes 5.2% of pixels | pass |
| 4 | Folded card and hand | Gap 0 px on three frames up to 6 s apart; the fold takes 4 frames | pass |
| 5 | Mouth states | 100 states over seven lines, shortest 2 frames, none of 1 | pass |
| 6 | Seam in the close-up | None at 4x or in an edge-amplified crop | pass |
| 7 | End card | The music's last bar ends 29-41 ms after the cut; the stamp's sound peaks 53 ms after it lands (limit 60); 23 words; final state held 3.79 s | pass |
| 8 | Cut to daylight | 12 ms before the nearest strong accent | pass |
| 9 | Smallest type | PARODY and DIRECTOR, capitals 13 px = 2.7%; credit capitals 14.5 px, their lower case 10.4 px (2.2%) | pass on capitals |
| 10 | Loudness | -14.2 LUFS, true peak -2.4 dBTP; audio and video both 40.833 s | pass |
| 11 | Captions | 18 of 18 match the script word for word; no caption within 84 px of a speaking mouth | pass |
| 12 | Would a frame pass for real footage with the label cropped off | No. Closest are the close-ups; the white cut edge, a 327 px head on a 200 px collar and a flat photo over a blurred set decide it | pass |
| 13 | Anyone else shown or named | No: the two men, and the three photo credits | pass |

Its six minor notes, none acted on (this is the third round, and each would need a new render that nobody independent
has read):

1. 28.00 s, frame 672: a cuff with fingers shows for one frame while the card folds.
2. 19.5-21.1 s: the small figure behind the glass stands about 24 px above the floor line of the ottoman beside him.
3. 36.4-40.8 s: after the stamp, the end card sits at -36 to -40 dBFS for 3.9 s (room tone only).
4. The end card holds 23 words; the tool's line is 18 at once (it reads 17, because it joins some).
5. 3.0-5.58 s: in the sneaker shot the PARODY tag is the only parody marker. Neither man can be identified in it.
6. In the close-up the lower edge of the lip shadow is flat for 35-39 px; it could not say whether that is the photo or the cut.

Numbers the maker took on v007 (`measured_v007.md`, every frame read) agree: 980 of 980 frames carry the tag, 0 black
frames, 0 frozen stretches, -14.2 LUFS, -2.4 dBTP, 71 of 71 script words heard by Whisper. `hyperframes check`:
0 errors, 3 lint warnings (two scene files over 300 lines; two images share a source), 18 of 18 contrast samples pass.

## After the rounds: film_v008

A fourth reader, checking the project before it was published, found the end card's credit wrong on two counts: it
put a public-domain photo under "CC BY" and did not say the photos were edited. The line changed from "Photos: Tessa
Bury · Presidential Office, Taiwan · The White House · CC BY" to "Photos (edited): Tessa Bury and Presidential Office,
Taiwan, CC BY · The White House". Nothing else in the edit changed. The maker's script read every frame of the new
render (`measured_v008.md`): 980 of 980 frames carry the tag, 0 black frames, 0 frozen stretches, -14.2 LUFS,
-2.4 dBTP, 71 of 71 script words heard. The maker looked at the end card: the line sits on one row. No independent
judge has read film_v008, and the end card now holds 24 words against the tool's line of 18.

## Tool flags that every round overturned (they will come back on any re-run)

| Flag | Why it is not a defect |
|---|---|
| expected_text | OCR joins "MY NAME IS" and the credit line, splits the name tag, and its 2-a-second sampling misses "The language model?" (on screen for 1.4 s) |
| spelling "NVIDIA'S" | Spelled right; the OCR suggests "india's" |
| outfit_change | The jacket is taken from him: the story |
| face_light_change | The lights come up on "No", and the two head photos are lit differently |
| object_scale, shot 1 | Two legs of one walker |
| soft_shot, shot 1 | The generated sneaker shot beside hard-edged cut-outs; the reference's own sneaker shot measures softer |
| level_jumps | The planned silence after "No." |
| label_drift, PARODY | The tag is fixed to the frame on purpose; the scene moves under it |

## What no round checked

- Hearing: voices, accents, whether the voices resemble the real men, whether "Nvidia" is said right (Whisper's
  confidence on it near 23.5 s was 0.32-0.53 in three rounds),
  whether each effect is the sound it claims to be.
- Whether it is funny.
- A real upload to X: the banding numbers are simulations at 2048 and 900 kbps. Legibility on a phone.
- Likeness and parody law, platform policy on parodies of real people, and whether the photo credits satisfy each licence.
- The guides' stops for a person's approval: all were passed without one, because the request was a standing goal.
