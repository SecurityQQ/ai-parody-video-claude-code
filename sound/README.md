# AI voices, music and effects on one clock, mixed and checked by script (step 3 of 10: sound)

Sound is locked before any picture exists: the voice lines are recorded, laid on a clock and mixed, and every later step reads its times from that clock. The cut follows the words, not the other way round.

## What did the agent do in this step?

- Auditioned six stock ElevenLabs voices, two per role, and picked three by measured pitch and pace: Brian for the director, Eric and Will for the two characters. Nothing was cloned.
- Recorded 14 lines with `eleven_v3`. Four short lines came back rushed, at 194 to 245 words a minute, so they were re-recorded with written pauses and landed at 129 to 179: [lines.md](lines.md).
- Generated two music cues: a low pulse that stops dead on the first "No", and a bright cue from the catch to the end, played 1.9% faster so its last bar ends on the end-card cut.
- Kept eight effects and a room tone from ten paid calls, each effect placed on the frame of the action it belongs to. The music and effect prompts as sent were not kept; [plan.md](plan.md) describes each sound.
- Laid everything on one clock with [tools/build_sound.py](../tools/build_sound.py): [cues.json](cues.json) for the mixer and [beats.json](beats.json) for the picture, with every event snapped to the 24 fps grid.
- Mixed and checked with the skill's `sound.py`: −14.2 LUFS, voice 13.2 dB above the music, 10 of 10 effects within one frame, no dead air. 7 of 7 checks pass: [check.json](check.json).
- Planned the silences on purpose, for example 0.9 s after the director's "No.": [plan.md](plan.md).

## Which files should you open?

| File | What it holds |
|---|---|
| [plan.md](plan.md) | the sound plan beat by beat, and the check table |
| [lines.md](lines.md) | every line as sent to the voice model, with take, time and pace |
| [cues.json](cues.json) | every sound with its time and level |
| [beats.json](beats.json) | the clock the picture is cut to |
| [check.json](check.json) | the mix checks |

Voice takes, music, effects and the mix are in `media.zip` under `sound/`. The sound was measured, not listened to.

## Which skill ran this step?

[`video-sound`](https://varg.ai/how-to/skills/video-sound) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill video-sound
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_adb09f98b297.mp4) · [the whole project](../README.md)

Previous: [2. Moodboard](../look/README.md) · Next: [4. Script](../story/README.md) · [All ten steps](../README.md#the-10-steps)
