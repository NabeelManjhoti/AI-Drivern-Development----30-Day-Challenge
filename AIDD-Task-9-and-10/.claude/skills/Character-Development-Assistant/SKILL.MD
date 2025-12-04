# Skill: Character Development Assistant

## Description
Helps flesh out character details, including backstory, motivations, and personality traits.

## Inputs
- `name`: The name of the character.
- `role`: The character's role in the story (e.g., Protagonist, Antagonist, Mentor).
- `traits`: (Optional) A list of initial personality traits.
- `archetype`: (Optional) A character archetype to base the development on.

## Prompt Template
```markdown
You are a creative writing assistant specializing in character development. Help me flesh out a character.

**Basic Info:**
- **Name:** {{name}}
- **Role:** {{role}}
- **Traits:** {{traits|default("Not specified")}}
- **Archetype:** {{archetype|default("Not specified")}}

**Task:**
Create a detailed character profile including:
1.  **Backstory:** A compelling history that explains their current situation and motivations.
2.  **Personality:** detailed analysis of their strengths, weaknesses, and quirks.
3.  **Motivation:** What drives them? What is their ultimate goal?
4.  **Conflict:** Internal and external conflicts they face.
5.  **Voice:** Tips on how they speak and interact with others.
```
