---
name: Git Autosync
trigger: always_on
description: Enforce regular git synchronization (commit and push) using the dedicated git_sync skill to ensure changes are persistently backed up.
---

# Git Autosync Rule

To maintain workspace consistency and ensure changes are persistently backed up, all agents MUST follow these synchronization guidelines.

## When to Sync

Git sync MUST be triggered under the following conditions — **only when there are uncommitted file changes**:

1. **Time-Based**: If 10 or more minutes have elapsed since the last uncommitted change was made, a sync MUST be performed.
2. **Task-Based**: After completing any significant sub-task that involved creating, editing, or deleting files.
3. **Session-End**: Before concluding a session or handing off to the user.

> [!IMPORTANT]
> Do **NOT** run git sync if there are no uncommitted local changes. Running `git status` first to confirm changes exist is REQUIRED before invoking the sync skill.

## How to Check

Before triggering a sync, evaluate:
- Have any files been created, modified, or deleted during this session?
- Has it been 10+ minutes since those changes were last committed?

If **both** answers are yes → **sync immediately**.
If files were changed but under 10 minutes → sync after the current sub-task completes.
If **no files were changed** → do **not** sync.

## Synchronization Guidelines

1. **Mandatory Syncing**: Agents MUST perform routine `git commit` and `git push` operations to ensure work is saved, conditioned on uncommitted changes existing.
2. **Parallel Preference**: If the operation *can* be done in parallel without blocking the main workflow (e.g., using the `git_sync` skill as a background process), it is highly recommended.
3. **Blocking Allowed**: If background synchronization is not feasible or fails, agents MUST proceed with a standard blocking commit and push. Maintaining a save-point takes precedence over workflow speed.

## Commit Standards

- **Frequency**: Every 10 minutes of active changes, or after completing a significant sub-task — whichever comes first.
- **Messages**: Use concise, meaningful commit messages generated from the current task summary.
- **Reliability**: Ensure the sync operation completes successfully before moving to the next major task phase if a background sync was not used.
- **No Empty Commits**: Never commit or push when the working tree is clean.

## Conflict Resolution

- In case of push conflicts, the sync agent (or manual git commands) should attempt a `git pull --rebase`.
- If manual intervention is required, the user must be notified immediately.
