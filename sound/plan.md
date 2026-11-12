# Sound plan

The picture is cut to this. Times come from `beats.json` (written by `tools/build_sound.py`); the mix is `mix.wav`,
built from `cues.json` by the video-sound skill's `sound.py mix`. This file is written by `tools/write_sound_plan.py`.

Film length: 40.8333 s (980 frames at 24 fps).

## Beat by beat

| time | picture | voice | music | effects | ambience | silence |
|---|---|---|---|---|---|---|
| 0.00-3.00 | Atrium, a small figure crosses | DIRECTOR: Cut to an interior. Camera follows a mysterious figure... | tension pulse, low | footsteps, far | - | - |
| 3.00-5.58 | Sneakers at floor height | ...before revealing our main character. | tension | footsteps, close | - | - |
| 5.58-8.08 | He walks up out of the dark; the strip finds his eyes | JENSEN: Hello, and welcome to N- | tension, cut dead on N- | light swell, its click on the eyes | - | - |
| 8.08-10.42 | Lights up, punch in, surprised head | DIRECTOR: No, no, no, no, no. Not you. | none | breaker clunk on the first no | room tone | - |
| 10.85-15.37 | The exchange, one framing | Is this about the model? / It's about the model. / The language model? | none | none | room tone | 0.4 s before his first question |
| 15.88-17.29 | Close on the smile; it stays; he sags | DIRECTOR: No. | none | none | room tone | 0.9 s after 'No.': the beat |
| 17.29-19.50 | Wide; the jacket unzips, leaves, flies; focus moves back | DIRECTOR: Jacket. | none | zip and whoosh | room tone | - |
| 19.50-21.12 | The man behind the glass catches it | DIRECTOR: That's your opener. | bright cue starts on the catch, 0.4 s before the line | catch thump | room tone | - |
| 21.12-24.54 | Daylight; he walks up and waves | TIM: Good morning! And welcome to Nvidia. | bright cue, ducked 10 dB under him | none | room tone | - |
| 24.54-31.08 | Closer; the card, the fold, two tags | This is the new RTX. It folds. / The power cable is sold separately. | bright cue, ducked | snap on the fold, a pop per tag | room tone | 0.8 s inside the first line, before 'It folds.' |
| 31.08-36.33 | Jensen leans in | Can I have my jacket back? / It's a subscription now. | bright cue, ducked; its last bar ends on the cut | none | room tone | 0.4 s after the last word |
| 36.33-40.83 | End card: the old name struck, the new one stamped | - | the tail of the last chord | a pop on the stamp | room tone | - |

Never more than four layers at once: voice, one music cue, one effect, room tone.

## Voices (three stock voices, no clones)

| Role | Voice | Why | Measured on the audition line |
|---|---|---|---|
| Director, off screen | Brian | The lowest of the six auditioned: median pitch 91 Hz, so he sits under both men | 2.32 s for "No, no, no, no, no. Not you." |
| Jensen | Eric | The lightest: 143 Hz, 52 Hz above the director, so the two never blur in the exchange | 1.44 s for "Is this about the model?" |
| Tim | Will | The slowest read of the greeting: 132 words a minute with two pauses, 114 Hz | 2.72 s for "Good morning! And welcome to Nvidia." |

Auditioned and not used: Bill (director, 131 Hz), Chris (Jensen, 103 Hz: too close to the director), George (Tim: 160 Hz,
and British). Files in `audition/`. The pick was made on pitch, pace and the library's description. **Nobody has
listened.** The first thing a person should do with this film is play it and judge the three voices.

Four lines were re-recorded after `voice_check.py` measured them at 194-245 words a minute; see `lines.md`. Three of the
new takes had their one written pause shortened in the silence (never inside a word).

## Music and effects

| Cue | File | Made with | Used |
|---|---|---|---|
| Tension pulse | `music/tension.mp3` | eleven_music_v2_5, 12 s asked, instrumental | 0.00-8.08, then cut dead |
| Bright cue | `music/keynote_cut.wav` | eleven_music_v2_5, 20 s asked, instrumental, 112 BPM measured; played 1.9% faster | from the catch at 19.50; its last bar ends on the end-card cut at 36.33 and the tail rings under the badge |
| 9 effects and a room tone | `sfx/*.mp3` | eleven_sound_effects_v3 | each has its visible moment in `cues.json`; the paper pop is used three times |

No melody, voice or artist was named in any prompt.

## Check (`sound.py check`, on the mix)

| Check | Measured | Target | Result |
|---|---|---|---|
| loudness | -14.2 LUFS | -14 ±1 LUFS (x) | pass |
| true peak | -3.1 dBTP | <= -2.6 dBTP | pass |
| length | 40.837 s | 40.8333 s ±1 frame | pass |
| voice above music | 13.2 dB in 300 Hz-4 kHz (worst line 21.59-35.94s) | >= 10.0 dB during every line (WCAG AAA asks 20) | pass |
| sfx on their moments | 10/10 within 1 frame | <= 42 ms | pass |
| no dead air | 0 unplanned gaps under -60 dBFS | 0 (room tone under everything) | pass |
| mono safe | mono is 3.1 dB quieter | <= 6.5 dB | pass |

The mix is mastered to -14 LUFS with a true peak near -3 dBTP, lower than the usual -1.5: the AAC encode in the
second render lifted peaks by 0.7 dB and put that file 0.2 dB over the limit.
Measured, not heard: every row above is a number from a script.
