<!--
    Sync Impact Report:
    - Version change: 0.0.0 -> 1.0.0
    - List of modified principles:
        - [PRINCIPLE_1_NAME] -> I. Minimalism and Focus
        - [PRINCIPLE_2_NAME] -> II. Clear API
        - [PRINCIPLE_3_NAME] -> III. Test-Driven Development
        - [PRINCIPLE_4_NAME] -> IV. No External Dependencies
        - [PRINCIPLE_5_NAME] -> V. Stateless Operations
    - Added sections: None
    - Removed sections: [PRINCIPLE_6_NAME], [SECTION_2_NAME], [SECTION_3_NAME]
    - Templates requiring updates:
        - ✅ .specify/templates/plan-template.md
        - ✅ .specify/templates/spec-template.md
        - ✅ .specify/templates/tasks-template.md
    - Follow-up TODOs: None
-->
# Simple Calculator Constitution

## Core Principles

### I. Minimalism and Focus
The project is strictly limited to basic arithmetic operations: addition, subtraction, multiplication, and division. No other features, such as scientific calculations, history, or memory functions, will be included.

### II. Clear API
All calculator functionality must be exposed through a simple, well-documented, and predictable API. Functions should be pure and have no side effects.

### III. Test-Driven Development
Every operation and function must be developed using a strict Test-Driven Development (TDD) approach. Comprehensive unit tests are required to ensure correctness for all edge cases.

### IV. No External Dependencies
The core calculation logic must be implemented using only the standard language libraries. No third-party packages or frameworks are allowed for the core functionality to maintain simplicity and avoid bloat.

### V. Stateless Operations
The calculator must be stateless. Each calculation is an independent, atomic transaction that takes inputs and produces an output without relying on or storing any previous state.

## Governance
This Constitution is the single source of truth for project scope and engineering standards. All development work, pull requests, and reviews must adhere to these principles. Amendments require a documented proposal and team consensus.

**Version**: 1.0.0 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-03
