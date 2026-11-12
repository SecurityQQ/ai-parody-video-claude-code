# A moodboard an AI image model can follow, checked on stills (step 2 of 10: look)

The moodboard turns the reference into lines a frame can be checked against: colours as hex values, light as percentages, framing as shot size, camera height and lens. Then it is tested on stills before any video is made.

## What did the agent do in this step?

- Wrote the look in one sentence and every other line as a number: five measured palette colours and one accent, light per shot, a framing table for all shots, a type table: [moodboard.md](moodboard.md).
- Generated five test stills on two image models, GPT Image 2.6 and Nano Banana 2.1, from the board's lines alone.
- Measured each still against the board: palette distance (mean ΔE) from 4.8 to 14.8, each under its bar; in the dark corridor 94% of pixels are below half grey, as asked.
- Kept three stills as the film's background plates: the dark corridor, the daylight corridor and the atrium that starts the first shot. They were prompted from the board's lines; the prompts as sent were not kept as separate files.
- Fixed the motion rule for the edit: figures move on twos (12 poses a second), props on ones.

## Which files should you open?

| File | What it holds |
|---|---|
| [moodboard.md](moodboard.md) | the board: look, light, palette, framing, type, motion, the never list and the table of test stills |

The stills are in `media.zip` under `look/stills/`.

## Which skill ran this step?

[`video-moodboard`](https://varg.ai/how-to/skills/video-moodboard) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill video-moodboard
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [1. References](../refs/README.md) · Next: [3. Sound](../sound/README.md) · [All ten steps](../README.md#the-10-steps)
