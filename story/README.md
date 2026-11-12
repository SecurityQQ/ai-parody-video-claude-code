# A parody script in 14 lines, each sized to its seconds (step 4 of 10: script)

The script is written as a table: what is said, what is on screen, what is seen and what is heard, per beat, with the seconds each beat may take. A facts file next to it lists the only things the film is allowed to state.

## What did the agent do in this step?

- Wrote one promise and the last line first, then the beats between them: [script.md](script.md).
- Kept it to 14 lines and 71 words for three voices. The script checker passed with 0 failures and 2 warnings.
- Built the middle as a question ladder: "Is this about the model?" / "It's about the model." / "The language model?" / "No."
- Took two jokes from replies people had already liked, and the end card from a third. Kept two of the reference's narrator lines word for word, because the parody rests on them.
- Listed six facts with sources, marked two as inferred, and wrote down what the film does not claim: [facts.md](facts.md).
- Added an "as cut" table after the edit, with the times the lines really landed on.

## Which files should you open?

| File | What it holds |
|---|---|
| [script.md](script.md) | the script table, the strategy line and the as-cut times |
| [facts.md](facts.md) | what may be said, with sources |

## Which skill ran this step?

[`video-script`](https://varg.ai/how-to/skills/video-script) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill video-script
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [3. Sound](../sound/README.md) · Next: [5. Characters](../cast/README.md) · [All ten steps](../README.md#the-10-steps)
