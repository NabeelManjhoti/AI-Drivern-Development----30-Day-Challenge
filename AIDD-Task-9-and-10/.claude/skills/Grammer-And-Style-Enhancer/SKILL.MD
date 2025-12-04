# Skill: Grammar and Style Enhancer

## Description
Improves the grammar, flow, and style of a given text passage.

## Inputs
- `text`: The text to be improved.
- `style_guide`: (Optional) Specific style instructions (e.g., "Hemingway-esque", "Flowery", "Formal").
- `focus`: (Optional) What to focus on (e.g., "Clarity", "Show, don't tell", "Pacing").

## Prompt Template
```markdown
You are a professional editor. Improve the following text.

**Text:**
{{text}}

**Style Guide:**
{{style_guide|default("Standard literary style")}}

**Focus Area:**
{{focus|default("General improvement")}}

**Task:**
Rewrite the text to improve grammar, flow, and impact.
1.  **Polished Version:** The rewritten text.
2.  **Changes Made:** A brief explanation of key changes (e.g., "Removed passive voice", "Enhanced sensory details").
```
