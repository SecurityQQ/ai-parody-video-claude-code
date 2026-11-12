# Keeping an AI video project in GitHub: text in git, media in Releases (step 10 of 10)

A video project is mostly large files that git handles badly, plus prompts and code that git handles well. The last step puts the text in git, lists every media file by hash, stores the bytes in Releases, and proves that a fresh copy restores.

## What the agent did

- Kept the working project in a private repo with the skill's `repo.py`, saving a version after each finished piece of work.
- Listed 408 media files (213 MB) by hash in a lock file and stored them in the private repo's Releases, never in git.
- Ran the proof: a fresh copy from GitHub, restored, compared with the working folder. All 149 text files and all 408 media files matched byte for byte.
- Ran the safety check before every save: no keys, no media in git.
- Made this public repo as a cleaned copy: other people's media (the reference clip, museum scans), the judges' scratch files and anything that names the machine it was made on are left out.
- Put the media needed for a rebuild into one file, `media.zip`, on the `media-v1` release of this repo.

Why private first: a video project holds licensed photos, paid generations and work nobody has approved yet. Publish a copy when it is ready, not the working folder.

## The skill

[`video-project-github`](https://varg.ai/how-to/skills/video-project-github) on varg how to. Install it in Claude Code, Codex, Grok, Cursor or Gemini CLI:

```bash
npx skills add vargHQ/skills --skill video-project-github
```

This film is a parody made by an AI agent; nobody shown said any of its lines. [Watch it](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_12b7a91f86db.mp4) · [the whole project](../README.md)

Previous: [9. AI judge](../review/README.md) · [All ten steps](../README.md#the-10-steps)
