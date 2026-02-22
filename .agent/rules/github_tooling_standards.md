---
trigger: model_decision
description: Prioritize GitHub MCP server for repository operations, with gh CLI as a fallback.
---

# GitHub Tooling Standards

This rule defines the tool selection policy for GitHub-related operations (issues, PRs, repository metadata) in the `pace-planner` workspace.

## Tool Prioritization

1.  **Primary: GitHub MCP Server (`github-mcp-server`)**
    *   **Always** attempt to use `github-mcp-server` tools first for issue management, PR handling, and repository data.
    *   Use this for: `list_issues`, `create_issue`, `get_pull_request`, etc.
    *   **Context**: Use owner `abhimamg` and repository `pace-planner`.

2.  **Fallback: GitHub CLI (`gh`)**
    *   Use the `gh` CLI via `run_command` **only if**:
        *   The required capability is missing from the MCP server.
        *   An MCP tool call fails due to service issues or specific limitations.
        *   Bulk data or formatting is better handled by CLI outputs (e.g., `gh label list`).

## Project Context
*   **PACE Project Manager**: When managing issues, always consider their placement within the "PACE Project Manager" project.
*   Mention project links or context in descriptions to maintain consistency with the workspace organization.