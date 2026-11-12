# Editing a video as code with HyperFrames: puppets, captions and labels (step 8 of 10: edit)

The edit is a HyperFrames project: HTML, CSS and GSAP timelines that render to MP4 frame by frame, so every render is identical and any line can be changed in text. One script writes the whole project from the sound clock.

## What did the agent do in this step?

- [tools/build_edit.py](../tools/build_edit.py) writes the project at 854×480 and 24 fps: [index.html](index.html) and five scenes in [compositions/](compositions/s3.html).
- Built each character as a puppet: a body, a head and a jaw. The jaw's drop follows the loudness of that character's voice line, frame by frame, held on twos, with four mouth shapes.
- Made the light strip across the eyes with three copies of the figure in step: lit, dark with a hole, and fully dark.
- Made the rack focus by cross-fading to a blurred copy while the man behind the glass comes into light.
- Set every word on screen in code: the premise bar, the PARODY tag in all frames, lower thirds, paper tags, 18 caption groups and the end card.
- Baked fine grain into the dark plates after the judge measured banding, and moved every pose change 4 ms early after it found mouth shapes lasting one frame.
- Rendered eight times with `bunx hyperframes@0.9.15 render --fps 24 --quality looks`. The project check reports 0 errors.

## Which files should you open?

| File | What it holds |
|---|---|
| [index.html](index.html) | the root composition: scenes, the two AI shots and the audio |
| [compositions/s3.html](compositions/s3.html) | the dark corridor: the reveal, "Not you", the jacket |
| [compositions/s4.html](compositions/s4.html) | daylight: the greeting, the card that folds, the tags |
| [compositions/end.html](compositions/end.html) | the name badge and the credits |
| [compositions/labels.html](compositions/labels.html) | the premise bar, the PARODY tag, lower thirds |
| [compositions/captions.html](compositions/captions.html) | the captions |
| [captions.json](captions.json) | caption text and times |

`edit/assets/` is rebuilt by `tools/build_edit.py` from `media.zip`.

## Which skill ran this step?

[`edit-footage-with-code`](https://varg.ai/how-to/skills/edit-footage-with-code) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill edit-footage-with-code
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [7. Video generation](../shots/README.md) · Next: [9. AI judge](../review/README.md) · [All ten steps](../README.md#the-10-steps)
