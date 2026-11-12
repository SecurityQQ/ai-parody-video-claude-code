# The paper-doll sheet

One image holds every body and both props, so they share one hand. Model: `gpt_image_2_6`, quality high, transparent
background, PNG, 16:9 (1088x608). Job job_b760ca755bbe, $0.06. No reference image was attached, and no person is named.

## Prompt (as sent)

A sheet of six separate paper-doll cut-out pieces in one row with clear gaps between them, nothing overlapping, in the
style of an 1870s hand-coloured lithograph caricature: fine black ink hatching, flat watercolour washes, slightly
off-register colour. Each body is a small, stubby full-length standing figure WITHOUT a head: it ends at the collar
with a short bare neck stub, because a photo head is glued on later. Left to right: (1) body in a black leather biker
jacket zipped halfway over a black T-shirt, black trousers, black sneakers, arms slightly out, palms open; (2) the same
body with no jacket: black T-shirt, black trousers, black sneakers, arms wrapped around itself as if cold; (3) body in
a navy quarter-zip sweater and light grey trousers with white sneakers, wearing on top a black leather biker jacket two
sizes too big, shoulders drooping, sleeves hanging past the hands; (4) the same oversized-jacket body with the right
arm raised to shoulder height, the long sleeve flopping over the hand, holding nothing; (5) an empty black leather
biker jacket with its arms spread wide, as if flying; (6) a long graphics card with three round fans and a metal
bracket, front view, no brand marks. No heads, no faces, no text, no logos, no labels, no numbers. Transparent
background.

## Checked against the passports, line by line (by eye, on the sheet)

| Line | On the sheet |
|---|---|
| Six pieces, nothing overlapping | Yes, six; split by `tools/split_sheet.py` |
| No heads | Yes: each body ends in a neck stub |
| Body 1: jacket half zipped, black T-shirt, palms open | Yes |
| Body 2: no jacket, arms wrapped | Yes: arms crossed over the chest, bare forearms |
| Body 3: navy quarter-zip, grey trousers, white sneakers, jacket too big, sleeves past the hands | Yes |
| Body 4: right arm raised | Raised on the viewer's right, sleeve over the hand |
| "Small, stubby" bodies | No: the bodies came out in normal proportions. Kept: the big head does the caricature |
| Jacket with arms spread | Yes |
| Card: three fans, bracket, no brand marks | Yes; no letters or numbers found by eye |
| No text anywhere | None found by eye; not run through OCR |

One sheet was made; nothing was re-rolled or edited.
