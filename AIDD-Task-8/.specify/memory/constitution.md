# Simple Calculator Constitution

## Core Principles

### Modularity
Focus on clear, small, and reusable functions for each basic operation (add, subtract, multiply, divide). Each operation should be a self-contained unit.

### CLI-First
The calculator will primarily be a command-line interface application. Input will be via arguments, and output to stdout.

### Test-Driven Development (TDD)
All features and bug fixes must be accompanied by tests. The Red-Green-Refactor cycle is strictly enforced.

### Accuracy
Numerical precision for all calculations must be maintained. Edge cases like division by zero should be handled gracefully.

### Simplicity
Adhere to YAGNI (You Ain't Gonna Need It) principles. Only implement basic arithmetic operations (add, subtract, multiply, divide). Avoid unnecessary features.

### Maintainability
Code should be clean, readable, and well-documented to facilitate future updates and bug fixes.

## Scope and Constraints

**In Scope**: Addition, subtraction, multiplication, division of two numbers.
**Out of Scope**: Advanced mathematical functions, scientific notation, GUI, chained operations, order of operations (PEMDAS).
**Input**: Two numbers and a single operator.
**Output**: Result of the operation or an error message.

## Quality Assurance

**Code Review**: All changes must pass code review by at least one other developer.
**Testing**: Unit tests for each operation, integration tests for CLI interaction.
**Error Handling**: Clear error messages for invalid input or operations (e.g., division by zero).

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All Pull Requests and code reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-03