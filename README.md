<div align="center">

# AI parody video made with Claude Code: the full project, 10 steps, $2.12

**A worked example: one request to an AI agent in, a finished 41-second parody film out.**<br>
The shot and character prompts, the script, the voice lines, the edit as code, the AI judges' findings and the bill are in this repo,<br>
so you or your agent can copy the method for your own video.

[![Made with varg skills][b-varg]][skills] [![Claude Code][b-cc]](#make-your-own) [![HyperFrames][b-hf]](edit/README.md) [![Cost: $2.12][b-cost]](#what-did-it-cost) [![MIT license][b-mit]](LICENSE)

<a href="https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4"><img src="https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_523fd8925738.webp" width="640" alt="Animated preview of the AI parody video Not you: a paper cut-out of Jensen Huang is lit by a strip of green light in a dark corridor, a director says Not you, his leather jacket flies to Tim Cook, who shows a graphics card with tags reading It folds and Power cable sold separately, and a name badge reads Tim Nvidia. A PARODY label is in the corner of every frame."></a>

**[▶ Watch the film (MP4, 41 s, with sound)](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4)** · **[Read this as a web page](https://securityqq.github.io/ai-parody-video-claude-code/)**

[The request](#the-request) · [The 10 steps](#the-10-steps) · [Cost](#what-did-it-cost) · [Real people](#how-were-the-real-people-handled) · [The AI judge](#what-did-the-ai-judge-find) · [Make your own](#make-your-own) · [Rebuild](#rebuild-the-film) · [For AI agents](#for-ai-agents) · [FAQ](#faq)

</div>

> **This is a parody, not news.** Nobody shown said any of these lines, and the film claims nothing about real events. The word PARODY is on screen in all 980 frames, and the end card reads "Parody. Nobody said this."

## What is this?

"Not you." is a 40.8-second parody video at 854×480. A film director re-casts Nvidia's keynote opener on camera: he stops Jensen Huang in the first ten seconds, takes the leather jacket and hands the show to Tim Cook, who presents a graphics card that folds. The video it adjusts is Apple's September 2026 keynote opener, in which Tim Cook hands the opening to someone else; here the handoff is flipped and the keynote is Nvidia's.

An AI agent made it on 2026-11-11 from one request: Claude Code running Claude Fable 5.2, with ten open-source [varg video skills][skills] and the image, voice, music and video models behind one [varg](https://varg.ai) account. This repo is the project as the agent left it, cleaned for publishing: references, moodboard, script, sound plan, character sheets, 3D blockout, shot prompts, the edit as a [HyperFrames](https://github.com/heygen-com/hyperframes) project, and the judge's measured reports.

| | |
|---|---|
| Film | 40.8 s, 980 frames at 24 fps, 854×480 (480p), −14.2 LUFS |
| Made by | Claude Code (Claude Fable 5.2) from one request; nobody steered it until the film was done |
| Method | 10 steps, one [varg skill][skills] each |
| Paid model calls | **$2.12** in total ([the bill](#what-did-it-cost)) |
| Shots | 6: two AI video shots (Seedance 2.5), four animated in code (HyperFrames + GSAP) |
| Voices | 14 lines on 3 stock ElevenLabs voices. No voice was cloned |
| Faces | Freely licensed photos, cut out and edited by code. No generative model was given a photo of either man |
| Quality control | 3 rounds by independent AI judges over 7 renders; the last found no measured defect on 13 checks. An eighth render only corrects the photo credit |
| Licence | Code and text: MIT. Photos keep their own licences ([credits](CREDITS.md)) |

<p align="center"><img src="https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_9945c5231f8d.jpg" width="820" alt="Four stages of making the AI parody video: a generated dark corridor plate, paper-doll bodies and props generated from a text prompt, a grey three.js blockout of the same shot, and the final frame with a photo cut-out head and code-set labels"></p>

## The request

The whole brief, as typed:

> make a video where tim cook is replacing jensen huang because of the model incident. take their pictures and make a funny video with it; make it 480p please
>
> use ten steps [one guide per step: references, moodboards, sounds, video scripts, characters, Blender/three.js, video generation, HyperFrames, AI judge, GitHub]
>
> Mostly just take another funny video and adjust it.

The agent read "another funny video" as Apple's keynote opener, in which Tim Cook says "No, no, no, no, no. Not me. That's your guy." and hands the opening to someone else. Here the director says "Not you." Its full reading of the request, and the limits it set for itself, are in [brief.md](brief.md). A prompt you can paste to make your own is in [PROMPT.md](PROMPT.md).

## The 10 steps

Each step has a folder with a short README, the working files and the skill that ran it. Start anywhere.

| # | Step | The question it answers | What the agent did here | Skill on varg.ai |
|---|---|---|---|---|
| 1 | [References](refs/README.md) | Which existing video do we adjust, and what exactly does it do? | 23 logged searches, most of them over X, Wikimedia Commons, The Met and the Library of Congress. Picked Apple's opener and measured it: cuts at 3.14, 6.24 and 16.82 s, palette, word times. Read which jokes people had already liked | [`find-references`](https://varg.ai/how-to/skills/find-references) |
| 2 | [Moodboard](look/README.md) | What must every frame look like, in numbers? | Five palette colours measured from the reference plus one accent, light and framing per shot, type sizes. Five test stills on two image models, each checked against the palette | [`video-moodboard`](https://varg.ai/how-to/skills/video-moodboard) |
| 3 | [Sound](sound/README.md) | Who speaks, how fast, and where does the music stop? | Six stock voices auditioned and three picked, 14 lines recorded, 4 re-recorded because the voice model rushed short lines. Two music cues, eight effects and a room tone. The picture is cut to this clock | [`video-sound`](https://varg.ai/how-to/skills/video-sound) |
| 4 | [Script](story/README.md) | What is said, in how many seconds, and is each claim allowed? | 14 lines, 71 words. Two jokes come from replies that already had 955 and 684 likes; two lines are the reference's own narration. A facts file lists what may be said | [`video-script`](https://varg.ai/how-to/skills/video-script) |
| 5 | [Characters](cast/README.md) | How do two real people appear without a generated face? | Heads cut from licensed photos with a face mesh; the jaw drops in a slot like a marionette. Bodies and props generated from words on one sheet for $0.06 | [`character-passport`](https://varg.ai/how-to/skills/character-passport) |
| 6 | [Blockout](blockout/README.md) | Where is everyone, and where is the camera, on every frame? | The whole film staged in three.js in metres and seconds, driven by the sound clock. Five rounds. One grey guide clip for the tracking shot | [`code-to-video-previz`](https://varg.ai/how-to/skills/code-to-video-previz) |
| 7 | [Video generation](shots/README.md) | Which shots need an AI video model, and which are better as code? | Two shots went to Seedance 2.5 at 480p ($0.52 and $0.62, one take each). Four shots with faces, text and exact timing went to code | [`video-animate`](https://varg.ai/how-to/skills/video-animate) |
| 8 | [Edit](edit/README.md) | How do the pieces become one film that can be re-rendered? | A HyperFrames project: photo puppets whose jaws follow the voice's loudness, captions, labels, the end card. Rendered eight times | [`edit-footage-with-code`](https://varg.ai/how-to/skills/edit-footage-with-code) |
| 9 | [AI judge](review/README.md) | What is wrong with it, measured, by someone who did not make it? | Three separate agents measured the film. Round 1 found 2 major and 4 minor defects; round 3 found none on 13 checks | [`media-judge`](https://varg.ai/how-to/skills/media-judge) |
| 10 | [GitHub](github/README.md) | Can the project be restored on another machine? | In the private working repo: text in git, media in Releases, and a fresh copy compared byte for byte (149 text files and 408 media files matched). This repo is a cleaned copy of it | [`video-project-github`](https://varg.ai/how-to/skills/video-project-github) |

## What did it cost?

$2.12, all through one varg account at provider price (1 credit = $0.01). The agent set itself a $15 cap and asked for a price estimate before every paid call. The figure is the model calls only: the agent's own usage (Claude Code) is not in it.

| What | Model | Calls | Cost |
|---|---|---|---|
| Watching reference and trend videos | varg `analyze_video`, a video-understanding model | 5 | $0.25 |
| 5 background plates on two models, 1 paper-doll sheet | [GPT Image 2.6](https://varg.ai/models/gpt_image_2_6), [Nano Banana 2.1](https://varg.ai/models/nano_banana_2_1) | 6 | $0.31 |
| 6 audition lines, 14 lines, 4 re-takes | [ElevenLabs v3](https://varg.ai/models/eleven_v3) | 24 | $0.24 |
| 2 music cues | [ElevenLabs Music v2.5](https://varg.ai/models/eleven_music_v2_5) | 2 | $0.08 |
| 8 sound effects and a room tone kept, from 10 paid calls | [ElevenLabs Sound Effects v3](https://varg.ai/models/eleven_sound_effects_v3) | 10 | $0.10 |
| 2 video shots, 5 s each at 480p | [Seedance 2.5](https://varg.ai/models/seedance_2_5) | 2 | $1.14 |
| **Total** | | | **$2.12** |

Free: the three.js blockout, the HyperFrames edit and all eight renders, background removal, transcription and the judge's measurements. Line by line: [review/spend.md](review/spend.md).

## How were the real people handled?

The film shows two real, named people, so the agent wrote rules before making anything ([refs/never.md](refs/never.md)) and the judge checked them at the end.

- **Photos, not generated faces.** Both heads are freely licensed photos from Wikimedia Commons (CC BY 4.0, CC BY 2.0, public domain), edited by code only: cut out, the jaw separated so it can move, a band of teeth drawn behind it, a darkened copy for the unlit shots. No generative model was given a photo of either man, and nothing generated, redrew or lip-synced a face. Two local models that do not generate touched the photos: one removed the background, one found the lips. Credits: [CREDITS.md](CREDITS.md).
- **Bodies from words.** The paper-doll bodies, the jacket and the card were generated from a text prompt that names nobody ([cast/sheets/prompt.md](cast/sheets/prompt.md)).
- **Stock voices.** Three library voices picked for pitch and pace. Nothing was cloned and none is meant to sound like either man. Nobody has checked that by ear.
- **A label on every frame.** PARODY sits in the same corner from the first frame to the last (measured: 980 of 980 frames), and the end card says nobody said this.
- **It cannot pass for footage.** White cut edges, a head too big for its body, a flat photo over a soft set. The judge's check "would a frame pass as real with the label cropped off" came back no.
- **It does not say what happened.** The request's "model incident" appears as the opening title ("Nvidia's keynote opener, after the model incident") and as the word "model" in three lines of dialogue. The film does not say what the story was, this project did not verify it and repeats none of it, and nobody else is shown or named. The other jokes are about product habits: it folds, the cable is sold separately, it is a subscription now.

This is what this project did, not legal advice. Likeness and parody rules differ by country and by platform, and nobody checked them here.

## What did the AI judge find?

The agent that made the film did not grade it. Three separate agents, each with a fresh context and only the film, the brief, the reference and the expected lines, measured it with the [`media-judge`](https://varg.ai/how-to/skills/media-judge) skill and then opened every flag.

| Round | Film | Verdict | Examples of what it measured |
|---|---|---|---|
| 1 | v001 | 2 major, 4 minor | The folded card hung 15 to 20 px above the hand for 150 frames; banding in the dark corridor (CAMBI 5.41, limit 5); mouth shapes lasting one frame |
| 2 | v004 | no major, 4 minor | The music stopped 263 ms after the cut it belonged to; the end card had 26 words in 3.3 s |
| 3 | v007 | no measured defect on 13 checks, 6 notes left open | Label on 980 of 980 frames; 18 of 18 captions match the script; −14.2 LUFS; no frozen stretch |

After round 3 an eighth render corrected the photo credit on the end card; it was measured by script and not judged again. Every finding and what was changed for it: [review/review.md](review/review.md). The first judge's own verdict: [review/round1_verdict.md](review/round1_verdict.md). The judges measured the sound; nobody listened to it, and nobody rated whether it is funny. That list is in the same file under "What no round checked".

## Make your own

1. Install the ten skills in your agent (Claude Code, Codex, Grok, Cursor, Gemini CLI and others). This needs Node.js for `npx`; the blockout, edit and renders also need ffmpeg, Python 3 and [Bun](https://bun.sh):

   ```bash
   npx skills add vargHQ/skills --skill find-references --skill video-moodboard --skill video-sound \
     --skill video-script --skill character-passport --skill code-to-video-previz --skill video-animate \
     --skill edit-footage-with-code --skill media-judge --skill video-project-github
   ```

2. Connect the models: add the varg MCP server `https://mcp.varg.ai/mcp` (sign in with OAuth) or set `VARG_API_KEY` from [varg.ai](https://varg.ai). One key covers Seedance, Kling, Veo, GPT Image, Nano Banana and ElevenLabs. A new account starts with free credits, enough for stills but not for a film.

3. Find the photos yourself or let the agent search: [Wikimedia Commons](https://commons.wikimedia.org) lists the licence of every photo. This project took only CC BY and public-domain photos and kept their credits.

4. Paste a request. The one below is this project's request with the blanks left for you ([PROMPT.md](PROMPT.md) has it with notes):

   ```text
   Make a funny 480p parody video: <who> takes over from <who> because of <what happened>.
   Mostly just take another funny video and adjust it.
   Use their real, freely licensed photos as paper cut-outs. Never give a photo of a real
   person to an image or video model, never clone a voice, and keep a PARODY label in every frame.
   Work in ten steps with the varg skills: find-references, video-moodboard, video-sound,
   video-script, character-passport, code-to-video-previz, video-animate, edit-footage-with-code,
   media-judge, video-project-github.
   Use https://github.com/SecurityQQ/ai-parody-video-claude-code as the worked example.
   Show me a price estimate before you spend anything.
   ```

More formats, each with its own skills and example videos: [varg how to](https://varg.ai/how-to). This film's method in general form: [how to remake a reference video with AI](https://varg.ai/how-to/remake-a-reference-video). More videos made with the same model: [make videos with Claude Fable 5.2](https://varg.ai/how-to/make-videos-with-claude-fable-5-2).

## Rebuild the film

The edit is text, so the film can be rendered again or changed line by line. You need Python 3.9+ with Pillow, ffmpeg, [Bun](https://bun.sh) and the GitHub CLI.

```bash
git clone https://github.com/SecurityQQ/ai-parody-video-claude-code && cd ai-parody-video-claude-code
gh release download media-v1 -p media.zip && unzip -o media.zip      # photos, plates, voices, music, the two AI shots (49 MB)
git clone https://github.com/vargHQ/skills ../varg-skills              # the sound mixer and the judge live in the skills

python3 tools/build_sound.py                                           # voice lines onto the clock -> sound/cues.json, beats.json
python3 ../varg-skills/video-sound/scripts/sound.py mix sound/cues.json -o sound/mix.wav
python3 tools/build_edit.py                                            # assets + HyperFrames scenes -> edit/
cd edit && bunx hyperframes@0.9.15 check --json
bunx hyperframes@0.9.15 render --fps 24 --quality looks --output ../renders/film.mp4 && cd ..
python3 tools/measure_film.py renders/film.mp4                         # size, label on every frame, loudness
```

To change a line, edit `LINES` in [tools/build_sound.py](tools/build_sound.py) and record the new take with any text-to-speech model; the cut follows the sound. Pinned versions: hyperframes 0.9.15, gsap 3.15.0, mediapipe 0.10.14 (only for cutting the heads), voices on `eleven_v3`.

## For AI agents

- **Read first:** [llms.txt](llms.txt) lists every file worth opening with one line each. [AGENTS.md](AGENTS.md) says how to reuse this project for a new video and what not to copy.
- **The order of work:** [brief.md](brief.md), then the ten step READMEs in the table above. Each one names the files that are the step's output.
- **Skills:** install the ten with the command under [Make your own](#make-your-own), or read https://raw.githubusercontent.com/vargHQ/skills/main/llms.txt and pick by task. Each step's skill is linked in its README and on [varg how to](https://varg.ai/how-to).
- **Generate:** the varg MCP (`https://mcp.varg.ai/mcp`, OAuth) or `VARG_API_KEY` against `https://api.varg.ai/v2`. Model ids, inputs and limits: [varg.ai/models/llms.txt](https://varg.ai/models/llms.txt). Take prices from an estimate call, never from this page.
- **Real people:** follow [refs/never.md](refs/never.md). Do not give a real person's photo to a generative model, do not clone a voice, keep the label.

## FAQ

### Can Claude Code make a video?

Yes. Here it wrote the script, generated the voices, music, images and two video shots through varg, animated the rest as HTML and GSAP in HyperFrames, rendered the MP4 with ffmpeg and had other agents judge the result. Claude Code does not generate pixels itself: it writes code and calls models. The skills tell it which to use for what.

### How much does an AI video like this cost?

This one cost $2.12 in model calls for 40.8 seconds at 480p, not counting the agent's own usage (Claude Code). The two AI video shots were $1.14 of that; everything coded was free to render. Higher resolutions and more AI shots cost more, so the agent asks for an estimate before each call.

### Which AI models were used?

Seedance 2.5 for two video shots, GPT Image 2.6 and Nano Banana 2.1 for background plates and the paper-doll sheet, ElevenLabs v3 for voices, ElevenLabs Music v2.5 for two cues and ElevenLabs Sound Effects v3 for eight effects and a room tone, all through [varg](https://varg.ai). A video-understanding model (varg `analyze_video`) watched the reference clips. Whisper, a background-removal model and a face mesh model ran locally, for checks and for cutting the heads.

### How do you make a parody of a real person with AI without making a deepfake?

This project kept the faces as licensed photos edited only by code (cut out, with a moving jaw), animated them as paper cut-outs, used stock voices, and kept a PARODY label on every frame. No generative model made, edited or lip-synced a real face. The exact rules are in [refs/never.md](refs/never.md); the law where you live and the rules of the platform you post on are yours to check.

### How does the mouth move if no model animates the face?

Code cuts the lower jaw out of the photo along the lips, found with a face mesh, and slides it down in a slot, like a marionette. How far it drops follows the loudness of that character's voice line, frame by frame, held for two frames at a time. See [tools/head_cut.py](tools/head_cut.py) and [tools/build_edit.py](tools/build_edit.py).

### Why were only two shots made with an AI video model?

The agent's rule: exact things go to code, and a model gets only what nothing exact depends on. Faces from photos, on-screen text and timing to a spoken word are exact, so four shots are code. A wide shot of a walker and a tracking shot of sneakers have no face, no text and no word to hit, so they went to Seedance 2.5. The table is in [shots/shots.md](shots/shots.md).

### Why 480p?

The request asked for it. It also keeps AI video cheap, and since the film is finished at 480p there was no upscale pass.

### Can I reuse the code?

Yes, the code and text are MIT licensed. The photos keep their own licences and need their credits ([CREDITS.md](CREDITS.md)). To make a different parody, replace the photos, the lines and the plates; the tools do not depend on who is in the film.

### Is any of this real?

No. Nobody shown said these lines and the film makes no claim about real events. It is a joke built on a week of jokes on X, and it says so on every frame.

## Credits and licence

- **Photos:** Tessa Bury (CC BY 4.0), 總統府 / Office of the President, Taiwan (CC BY 2.0), The White House (public domain), via Wikimedia Commons. Full table and what was changed: [CREDITS.md](CREDITS.md).
- **Reference:** Apple's September 2026 keynote opener: its structure, its timing and two of its narrator's lines, quoted for parody ("Cut to an interior. Camera follows a mysterious figure... before revealing our main character." and "That's your opener."). None of its footage, sound or imagery is in the film or in this repo.
- **Jokes:** "it folds" and "the power cable is sold separately" come from replies on X, credited in [refs/trends.md](refs/trends.md).
- **Code and text:** MIT, see [LICENSE](LICENSE). **Film and generated media:** watch, link and embed with a credit to this repo; open an issue here to ask about other uses.

Related: [vargHQ/skills][skills] (the skills used here, plus about 70 more) · [vargHQ/code2video-templates](https://github.com/vargHQ/code2video-templates) (video templates that render from code) · [varg how to](https://varg.ai/how-to) (guides, skills and prompts for AI video) · [varg models](https://varg.ai/models) (every model with its price)

<p align="center"><sub>Made by an AI agent with <a href="https://varg.ai">varg</a> · <a href="https://varg.ai/how-to">varg how to</a> · Parody: nobody said this.</sub></p>

[skills]: https://github.com/vargHQ/skills
[b-varg]: https://img.shields.io/badge/made%20with-varg%20skills-76B900
[b-cc]: https://img.shields.io/badge/agent-Claude%20Code-D97757
[b-hf]: https://img.shields.io/badge/edit-HyperFrames-1f6feb
[b-cost]: https://img.shields.io/badge/model%20cost-%242.12-76B900
[b-mit]: https://img.shields.io/badge/code-MIT-blue
