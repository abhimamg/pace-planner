---
name: Portable Rule Example
description: Demonstrates the use of repo-root resolution for portability.
---

# Portable Rule Example

This rule demonstrates how to reference resources relative to the repository root.

- **Glob**: `**/*.ts`
- **Context**: Refer to the project's standard documentation at `@/docs/coding_standards.md` to ensure consistency.

> [!TIP]
> Always use the `@/` prefix for inter-directory file references within the `.agent` folder to ensure the configuration remains portable across different environments.
