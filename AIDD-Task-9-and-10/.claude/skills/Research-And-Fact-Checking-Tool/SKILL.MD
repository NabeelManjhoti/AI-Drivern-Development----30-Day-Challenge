# Skill: Research and Fact-Checking Tool

## Description
Verifies facts and provides research assistance for specific topics within the book.

## Inputs
- `topic`: The specific topic or claim to research.
- `context`: (Optional) The context in which this fact appears in the story (e.g., historical setting, scientific concept).

## Prompt Template
```markdown
You are a research assistant for a writer. Verify the following information or provide research on the topic.

**Topic/Claim:**
{{topic}}

**Context:**
{{context|default("General research")}}

**Task:**
1.  **Verification:** Is this information accurate? If not, correct it.
2.  **Details:** Provide relevant details that would add authenticity to the story.
3.  **Sources:** (Optional) Mention where this information generally comes from (e.g., "According to historical records...").
4.  **Creative Integration:** Suggest how to weave this fact naturally into the narrative.
```
