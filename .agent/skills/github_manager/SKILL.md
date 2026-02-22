---
name: GitHub Manager
description: Manage issues and projects on GitHub for the pace-planner repository.
---

# GitHub Manager

This skill provides capabilities to manage issues and projects on GitHub, specifically tailored for the `abhimamg/pace-planner` repository and the "PACE Project Manager" project.

## Core Capabilities

### 1. Issue Management
Create and track work items within the repository:
- `create_issue`: Create new issues in `abhimamg/pace-planner`.
- `update_issue`: Modify existing issues (state, assignees, labels).
- `list_issues`: List and filter issues in the repository.
- `add_issue_comment`: Add feedback or updates to specific issues.

### 2. Pull Request Management
Manage the code review and integration process:
- `create_pull_request`: Open new PRs for feature branches.
- `get_pull_request`: Review PR details and status.
- `list_pull_requests`: Track open PRs in the repository.
- `merge_pull_request`: Finalize and merge approved changes.

### 3. Repository Search & Exploration
Search and retrieve technical context:
- `search_code`: Find code patterns or implementations across repositories.
- `get_file_contents`: Retrieve contents of specific files from GitHub.

## Project Context: PACE Project Manager
All issues and pull requests should be considered within the context of the **"PACE Project Manager"** project. When creating issues, ensure they align with the project's milestones and goals.

## Best Practices
- **Explicit Context**: Always specify the owner (`abhimamg`) and repo (`pace-planner`) for repository-specific tools.
- **Reference Project**: Mention "PACE Project Manager" in issue descriptions when relevant for consistency.
- **Verification**: Use `get_issue` or `get_pull_request` to verify the state of items before making updates.
