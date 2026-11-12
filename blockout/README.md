# A three.js blockout of the whole film before any video is generated (step 6 of 10: previz)

Before anything is animated or generated, the whole film is staged once as grey boxes in a 3D scene, in real metres and on the sound's clock. It settles where everyone stands, where the camera is and what lens it has, for free.

## What did the agent do in this step?

- Staged three sets and one camera per shot in three.js. The scene is data: [make_staging.py](make_staging.py) writes [staging.json](staging.json) from the sound clock.
- Gave every shot a height, a lens and a move, for example the sneaker shot: 14 cm above the floor, 35 mm, tracking at 0.82 of the walker's speed: [REPORT.md](REPORT.md).
- Ran the skill's staging check and fixed what it found: figures jumping on cut frames, feet off the bridge, a figure visible too early.
- Rendered five rounds and looked at contact sheets of four. A round renders about 870 frames in 15 to 23 s.
- Rendered one grey guide clip of the tracking shot and gave it to the video model as a video reference in the next step.

## Which files should you open?

| File | What it holds |
|---|---|
| [REPORT.md](REPORT.md) | the blockout report: beats in seconds and metres, cameras, what each round changed |
| [make_staging.py](make_staging.py) | writes the scene from the sound clock |
| [staging.json](staging.json) | the scene: sets, figures, cameras, keys |
| [staging_guide_sh020.json](staging_guide_sh020.json) | the scene for the guide clip |
| [contact_sheet.py](contact_sheet.py) | frames of every shot on one sheet |

Contact sheets are in `media.zip` under `blockout/stills/`.

## Which skill ran this step?

[`code-to-video-previz`](https://varg.ai/how-to/skills/code-to-video-previz) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill code-to-video-previz
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [5. Characters](../cast/README.md) · Next: [7. Video generation](../shots/README.md) · [All ten steps](../README.md#the-10-steps)
