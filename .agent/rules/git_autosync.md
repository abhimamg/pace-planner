---
name: Git Autosync
description: Enforce regular git synchronization (commit and push) using the dedicated git_sync skill to avoid blocking agentic workflow.
---

# Git Autosync Rule

To maintain workspace consistency and ensure changes are persistently backed up without bottlenecking primary agentic tasks, all agents MUST follow these synchronization guidelines.

## Background Synchronization

1.  **Offload Syncing**: agents should not spend primary context time on routine `git commit` and `git push` operations for every small change.
2.  **Use Dedicated Skill**: Use the `git_sync` skill to trigger background synchronization.
3.  **Parallel Execution**: When starting a large task, spin up the `git_sync` skill as a parallel process to handle intermittent commits.

## Commit Standards

*   **Frequency**: Sync every 5-10 minutes or after completing a significant sub-task (whichever comes first).
*   **Messages**: Use concise, meaningful commit messages generated from the current task summary.
*   **Non-Blocking**: Ensure the sync operation does not block the terminal or the main reasoning loop.

## Conflict Resolution

*   In case of push conflicts, the sync agent should attempt a `git pull --rebase`.
*   If manual intervention is required, the main agent must be notified immediately.
