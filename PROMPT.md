# The prompt: make your own AI parody video

Paste this into Claude Code, Codex, Grok or any agent that can run skills. Fill the three blanks.

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

## Before you paste it

1. Install the ten skills (or tell the agent: "Install varg video skills by reading https://raw.githubusercontent.com/vargHQ/skills/main/llms.txt"):

   ```bash
   npx skills add vargHQ/skills --skill find-references --skill video-moodboard --skill video-sound \
     --skill video-script --skill character-passport --skill code-to-video-previz --skill video-animate \
     --skill edit-footage-with-code --skill media-judge --skill video-project-github
   ```
2. Connect the models: the varg MCP server `https://mcp.varg.ai/mcp` (OAuth), or `VARG_API_KEY` from [varg.ai](https://varg.ai).
3. Have Node.js (for `npx`), ffmpeg, Python 3 and [Bun](https://bun.sh) on the machine. The blockout, the edit and the renders run locally and cost nothing.
4. Photos of real people: [Wikimedia Commons](https://commons.wikimedia.org) lists the licence of every photo. This project took only CC BY and public-domain photos and kept their credits ([CREDITS.md](CREDITS.md)).

## What each line of the prompt does

| Line | Why it is there |
|---|---|
| "takes over from ... because of ..." | The premise in one sentence. The agent turns it into a promise and a last line before writing anything else ([story/script.md](story/script.md)) |
| "take another funny video and adjust it" | Tells the agent to find one reference, measure its cuts and re-stage it, instead of inventing a structure. Here that was Apple's keynote opener ([refs/refs.md](refs/refs.md)) |
| "freely licensed photos as paper cut-outs" | Real faces stay real photos with credits, edited by code only. No generative model touches a face ([cast/README.md](cast/README.md)) |
| "never clone a voice ... PARODY label in every frame" | The two rules that keep a parody from passing as footage. The judge measures the label on every frame ([review/review.md](review/review.md)) |
| "ten steps with the varg skills" | One skill per step, in this order, so sound is locked before any picture is made ([the table](README.md#the-10-steps)) |
| "as the worked example" | Gives the agent a finished project to compare its own files against |
| "price estimate before you spend" | This film cost $2.12 in model calls; the agent capped itself at $15 ([review/spend.md](review/spend.md)) |

## The request this film was made from

> make a video where tim cook is replacing jensen huang because of the model incident. take their pictures and make a funny video with it; make it 480p please
>
> use ten steps [one guide per step: references, moodboards, sounds, video scripts, characters, Blender/three.js, video generation, HyperFrames, AI judge, GitHub]
>
> Mostly just take another funny video and adjust it.

It was given as a standing goal, so the agent did not stop for approval between steps. With an ordinary request the skills stop and show stills before any video is paid for.

The skills behind the ten steps, each with examples: [find-references](https://varg.ai/how-to/skills/find-references) · [video-moodboard](https://varg.ai/how-to/skills/video-moodboard) · [video-sound](https://varg.ai/how-to/skills/video-sound) · [video-script](https://varg.ai/how-to/skills/video-script) · [character-passport](https://varg.ai/how-to/skills/character-passport) · [code-to-video-previz](https://varg.ai/how-to/skills/code-to-video-previz) · [video-animate](https://varg.ai/how-to/skills/video-animate) · [edit-footage-with-code](https://varg.ai/how-to/skills/edit-footage-with-code) · [media-judge](https://varg.ai/how-to/skills/media-judge) · [video-project-github](https://varg.ai/how-to/skills/video-project-github)
