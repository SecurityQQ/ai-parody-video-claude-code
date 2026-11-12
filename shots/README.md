# Which shots go to an AI video model and which to code (step 7 of 10: video generation)

Every shot is routed by one rule, first yes wins: exact things (text, faces from photos, timing to a word) go to code; a camera move that must be obeyed gets the blockout as a video reference; the rest is a prompt and a start frame. Two of six shots went to a video model.

## What did the agent do in this step?

- Routed all six shots in one table with the reason for each: [shots.md](shots.md).
- sh010, the atrium: image-to-video from a generated still on Seedance 2.5 at 480p, 5 s. Estimated up to $0.54, charged $0.52: [sh010/shot.md](sh010/shot.md).
- sh020, the sneakers: Seedance 2.5 with the grey blockout clip as a video reference, so the camera path is obeyed. Charged $0.62: [sh020/shot.md](sh020/shot.md).
- Made one take of each, looked at frames of it against the shot's requirements (four for the first shot, six for the second), and kept it.
- Asked for a price estimate on the real request before each call and logged estimate against charge: [runs.md](runs.md).
- Numbered shots in tens (`sh010`, `sh020`) so a shot can be added between two others, and never overwrote a take.

## Which files should you open?

| File | What it holds |
|---|---|
| [shots.md](shots.md) | the routing table |
| [runs.md](runs.md) | estimates and charges |
| [sh010/shot.md](sh010/shot.md) | prompt as sent, model, price, what was checked |
| [sh020/shot.md](sh020/shot.md) | the same for the guided shot |

The two approved takes are in `media.zip` under `shots/`.

## Which skill ran this step?

[`video-animate`](https://varg.ai/how-to/skills/video-animate) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill video-animate
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [6. Blockout](../blockout/README.md) · Next: [8. Edit](../edit/README.md) · [All ten steps](../README.md#the-10-steps)
