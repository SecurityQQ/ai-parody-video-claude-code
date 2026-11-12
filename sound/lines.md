# Lines

Text exactly as sent to the voice model (eleven_v3). Times are on the film's clock. Pace is words a minute over the
whole take, pauses included. Written by `tools/build_sound.py`.

| id | who (stock voice) | text as sent | take | start | end | wpm | note |
|---|---|---|---|---|---|---|---|
| D1 | DIRECTOR (Brian) | Cut to an interior. Camera follows a mysterious figure... before revealing our main character. | `D1.wav` | 0.30 | 6.12 | 144 |  |
| J1 | JENSEN (Eric) | Hello, and welcome to Nvidia! | `J1.wav` | 6.75 | 8.17 | 211 | cut 0.13 s into the last word: he gets as far as N- |
| D2 | DIRECTOR (Brian) | No, no, no, no, no. Not you. | `D2.wav` | 8.10 | 10.42 | 181 |  |
| J2 | JENSEN (Eric) | Is this... about the model? | `J2_t02.wav` | 10.85 | 12.52 | 179 | take 2: take 1 ran at 245 words a minute |
| D3 | DIRECTOR (Brian) | It's about the model. | `D3.wav` | 12.85 | 13.87 | 234 |  |
| J3 | JENSEN (Eric) | The language model? | `J3.wav` | 14.26 | 15.37 | 162 |  |
| D4 | DIRECTOR (Brian) | No. | `D4.wav` | 15.91 | 16.40 | 122 |  |
| D5 | DIRECTOR (Brian) | Jacket. | `D5.wav` | 17.31 | 18.25 | 64 |  |
| D6 | DIRECTOR (Brian) | That's your opener. | `D6.wav` | 19.92 | 20.95 | 175 |  |
| T1 | TIM (Will) | Good morning! And welcome to Nvidia. | `T1.wav` | 21.59 | 24.25 | 135 |  |
| T2 | TIM (Will) | This is the new R-T-X. It folds. | `T2.wav` | 24.63 | 28.05 | 123 |  |
| T3 | TIM (Will) | The power cable... is sold separately. | `T3_t02_tight.wav` | 28.54 | 30.92 | 151 | take 2: take 1 ran at 198 words a minute; its pause shortened to 0.36 s, cut inside the silence |
| J4 | JENSEN (Eric) | Can I... have my jacket back? | `J4_t02_tight.wav` | 31.38 | 33.75 | 152 | take 2: take 1 ran at 238; this one hesitates, 134; its pause shortened to 0.3 s, cut inside the silence |
| T4 | TIM (Will) | It's a subscription... now. | `T4_t02_tight.wav` | 34.09 | 35.94 | 129 | take 2: a 0.58 s pause before 'now'; take 1 ran at 194; its pause shortened to 0.36 s, cut inside the silence |

No voice here is a clone or an impression: three stock library voices, picked for pitch and pace (see plan.md).
Checked by machine: a transcript of the 14 first takes, joined, read word for word as the script (Whisper small.en).
Not checked by ear: nobody has listened yet. Accent, tone and whether a joke lands need a person.
