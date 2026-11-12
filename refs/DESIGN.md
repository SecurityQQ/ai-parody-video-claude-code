# Design values

Each value says where it came from: measured (a script on a file), record (a catalogue entry), by eye, or assumed.

## Palette, from the reference frames (`palette.py extract --k 6`)

| Shot | Frame | Dominant colours, share | Reading |
|---|---|---|---|
| S1 wide | `frames/02_t1_55.jpg` | #334645 57.6% · #212D2C 21.3% · #465A57 12.2% · #6A7E7D 4.8% · #9EB8BE 2.5% | measured: dark teal-grey, 84% of pixels below half grey |
| S2 sneakers | `frames/05_t4_70.jpg` | #496164 24.6% · #66858B 22.9% · #2C3A3B 19.9% · #88ACB1 17.0% · #101818 9.4% | measured: cool grey-blue floor, brighter right, contrast 5.2 stops |
| S3 reveal | `frames/08_t9_50.jpg` | #090C0D 33.8% · #1A2021 24.0% · #2D3937 20.7% · #415652 13.3% · #738E8E 5.5% · #75605E 2.8% | measured: near black, 88% below half grey, contrast 6.9 stops, skin is the only warm colour |
| S4 daylight | `frames/13_t18_80.jpg` | #969C9A 26.0% · #71756E 25.4% · #BED4DF 18.7% · #9A9B6E 17.8% · #5F6A4A 8.6% | measured: high key, 6% below half grey, bright side left (ratio 1.93) |

Board palette (taken from the rows above; one accent added):

| Role | Hex | Source |
|---|---|---|
| Shadows | #090C0D | measured, S3 |
| Dark mid | #2D3937 | measured, S3 |
| Cool mid | #496164 | measured, S2 |
| Daylight sky | #BED4DF | measured, S4 |
| Dry grass | #9A9B6E | measured, S4 |
| Accent: chip green | #76B900 | assumed: a bright yellow-green that the reference does not have; used for one light strip and the type accent only |

The switch from S3 (near black) to S4 (high key) is the handoff. Keep it: dark for Jensen, daylight for Tim.

## Light

| Shot | Value | Source |
|---|---|---|
| S3 | One horizontal strip across the eyes, everything else silhouette; room behind is 2-3 stops brighter than the figure | by eye from `frames/08`..`09`; contrast 6.9 stops measured |
| S4 | Open daylight from camera-left, soft, no hard shadow on the presenter | bright side left measured (ratio 1.93); softness by eye |
| Colour temperature | highlights 7,500-8,300 K in S1-S3, 7,700 K in S4 | measured by `frame_light.py` (an estimate from pixel colour, not a meter) |

## Figures (the cut-outs)

| Value | Number | Source |
|---|---|---|
| Head height as a share of the whole figure | about 40% | by eye from R06-R08 |
| Cut edge | off-white outline, 2-3 px at 480p, baked into each piece; no drop shadow | assumed |
| Jaw travel when speaking | up to 9% of head height, in four steps | assumed; driven by the measured loudness of each line, never set by ear |

## Type (set in code only)

| Use | Font, weight | Size at 854x480 | Hex | Position | Source |
|---|---|---|---|---|---|
| Premise line, first 3 s | Oswald 700, caps, tracking +3.5% | 25 px | #FFFFFF and #76B900 on a #090C0D bar | top, 50 px tall | assumed |
| PARODY tag, every frame | Oswald 700, caps, tracking +15% | 16 px (capitals 13 px, 2.7% of the height) | #090C0D on #76B900 | top-right corner | assumed |
| Captions | Oswald 600; a 16 px DIRECTOR tag before the off-screen voice's lines | 25 px | per speaker, on a #090C0D box at 86% | bottom centre | assumed; the 28 px floor at 1080 is 12.4 px here |
| Speaker colour | director #FFFFFF italic · Jensen #B4F03A · Tim #CFE4EE | - | - | - | palette above, lightened for the dark box |
| Lower thirds | Oswald 700 | 28 px name, 19 px role | #090C0D on #FBF9F2, role on #76B900 | left, y 316 | assumed; raised from 23 / 15 px after the judge measured the role under the 2.6% floor |
| Paper tags | Oswald 700 | 17 px | #090C0D on #FBF9F2, 2 px border | beside the prop | assumed |
| Credit line | Oswald 500 | 18 px | #DBE3E0 | end card, bottom | raised from Inter 13 px: capitals measured 2.08% of the height, under the floor |

Oswald is bundled with HyperFrames, so no font file is downloaded. An earlier draft of this table named Inter Tight;
it was dropped to avoid a download.
Never: Inter, Roboto or Arial as the display face, centred text fading in, a gradient background.

## Motion

| Value | Number | Source |
|---|---|---|
| Frame rate | 24 fps | brief |
| Camera moves | one per shot: locked, track, slow push, focus pull, locked, locked | R01, by eye |
| Cut-out motion | on twos (12 poses a second) for body bob and jaw; props on ones | assumed, for the paper look |
| Easing for type and props | cubic-bezier(0.16, 1, 0.3, 1); nothing linear except the jaw | editing guide |
| Type in / out | in 10 frames, out 8 frames | editing guide |
