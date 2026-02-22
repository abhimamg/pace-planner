---
description: Trigger a regular git synchronization (commit and push) using the parallel Git Sync Agent.
---

# Git Sync Workflow

Use this workflow to manually synchronize your changes or to ensure the parallel agent is working correctly.

1.  **Run Sync Agent**
    // turbo
    `uv run .agent/skills/git_sync/sync.py --message "Manual sync: $[current_task_summary or 'Progress update']"`

2.  **Verify Status**
    `git status`

3.  **Check Remote**
    `git log -n 5`
