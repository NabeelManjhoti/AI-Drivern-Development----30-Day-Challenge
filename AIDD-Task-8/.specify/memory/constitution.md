<!--
Sync Impact Report:
Version change:  → 0.1.0
Modified principles:
  - PRINCIPLE_1_NAME → Basic Operations Only
  - PRINCIPLE_2_NAME → Clear Input/Output
  - PRINCIPLE_3_NAME → Accuracy and Precision
  - PRINCIPLE_4_NAME → Simplicity and Maintainability
  - PRINCIPLE_5_NAME → Test Coverage
Added sections: None
Removed sections:
  - [PRINCIPLE_6_NAME] and its description
  - [SECTION_2_NAME] and its content
  - [SECTION_3_NAME] and its content
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .gemini/commands/sp.adr.toml ⚠ pending
  - .gemini/commands/sp.analyze.toml ⚠ pending
  - .gemini/commands/sp.checklist.toml ⚠ pending
  - .gemini/commands/sp.clarify.toml ⚠ pending
  - .gemini/commands/sp.constitution.toml ⚠ pending
  - .gemini/commands/sp.git.commit_pr.toml ⚠ pending
  - .gemini/commands/sp.implement.toml ⚠ pending
  - .gemini/commands/sp.phr.toml ⚠ pending
  - .gemini/commands/sp.plan.toml ⚠ pending
  - .gemini/commands/sp.specify.toml ⚠ pending
  - .gemini/commands/sp.tasks.toml ⚠ pending
Follow-up TODOs: None
-->
# Simple Calculator Constitution

## Core Principles

### I. Basic Operations Only
The calculator must implement only basic arithmetic operations: addition, subtraction, multiplication, and division. No advanced functions (e.g., trigonometric, logarithmic, roots) are permitted.

### II. Clear Input/Output
The calculator must provide a clear and intuitive interface for inputting numbers and operations, and for displaying results. Error messages should be user-friendly and informative.

### III. Accuracy and Precision
Results must be accurate for standard arithmetic operations, handling floating-point numbers with reasonable precision. Division by zero must be explicitly handled and reported as an error.

### IV. Simplicity and Maintainability
Codebase should be kept minimal and easy to understand. Favor clear, straightforward implementations over complex optimizations.

### V. Test Coverage
All core arithmetic functions and edge cases (e.g., division by zero, invalid input) must have comprehensive unit tests.

## Governance

Amendments to this constitution require review and approval by the project lead. All changes must be documented, including the rationale for the change.

**Version**: 0.1.0 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-03