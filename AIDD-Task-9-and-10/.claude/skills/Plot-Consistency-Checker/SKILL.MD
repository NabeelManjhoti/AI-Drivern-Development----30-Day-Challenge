# Skill: Plot Consistency Checker

## Description
Analyzes plot points or a summary to identify inconsistencies, plot holes, and timeline errors.

## Inputs
- `plot_summary`: A summary of the plot or a list of plot points to check.
- `context`: (Optional) Any established world-building rules or character backstories relevant to the check.

## Prompt Template
```markdown
You are a meticulous editor and continuity expert. Analyze the following plot details for consistency.

**Plot Summary/Points:**
{{plot_summary}}

**Established Context:**
{{context|default("None provided")}}

**Task:**
Identify any potential plot holes, logical inconsistencies, or timeline errors. For each issue found:
1.  **Description:** Clearly explain the inconsistency.
2.  **Impact:** How does this affect the story or reader immersion?
3.  **Suggestion:** Propose a way to fix or explain the inconsistency.

If no issues are found, confirm that the plot appears consistent.
```
