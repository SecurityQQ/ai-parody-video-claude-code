# Moodboard

> In this public copy: paths under `renders/`, `review/judge_run*/` (with its `evidence/` and `eyes/`),
> `refs/apple-opener/`, `refs/style/` and `sound/audition/` point to files kept in the private working project.
> They are not in this repo.

Every line is something a frame can be checked against. Numbers come from `refs/DESIGN.md` (measured on the reference).

**Look:** a product-launch film interior shot on a large-format digital camera, cool teal-grey, with 1875-style photo
cut-out people pasted on top.

**References:** R01 the Apple opener (structure, framing, palette), R06-R08 the Chabalgoity photo collages (the figures).
Both are in `refs/refs.md`. Neither is given to a generating model.

**Subject lock:** the two men are photo cut-outs: a real head, about 40% of the figure, on a small hand-coloured
lithograph body. Heads come from `inputs/photos`, cut out by code and never redrawn. Details per person in `cast/`.

**Light:**
- Dark corridor (sh030): the figure is a silhouette at 12% brightness until one horizontal strip of yellow-green light
  (#76B900), 30 px tall at 480p, crosses his eyes. The room behind is 2-3 stops brighter than the corridor walls.
- Daylight corridor (sh040-050): open daylight from camera-left, soft, no hard shadow. Highlights about 7,700 K.
- The switch from near black to high key is the handoff and happens on one cut.

**Palette:** shadows #090C0D · dark mid #2D3937 · cool mid #496164 · daylight sky #BED4DF · dry grass #9A9B6E ·
one accent #76B900 (the light strip, the PARODY tag, Jensen's captions). Nothing else is saturated except the red
#C8102E of a strike-through and the name badge. Grade in words: cool, low contrast in the dark, no orange.

**Framing (16:9, 854x480):**
| Shot | Size | Camera | Lens | Subject |
|---|---|---|---|---|
| sh010 | extreme wide | eye level, locked | 24 mm | figure 1/20 of frame height, crossing at mid-height |
| sh020 | close on feet | 14 cm above the floor, tracking | 35 mm | feet drift from the left third to the right third |
| sh030 | wide to medium close-up, then punches to 1.22x and 1.95x | 1.55 m, slow push | 35 / 50 / 85 mm | head centred, 48% of frame height at rest |
| sh040 | wide | 1.5 m, locked | 28 mm | figure on the right third, about 60% of frame height |
| sh050 | medium | same axis, 1.5x | 40 mm | head in the upper right third, card beside it |

**Texture:** the plates keep the image model's slight softness. Fine grain is baked into the dark plates and the
end-card plate: without it the judge measured banding in the first render. The cut-outs have a 2-3 px off-white cut edge. No drop shadows.

**Motion:** one camera idea per shot (locked, track, push, punch, focus pull, locked, punch). Figures move on twos
(12 poses a second); props on ones. Shot lengths 3.0 / 2.6 / 15.5 (broken by two punch-ins) / 3.4 / 11.8 / 4.5 s.
Motion reference: `refs/apple-opener/apple_opener_2026-09.mp4`.

**Type (set in code, never by a model):** Oswald. Premise 25 px / 700 / white and #76B900 on a #090C0D bar, top.
PARODY tag 16 px / 700 / #090C0D on #76B900, top right, every frame. Captions 25 px / 600 on a #090C0D box at 86%,
bottom centre, one colour per speaker (director white italic with a 16 px DIRECTOR tag, Jensen #B4F03A, Tim #CFE4EE).
Lower thirds 28 px name over a 19 px role. Paper tags 17 px / 700. Credit line 18 px. No type under 2.6% of the height.

**Sound:** voice: three stock voices, deep / light / soft (`sound/plan.md`). Music: a low pulse until "No", nothing but
room tone through the exchange, a bright marimba cue from the catch to the end. Room tone under everything else.

**Never:** a model-made or model-changed face; a frame without the PARODY tag; "cinematic", "8k", "stunning" in any
prompt; text drawn by a model; a logo; perfect symmetry in a plate; centred text fading in; a gradient background.

## Test stills (the hero shot, from the lines above alone)

| Still | Model | Palette: mean ΔE to the board (bar: the reference's own ΔE + 5) | Light | Verdict |
|---|---|---|---|---|
| `stills/corridor_dark_gpt_a.png` | gpt_image_2_6 | 4.8 (bar 11.2) pass | 94% of pixels below half grey, contrast 5.0 stops, strip at head height | **used for sh030** |
| `stills/corridor_dark_gpt_b.png` | gpt_image_2_6 | 4.8 (bar 11.2) pass | by eye: same layout, taller window | spare |
| `stills/corridor_dark_nb.png` | nano_banana_2_1 | 5.4 (bar 11.2) pass | by eye: darker, strip lower on the walls | not used |
| `stills/corridor_day_gpt.png` | gpt_image_2_6 | 14.8 (bar 17.4) pass | 0% below half grey, contrast 1.8 stops, sides even (ratio 1.06) | **used for sh040-050** |
| `stills/atrium_gpt.png` | gpt_image_2_6 | 7.2 (bar 11.9) pass | 91% below half grey | **first frame of sh010** |

Measured with `palette.py check --ref <reference frame>` and `frame_light.py`. Not checked: a second agent as critic
(skipped), and the daylight plate's light direction, which measures "even" where the board asks for camera-left: the
window wall is on the left, the brightness is not. It was kept because nothing in the shot depends on a shadow.
The stop for approval before any video was passed without a person (the request was a standing goal).
