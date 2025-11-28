# SpecKit Plus: Specification-Driven Development

SpecKit Plus is a structured methodology used in the AI-Native Era to maximize developer productivity. It shifts the primary focus from writing code syntax to crafting detailed, unambiguous natural language specifications.

The core principle is simple: **"Specs are the new syntax."**

Developers define clear requirements, and AI agents handle the complex task of generating, testing, and documenting the corresponding software implementation. This process transforms the specification into a "living contract" between the human developer and the AI collaborator, significantly accelerating the development workflow.

## 5 Core Concepts of SpecKit Plus

SpecKit Plus is organized around five key stages that ensure clarity, consistency, and successful execution by AI agents:

### 1. /constitution (Vision & Rules)

This foundational stage defines the high-level, non-negotiable aspects of the project. It covers the overall technical vision, security requirements, governance rules, and the general architecture that all subsequent AI work must follow. It is the initial "constitution" of the software system.

### 2. /specify (Detailed Requirements)

This is the critical step of writing the detailed, precise features, user stories, and acceptance criteria in the `SPEC.md` file. This specification must be clear enough for an AI agent to execute without ambiguity, effectively replacing traditional implementation code.

### 3. /plan (Strategy & Design)

In this phase, the requirements defined in `/specify` are analyzed and broken down into a strategic design. This involves mapping out the major software components, data flow, and overall architecture needed to fulfill the requirements, setting the stage for task execution.

### 4. /tasks (Actionable Work Units)

The high-level plan is broken down into small, highly specific work units. These tasks are then assigned to specialized AI agents (e.g., a "Database Agent" for schema work or a "Frontend Agent" for UI components) to ensure focused, parallel, and efficient implementation.

### 5. /implement (Code Generation & Testing)

The final stage where the specialized AI agents write the actual code and related artifacts. Crucially, tests and documentation are automatically generated based on the acceptance criteria in the original specification, ensuring the resulting product is validated and synchronized with the spec.