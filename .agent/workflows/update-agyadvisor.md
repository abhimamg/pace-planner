---
description: How to update the Antigravity Workspace Advisor skill
---

# Updating Antigravity Workspace Advisor

Follow these steps to ensure the Workspace Advisor skill remains accurate and aligned with the latest official standards.

1.  **Research Documentation**: Use the `browser_subagent` to thoroughly explore `https://antigravity.google/docs`. Specifically, look for updates on:
    -   Skills (folder structure, YAML frontmatter, best practices).
    -   Rules (activation modes, glob patterns, `@mention` resolution).
    -   Workflows (slash commands, nesting, turbo annotations).
2.  **Review Current Implementation**: Examine the existing files in `.agent/skills/agyadvisor/` to identify outdated information or missing features.
3.  **Create Implementation Plan**: Draft a `implementation_plan.md` in the current brain directory detailing the specific updates required.
4.  **Execute Updates**: Apply the changes to `SKILL.md` and any associated example or resource files.
5.  **Verification**: 
    -   Cross-reference the changes with the research findings.
    -   Use the advisor skill on itself to ensure it correctly identifies the workspace structure.
6.  **Document Changes**: Create or update the `walkthrough.md` to show what was changed and how it adheres to the latest standards.
