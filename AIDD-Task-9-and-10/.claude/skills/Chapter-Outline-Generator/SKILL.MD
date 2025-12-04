# Skill: Chapter Outline Generator

## Description
Generates a detailed chapter outline based on the book title, genre, and key events.

## Inputs
- `title`: The title of the book.
- `genre`: The genre of the book (e.g., Fantasy, Sci-Fi, Mystery).
- `key_events`: A list or description of key events that should happen in the chapter.
- `chapter_number`: (Optional) The specific chapter number to outline.

## Prompt Template
```markdown
You are an expert book outliner. Create a detailed outline for a chapter in a book.

**Book Details:**
- **Title:** {{title}}
- **Genre:** {{genre}}

**Context/Key Events:**
{{key_events}}

**Task:**
Generate a structured outline for {{chapter_number|default("the next chapter")}}. Include:
1.  **Scene Breakdown:** A list of scenes with a brief description of what happens.
2.  **Character Focus:** Which characters are central to this chapter and their emotional state.
3.  **Pacing:** Suggestions for the pacing of the chapter (fast-paced action, slow introspection, etc.).
4.  **Ending Hook:** A suggestion for how to end the chapter to keep the reader engaged.
```
