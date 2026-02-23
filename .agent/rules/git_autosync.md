---
name: Git Autosync
trigger: always_on
description: Enforce regular git synchronization (commit and push) using the dedicated git_sync skill to ensure changes are persistently backed up.
---

# Git Autosync Rule

Agents MUST keep the workspace backed up via routine `git commit` and `git push`. Follow these rules exactly.

## Trigger Conditions

Only sync when **uncommitted file changes exist**. Always run `git status` first to verify.

| Condition | Action |
|-----------|--------|
| Files changed AND 10+ minutes since last commit | **Sync immediately** |
| Files changed AND under 10 minutes | Sync after current sub-task completes |
| No files changed | **Do NOT sync** |

Sync is also required:
- After any significant sub-task that created, edited, or deleted files
- Before concluding a session or handing off to the user

## How to Sync

- **Preferred**: Run `git_sync` skill as a background process to avoid blocking work.
- **Fallback**: Use standard `git add && git commit && git push` if the skill is unavailable or fails.
- **On push conflict**: Run `git pull --rebase`, then retry. Notify the user if manual intervention is needed.

## Commit Standards

- **Messages**: Concise and descriptive, summarizing the current task.
- **No empty commits**: Never commit when the working tree is clean.
