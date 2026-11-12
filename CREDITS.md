# Credits

## Photos

Every photo of a real person in this film, from Wikimedia Commons. Downloaded 2026-11-11 at 1280 px wide.
The licence covers the photographer's copyright only, not the right of the person shown to control their image.

| File (in `media.zip`) | Used for | Author | Licence | Taken | Source page |
|---|---|---|---|---|---|
| `inputs/photos/jen_hsun_huang_2025_2.jpg` | Jensen Huang head, smiling | The White House | Public domain | 2025-11-18 | https://commons.wikimedia.org/wiki/File:Jen-Hsun_Huang_2025_(2).jpg |
| `inputs/photos/jensen_huang_20231109.jpg` | Jensen Huang head, surprised, mouth open | 總統府 (Office of the President, Taiwan) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | 2023-11-09 | https://commons.wikimedia.org/wiki/File:Jensen_Huang_20231109.jpg |
| `inputs/photos/tim_cook_march_2026.jpg` | same photo, uncropped (spare) | Tessa Bury | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 2026-03-13 | https://commons.wikimedia.org/wiki/File:Tim_Cook_March_2026.jpg |
| `inputs/photos/tim_cook_march_2026_cropped.jpg` | Tim Cook head and waving hand | Tessa Bury | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 2026-03-13 | https://commons.wikimedia.org/wiki/File:Tim_Cook_March_2026_(cropped).jpg |

Changes made: background removed, cropped at the neck, lower jaw cut so it can move, edge outline added. The cut-out
heads in `cast/cutouts/` are adaptations of these photos and carry the same credits.
Not used: any CC BY-SA photo (share-alike would bind the film), any photo with no licence record.

## References (looked at, not copied)

- Apple's September 2026 keynote opener: structure and timing only. Its footage, sound and frames are not in the film
  and not in this repo. The clip the agent measured: https://x.com/aaronp613/status/2097785879041351803
- Juan Pedro Chabalgoity, photo collages, about 1875, The Metropolitan Museum of Art (public domain, Open Access):
  the idea of a large photographed head on a small printed body. Object numbers 764771, 764769, 764776.
- Jokes that people had already liked under a post on X: "folding GPUs" (@viperr), "selling the power cable
  separately" (@Slobodan88), "From Tim Apple to Tim Nvidia" (@masonisonx). See [refs/trends.md](refs/trends.md).

## Voices, music and effects

- Voices: three stock ElevenLabs library voices (Brian as the director, Eric and Will as the two characters), model
  `eleven_v3`. No voice was cloned and none is meant to sound like a real person.
- Music: two cues generated with `eleven_music_v2_5`. Effects: `eleven_sound_effects_v3`.

## Models and tools

- Video: Seedance 2.5 at 480p (two shots). Images: GPT Image 2.6 and Nano Banana 2.1. All through [varg](https://varg.ai).
- Edit and render: [HyperFrames](https://github.com/heygen-com/hyperframes) 0.9.15, GSAP 3.15.0, ffmpeg.
- Blockout: three.js. Head cut-outs: MediaPipe face mesh 0.10.14. Checks: Whisper small.en, ffmpeg ebur128.
- Skills: [vargHQ/skills](https://github.com/vargHQ/skills). Agent: Claude Code (Claude Fable 5.2).

## Licence

Code and text in this repo: MIT ([LICENSE](LICENSE)). The photos keep the licences above. The film and the generated
media: watch, link and embed with a credit to this repo; ask before other uses.
