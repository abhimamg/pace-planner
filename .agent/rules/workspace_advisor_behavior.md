---
trigger: model_decision
description: Guidelines for the agent to proactively maintain workspace health, organization, and alignment.
---

# Workspace Organization

All workspace-specific configurations, skills, rules, and workflows MUST reside within the `.agent/` root configuration folder.

## Standard Directory Structure
- `.agent/rules/`: Persistent rules and project constraints.
- `.agent/skills/`: Specialized capabilities and tool definitions.
- `.agent/workflows/`: Step-by-step automation and slash commands.

> [!IMPORTANT]
> Use `.agent/` as the primary directory for all Antigravity-related configurations to ensure consistent agent behavior and discovery.

> [!TIP]
> Use these checks during the "PLANNING" phase of any task involving workspace changes.

# Configuration Entity Standards

To maintain a clean and efficient workspace, follow these standards for all configuration entities.

## 1. Rules (`.agent/rules/*.md`)
- **Format**: Markdown files with YAML frontmatter (`name`, `description`).
- **Limit**: Strictly capped at **12,000 characters**.
- **Activation**: Prefer "Model Decision" or "Glob" patterns over "Always On" to prevent prompt bloat.

## 2. Skills (`.agent/skills/<skill-name>/`)
- **Structure**: Each skill must have its own subdirectory.
- **Requirement**: A mandatory `SKILL.md` file with YAML frontmatter.
- **Design**: Skills should follow the "Black Box" principle; use `--help` or clear descriptions rather than requiring the agent to read source code.

## 3. Workflows (`.agent/workflows/*.md`)
- **Format**: Markdown files defining step-by-step tasks.
- **Invocation**: Triggered via slash commands (e.g., `/my-workflow`).
- **Automation**: Use `// turbo` or `// turbo-all` for terminal commands to enable auto-execution.