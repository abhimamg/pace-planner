---
name: Git Sync Agent
description: A specialized skill for performing background git synchronization (commit and push) to avoid blocking main agent workflows.
---

# Git Sync Agent

This skill is designed to run as a parallel agent to handle the overhead of version control. It automates the "save points" of your development process.

## Capabilities

*   **Background Sync**: Runs `git add`, `git commit`, and `git push` without blocking the main agent.
*   **Intelligent Commits**: Generates commit messages based on the current context or provided summaries.
*   **Conflict Handling**: Automatically rebases on pull conflicts unless manual intervention is necessary.

## Usage

Agents can trigger this skill using:
`uv run .agent/skills/git_sync/sync.py --message "Task: Refactoring auth"`

### Options:
*   `--message, -m`: Custom commit message.
*   `--dry-run`: Show commands without executing them.
*   `--force-push`: Use with caution.
*   `--pull`: Perform a pull before pushing.

## Best Practices

*   Invoke this skill after significant file edits.
*   Do not wait for this skill to complete unless you are finishing your session.
*   The script should be run using `uv run` to ensure dependency isolation.
