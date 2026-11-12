# References

> In this public copy: paths under `renders/`, `review/judge_run*/` (with its `evidence/` and `eyes/`),
> `refs/apple-opener/`, `refs/style/` and `sound/audition/` point to files kept in the private working project.
> They are not in this repo.

Route used: the person named the method ("take another funny video and adjust it"), so one clip is the primary
reference and everything else has one small job. Order of care for this piece (coded cut-outs over generated plates):
timing, framing, palette, type; light only where a plate has it.

Every reference below was opened. Numbers are copied from the source or measured here; "by eye" is marked.

## Primary: the video being adjusted

**R01 · film · Apple keynote opener, September 2026** (clip posted by @aaronp613, 2026-09-09)
- Link: https://x.com/aaronp613/status/2097785879041351803 · 11,562 likes · 1,297 bookmarks · 428,390 views (read 2026-11-11)
- File: `apple-opener/apple_opener_2026-09.mp4`, 20.78 s, 1920x1080. Frames in `apple-opener/frames/`.
- What I see: a narrator pitches the opening like a film director. A figure crosses an atrium bridge, sneakers walk past
  glass, a silhouette walks to the lens and a strip of light shows Tim Cook. He says "No, no, no, no, no. Not me. That's
  your guy." and thumbs over his shoulder. Focus racks to a man walking past the glass behind him. Cut to bright daylight:
  John Ternus walks up and says "Hello, and welcome to Apple Park."
- Lends: the whole structure. 4 shots, cuts at 3.14 s, 6.24 s, 16.82 s (ffmpeg scdet), a rack focus inside shot 3. Shot
  lengths 3.14 / 3.10 / 10.58 / 3.96 s. Measured palettes and light are in `DESIGN.md`, word times in `timing.md`.
- One job: structure and timing.
- Must not copy: Apple's footage, its building, its logo, its music, John Ternus. Our film re-stages the beats in a
  different place with different people and a reversed joke (the director says "Not you").
- Rights: look only. A video-analysis model watched it once to describe it; it was not given to any generating
  model and is not shown in the film. Two of its narrator's lines are quoted in the script.
- Provenance: HUMAN-PROVEN (a broadcast company film, named speakers).
- Found by: X search `"Tim Cook" (parody OR keynote OR "good morning" OR introducing) filter:videos min_faves:3000 since:2026-06-01`, rank 1 of 1.

## Framing (from R01, one card per shot)

| id | Shot | Lends (by eye from the frames) | Must not copy |
|---|---|---|---|
| R02 | S1 wide interior, 0-3.14 s | Symmetric one-point view down an atrium, a small figure crossing mid-frame at about 1/20 of frame height, locked camera | The building |
| R03 | S2 low tracking, 3.14-6.24 s | Camera at floor height, sneakers enter top-right, floor fills the lower 2/3, soft reflections | The shoe model |
| R04 | S3 reveal, 6.24-16.82 s | Centred silhouette against a brighter room behind glass; a horizontal strip of light across the eyes only; head grows from 1/3 to 2/3 of frame height; then focus moves to the background | His face |
| R05 | S4 daylight, 16.82-20.78 s | Wide curved glass corridor, sky and hills fill the left 60%, presenter small on the right third at about 1/4 of frame height, walks toward camera and stops | The campus |

## Style: big photo head on a small printed body

| id | Reference | What I see | Lends | Must not copy | Rights |
|---|---|---|---|---|---|
| R06 | Juan Pedro Chabalgoity, [Photo Collage: Man Wearing Blue Top Hat], ca. 1875, The Met 764771 | A real photographed head with a moustache pasted on a tiny lithographed body in a green check suit, on a plain orange card | Head about 2/5 of the figure (by eye), cut edge visible, flat plain ground | The sitter, the suit | Public domain (Met Open Access). File `style/met_chabalgoity_blue_top_hat.jpg` |
| R07 | Same maker, [Photo Collage: Man Reading Newspaper], ca. 1875, The Met 764769 | Photo head, small blue body holding a newspaper titled LA PATRIE, tiny wings | A hand-held prop sized to the body, not to the head | The sitter | Public domain. File `style/met_chabalgoity_newspaper.jpg` |
| R08 | Same maker, [Photo Collage: Man Sitting at Cocktail Table], ca. 1875, The Met 764776 | Photo head in a cap, seated printed body with a pipe and a glass | A second piece of furniture drawn in the same print style as the body | The sitter | Public domain. File `style/met_chabalgoity_cocktail_table.jpg` |

Found by: `search.py met "collage caricature" --public-domain`, ranks 2, 6, 7 of 205.
Provenance: HUMAN-PROVEN (holding museum, dated about 1875).

## Pop culture

| id | Reference | Lends | Must not copy |
|---|---|---|---|
| R09 | "Tim Apple": reply by @masonisonx under the Polymarket post, "From Tim Apple to Tim Nvidia", 33 likes | The end-card name badge | Nothing else from the thread |
| R10 | The black leather jacket: in both Jensen Huang photos opened on Commons (2023-11-09, 2024-05-13) he wears one | The jacket as the thing that is handed over | The exact jacket in the photos |

## Trends, last 7 days (X, read 2026-11-11; full numbers in `trends.md`)

| id | Post | Lends | Must not copy |
|---|---|---|---|
| R11 | @Polymarket, "Tim Cook is reportedly being floated as a potential replacement", 9,036 likes | Why now | Its "JUST IN" news framing |
| R12 | @viperr reply, "NVIDIA is about to make folding GPUs lmao", 955 likes | The tag joke: it folds | - |
| R13 | @Slobodan88 reply, "Imagine Tim Cook selling the power cable separately", 684 likes | The tag joke: cable sold separately | - |

## Could not reach, or did not test

- Refs (refs.video): `search.py refs` answered "blocked". Not retried.
- FrameThrower: needs an account. Not used.
- Film-Grab, ShotDeck, Shot Cafe, Eyecannndy, Pinterest: person-only. Links in `links.md`.
- YouTube: not searched; the primary reference came from X.
- Light was not judged by a model: the piece is coded, and each plate's light is checked against `DESIGN.md` numbers instead.
- The blind three-candidates-per-job board was built for style, framing and trend only. Light, people, location,
  texture, type, motion and music have no candidate sets: the primary reference fixes them.

Not in this public copy: the reference clip and its frames (`apple-opener/`), the three museum scans (`style/`) and
two trend cards (R14, R15). The links above lead to the sources.
