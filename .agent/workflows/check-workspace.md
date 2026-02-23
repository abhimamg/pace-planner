---
description: Comprehensive check to ensure the workspace configuration follows Antigravity standards.
---

# Workspace Configuration Check

This workflow validates the `.agent/` directory structure, rules, skills, and hardcoded path configurations.

1.  **Identify Configuration Root**: List the repository root to ensure the `.agent/` directory exists and no unauthorized variants (like `_agent/`) are present.
2.  **Validate Directory Structure**: Verify the existence and contents of:
    - `.agent/rules/`
    - `.agent/skills/`
    - `.agent/workflows/`
3.  **Audit Skills**:
    - Ensure every skill is in its own subdirectory.
    - Check for the mandatory `SKILL.md` with proper YAML frontmatter.
    - Verify that skills follow the "One Thing Well" principle.
4.  **Audit Rules**:
    - Verify that rules are within the 12,000-character limit.
    - Check for appropriate activation modes (prefer "Model Decision" or "Glob").
5.  **Scan for Hardcoded Paths**:
    // turbo
    - Run `grep -ri "Users/" .agent` to identify absolute paths that may break portability.
6.  **Analyze Scope and Clarity**:
    - **Skills**: Check that each skill's `description` and `Persona` clearly define its boundaries. If a skill is "doing too many things," suggest splitting it.
    - **Rules**: Ensure rules have clear triggers (e.g., `model_decision` or `glob`) and concise descriptions.
    - **Clarity Audit**: Identify any vague instructions or overlapping responsibilities between configuration entities.
7.  **Suggest Modifications**: For every identified issue (scope creep, vague descriptions, hardcoded paths), provide specific, actionable suggestions for improvement.
8.  **Generate Report**: Summarize findings and provide an implementation plan for any identified issues.
