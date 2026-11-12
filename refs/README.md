# How the reference video was found and measured (step 1 of 10: references)

The request said "take another funny video and adjust it", so the first step finds that video, measures it and writes down what may be borrowed from it. The output is one primary reference with measured cuts, a dozen smaller reference cards with one job each, a list of jokes people had already liked, and a list of things the film must never do.

## What did the agent do in this step?

- Ran 23 searches in 20 logged packs over X, Wikimedia Commons, The Met, the Library of Congress and varg how to. Each pack is logged with its result count and what was kept: [queries.md](queries.md).
- Picked Apple's September 2026 keynote opener as the video to adjust and measured it: 20.78 s, four shots, cuts at 3.14, 6.24 and 16.82 s (ffmpeg scene detection), word times with Whisper: [timing.md](timing.md).
- Measured its palette and light into five colours with hex values, added one accent colour, and wrote a type table: [DESIGN.md](DESIGN.md).
- Read the replies under the most-liked post about the replacement rumour. "Folding GPUs" had 955 likes and "selling the power cable separately" had 684, so both became lines: [trends.md](trends.md).
- Found the figure style in three public-domain photo collages from about 1875 at The Met: a large photographed head on a small printed body.
- Wrote eleven tests that reject a frame, a line or a voice, before anything was made: [never.md](never.md).
- Wrote ten different ideas from the same references and made the first: [ideas.md](ideas.md).

## Which files should you open?

| File | What it holds |
|---|---|
| [refs.md](refs.md) | every reference card: what it lends, what must not be copied, its rights and where it was found |
| [timing.md](timing.md) | the reference clip beat by beat, and the target timing for this film |
| [DESIGN.md](DESIGN.md) | palette, light and type measured from the reference |
| [trends.md](trends.md) | the week's posts and the jokes people had already voted on |
| [never.md](never.md) | the rejection tests |
| [queries.md](queries.md) | the search log |
| [ideas.md](ideas.md) | ten ideas, one made |
| [links.md](links.md) | sites only a person may open |

Apple's clip and its frames are not in this repo: they are not ours to publish. The reference cards link to the sources.

## Which skill ran this step?

[`find-references`](https://varg.ai/how-to/skills/find-references) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill find-references
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Next: [2. Moodboard](../look/README.md) · [All ten steps](../README.md#the-10-steps)
