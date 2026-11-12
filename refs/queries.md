# Queries

One pack per job. L literal, N named, A adjacent, X excluded. Counts are results returned.

| Job | Slot | Source | Query | Results | Kept |
|---|---|---|---|---|---|
| never / obvious | L | X | his name plus the story's keywords, `filter:videos min_faves:2000 since:2026-11-06` | 8 | 0 kept, 4 watched; wrote never.md from it |
| trend | L | X | `Tim Cook Jensen Huang filter:videos min_faves:500 since:2026-11-05` | 0 | - |
| trend | N | X | `"Tim Cook" (Nvidia OR Jensen) since:2026-11-07 min_faves:300` | 9 | R11 |
| trend | A | X | `Jensen (replace OR replacement OR "new CEO" OR successor) Nvidia since:2026-11-09 min_faves:1000` | 2 | context only |
| trend | A | X | replies to post 2120663276556317109 | 36 | R09, R12, R13 |
| structure | N | X | `"Tim Cook" (parody OR keynote OR "good morning" OR introducing) filter:videos min_faves:3000 since:2026-06-01` | 1 | R01 |
| structure | A | X | `(Jensen OR Nvidia) (keynote OR jacket OR "new CEO" OR interim) filter:videos min_faves:1500 since:2026-11-08` | 0 | - |
| structure | L | varg how to | `funny parody video of two public figures, puppet caricature, remix a viral video` | 10 of 87 | read the titles; "remake a reference video" is the method used |
| style | L | Commons | `photomontage 1920s` | 26 | 0 (magazine pages, not figures) |
| style | L | Commons | `cutout animation` | 17,545 | 0 (too broad) |
| style | N | Commons | `photomontage caricature` | 5 | 0 |
| style | L | The Met | `photomontage` --public-domain | 72 | 0 |
| style | A | The Met | `collage caricature` --public-domain | 205 | R06, R07, R08 (ranks 2, 6, 7) |
| style | A | Library of Congress | `cut-out caricature` 1850-1940 | 37 | 0 |
| style | A | Library of Congress | `photomontage` 1880-1940 | 29 | 1 opened (Roosevelt crowd montage, 1908), not kept: a crowd, not a figure |
| motion | L | Commons | `filetype:video cutout animation` | 64 | 0 opened |
| motion | L | Commons | `filetype:video paper cutout animation` | 58 | 0 opened |
| motion | N | Refs | `{"query":"keynote opener walk reveal"}` | blocked | - |
| people (photos) | N | Commons | `Tim Cook portrait`, `filetype:bitmap Jensen Huang`, `Jen-Hsun Huang`, `黃仁勳` | 12 / 15 / 15 / 15 | 4 photos, see CREDITS.md |
| the story | L | web search | `Jensen Huang Tim Cook "model" incident Nvidia November 2026` | 9 links | read the summary only; used for the brief, not for any line |

Stopped style after the Met query: two queries in a row before it added nothing, and it returned the look.
Silent zeros: the two X queries with 0 results above.
