# An AI judge that measures the finished film and lists timed defects (step 9 of 10: review)

The agent that made the film did not grade it. Three separate agents, each with a fresh context and only the film, the brief, the reference clip and the expected lines, measured it and then opened every flag to see if it was real.

## What did the agent do in this step?

- Round 1 on the first render: 15 tool flags, 12 overturned, leaving 2 major and 4 minor defects, each with a time and a number.
- Fixed them in renders 3 to 5: the card that hung 15 to 20 px above the hand, banding in the dark corridor, small type, one-frame mouth shapes.
- Round 2 on the fourth render: nothing major, four minor rows, for example music that stopped 263 ms after its cut.
- Round 3 on the seventh render: thirteen named checks, no measured defect, six minor notes left open on purpose.
- The maker's own script read every frame of that seventh render: label on 980 of 980 frames, no black frame, no frozen stretch, −14.2 LUFS, 71 of 71 script words heard by Whisper: [measured_v007.md](measured_v007.md).
- Wrote down what no round checked: nobody listened to the sound, nobody rated whether it is funny, and no law or platform rule was checked: [review.md](review.md).
- After the rounds, an eighth render corrected the photo credit on the end card. The maker's script measured it; no judge read it again: [measured_v008.md](measured_v008.md).

## Which files should you open?

| File | What it holds |
|---|---|
| [review.md](review.md) | the three rounds: findings, what was changed, flags that were overturned, what nobody checked |
| [round1_verdict.md](round1_verdict.md) | the first judge's own verdict on the first render, as it wrote it |
| [measured_v007.md](measured_v007.md) | every-frame measurements of the render the judges last read |
| [measured_v008.md](measured_v008.md) | the same for the final film |
| [spend.md](spend.md) | the bill |
| [inputs/expected_lines_v007.txt](inputs/expected_lines_v007.txt) | the lines the judge was told to expect |

The judges' frame dumps and working files are not in this repo.

## Which skill ran this step?

[`media-judge`](https://varg.ai/how-to/skills/media-judge) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill media-judge
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [8. Edit](../edit/README.md) · Next: [10. GitHub](../github/README.md) · [All ten steps](../README.md#the-10-steps)
