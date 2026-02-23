---
name: Git Sync Agent
description: A specialized skill for performing git synchronization (commit and push) to ensure workspace persistence.
---

# Git Sync Agent

This skill handles the overhead of version control by automating the "save points" of your development process.

## Capabilities

*   **Synchronization**: Runs `git add`, `git commit`, and `git push` to save changes.
*   **Parallel Support**: Can run as a background process to avoid blocking the main workflow.
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
