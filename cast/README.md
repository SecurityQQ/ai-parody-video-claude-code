# Real people as photo cut-outs, without generating a face (step 5 of 10: characters)

The two characters are real people, so their faces are never generated. Each head is a licensed photo cut out by code, with a jaw that drops in a slot like a marionette. The bodies and props are paper dolls generated from words.

## What the agent did

- Wrote a passport for each paper figure: premise, what he wants, silhouette, and a table of pieces with the source of each: [jensen.md](jensen.md), [tim.md](tim.md).
- Cut three heads from three photos with [tools/head_cut.py](../tools/head_cut.py): background removed, a face mesh finds the lips, the lower jaw becomes a separate piece, and a band of teeth is painted behind it.
- Kept an uncut copy of each head for silent moments, so the jaw's seam only exists while the character speaks.
- Generated every body and both props on one sheet with GPT Image 2.6, transparent background, for $0.06. The prompt names nobody and no reference image was attached: [sheets/prompt.md](sheets/prompt.md).
- Split the sheet into six pieces by its transparent gaps with [tools/split_sheet.py](../tools/split_sheet.py).
- Wrote motion notes for the props, for example how the jacket leaves, turns and lands: [props.md](props.md).

## Files to open

| File | What it holds |
|---|---|
| [jensen.md](jensen.md) | the outgoing opener: design and pieces |
| [tim.md](tim.md) | the new opener: design and pieces |
| [props.md](props.md) | the jacket and the card |
| [board.md](board.md) | the cast on one page, with measured voice pace |
| [sheets/prompt.md](sheets/prompt.md) | the paper-doll sheet prompt, as sent |

Photos, the sheet and the cut-outs are in `media.zip`. Photo credits: [CREDITS.md](../CREDITS.md).

## The skill

[`character-passport`](https://varg.ai/how-to/skills/character-passport) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill character-passport
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_12b7a91f86db.mp4) · [the whole project](../README.md)

Previous: [4. Script](../story/README.md) · Next: [6. Blockout](../blockout/README.md) · [All ten steps](../README.md#the-10-steps)
