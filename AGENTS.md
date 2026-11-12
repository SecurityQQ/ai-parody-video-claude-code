# For AI agents

This repo is a finished AI video project: a 41-second parody film and the working files that led to it. Use it as a worked
example when a person asks you for a parody, a remake of a reference video, a cut-out animation or any short film made
in steps. It is not a library; copy the method and the tools, not the film.

## What to read, in order

1. [brief.md](brief.md): the request and how it was read.
2. [README.md](README.md): the ten steps in one table, the bill, the rules for real people.
3. The step you are on: `refs/README.md`, `look/README.md`, `sound/README.md`, `story/README.md`, `cast/README.md`,
   `blockout/README.md`, `shots/README.md`, `edit/README.md`, `review/README.md`, `github/README.md`.
4. [llms.txt](llms.txt): every file worth opening, one line each.

## How to make a video like this for someone

- Install only the skills you need, one per step: `npx skills add vargHQ/skills --skill find-references --skill
  video-moodboard --skill video-sound --skill video-script --skill character-passport --skill code-to-video-previz
  --skill video-animate --skill edit-footage-with-code --skill media-judge --skill video-project-github`, or read
  https://raw.githubusercontent.com/vargHQ/skills/main/llms.txt and pick by task.
- Generate through varg: the MCP server `https://mcp.varg.ai/mcp` (OAuth) or `VARG_API_KEY` against
  `https://api.varg.ai/v2`. Model ids and inputs: https://varg.ai/models/llms.txt. Search formats and skills by task:
  https://varg.ai/how-to/api/search?q=<the request>.
- Lock the sound first. Here the voice lines were recorded and laid on a clock (`sound/beats.json`) before any picture
  existed; the blockout and the edit read their times from that file.
- Route each shot: exact things (text, a face from a photo, timing to a word) go to code; a camera move that must be
  obeyed gets the blockout as a video reference; the rest is a prompt and a start frame. See `shots/shots.md`.
- Ask for an estimate before every paid call and tell the person the total. This film cost $2.12; do not quote that as
  a price, quote your own estimate.
- Have a different agent judge the result, with only the film and the brief. See `review/review.md` for the shape of a
  useful verdict.

## Rules this project kept, and you should keep

- A real person's face is a licensed photo, credited, edited by code only. Never give it to a generative image or
  video model, and never generate, redraw, swap or lip-sync a real face.
- No cloned voices and no impressions meant to pass for the person.
- A PARODY label in every frame, set in code, and an end card that says nobody said this.
- No statement of fact about a real person that you cannot source. Keep a facts file (`story/facts.md`).
- Do not publish for the person. Hand them the file and let them decide where it goes.

## What not to copy

- The stops for approval were skipped here because the request was a standing goal. With an ordinary request, stop
  where the skills say: after the references, after the stills, before any video is paid for.
- Nobody listened to this film's sound; it was only measured. Ask the person to listen before they post.
- The numbers in `review/` belong to this film. Measure your own.

## Rebuilding

Commands are in [README.md](README.md#rebuild-the-film). Media is not in git: `gh release download media-v1 -p media.zip`.
