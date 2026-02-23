---
name: Antigravity Workspace Advisor
description: Advises on how to best organize an Antigravity workspace, including how to properly structure skills, rules, and workflows. Assesses and resolves alignment issues or redundant/overlapping files.
---

# Antigravity Workspace Advisor

This skill provides guidelines and best practices for organizing an Antigravity workspace, based on the official documentation.

## Directory Structure
All workspace-specific configurations should reside within the root configuration folder.

### Supported Folder Names
*   **`.agent/`** (Primary): The documented standard for workspace configurations.

### 1. Rules (`.agent/rules/`)
*   **Purpose**: Rules are Markdown files (`.md`) that provide persistent, reusable context.
*   **Global Rules**: Found in `~/.gemini/GEMINI.md`.
*   **Activation Modes**:
    *   *Manual*: Activated via `@mention` in the chat.
    *   *Always On*: Persistently applied to all interactions.
    *   *Model Decision*: The agent applies the rule based on its natural language description. Recommended for task-specific context to avoid prompt bloat.
    *   *Glob*: Automatically applied to files matching a pattern (e.g., `src/**/*.ts`).
*   **Limits**: Each rule file is capped at **12,000 characters**.
*   **@ Mention Resolution**:
    *   `@filename` references resolve relative to the rule file.
    *   `@/path/to/file` resolves relative to the **repository root** (ensuring portability).
    *   If not found, resolution falls back to repository-relative paths.

### 2. Skills (`.agent/skills/`)
*   **Purpose**: Specialized capabilities discovered during the "Discovery" and "Decision" phases.
*   **Structure**: Each skill MUST reside in its own subdirectory (e.g., `skills/<skill-name>/`).
    *   **Standard Subfolders**: `scripts/` (for helpers), `examples/` (for reference), `resources/` (for assets).
*   **Required Files**: Mandatory `SKILL.md` with YAML frontmatter.
    *   **`description`**: Required. Use third-person, keyword-rich summaries to help discovery.
*   **Best Practices**:
    *   **Progressive Disclosure**: Follow the "Discovery (description) -> Activation (reading SKILL.md) -> Execution" pattern.
    *   **Stay Focused**: Each skill should do *one thing well*.
    *   **Scripts as Black Boxes**: Use `--help` to understand scripts instead of reading source code.

### 3. Workflows (`.agent/workflows/`)
*   **Purpose**: Step-by-step guides for complex tasks.
*   **Invocation**: Use slash commands (e.g., `/workflow-name`).
*   **Features**:
    *   **Nesting**: Workflows can call other workflows via slash commands.
    *   **Auto-run**: Use `// turbo` (single step) or `// turbo-all` (file-wide) for terminal commands.
    *   **Agent-Generated**: The agent can generate new workflow files based on conversation history.

## Maximizing Antigravity Features
*   **Rules vs. Skills vs. Workflows**:
    *   Use **Rules** for persistent style and project constraints (e.g., "Avoid plain red, blue, green").
    *   Use **Skills** for complex logic, multi-file edits, or specialized tools.
    *   Use **Workflows** for repeatable, multi-step processes or release cycles.
*   **Context Management**: Prefer "Model Decision" for rules to keep the prompt concise.

## Customizing Agents for Maximum Productivity
*   **Hybrid Implementation**: Combine **Global Rules** for personal preferences with **Workspace Rules** for project-specific needs.
*   **Agent Modes**: Switch between **Pro** for deep reasoning and **Flash** for rapid iteration where appropriate.
*   **Automation**: Use agent-generated workflows to codify repetitive manual tasks into single slash commands.

## Alignment & Redundancy Checks
As the Workspace Advisor, you should:
1.  **Clarify Requests**: If a request is unclear, always ask for clarification. **Never make assumptions** about the user's intent or workspace state.
2.  **Check for Overlaps**: Delineate boundaries between similar skills or rules. Ensure each has a **clear and distinct scope**.
3.  **Validate Structure**: Ensure correct folder structure and YAML frontmatter.
4.  **Optimize Context**: Suggest removing bloated rules or converting large scripts into "Black Box" skills. Prefer `Model Decision` or `Glob` for rule activation.
5.  **Audit for Clarity**: Identify vague descriptions or instructions and **suggest specific modifications**.
6.  **Validate Repository Portability**: Flag any hardcoded absolute paths in rules or skills and recommend switching to the `@/` repo-root syntax.
7.  **Consult Documentation**: For latest updates, visit the [Antigravity Docs](https://antigravity.google/docs).
