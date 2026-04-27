---
name: skill-creation-improver
description: A skill used to prompt for and suggest robust improvements when creating or updating other agent skills. Make sure to use this skill whenever you are helping the user create a new skill or use the skill-creator, to ensure the new skill adheres to the highest standards of reliability.
---

# Skill Creation Improver

When you are asked to create a new skill, or when you are actively using the `skill-creator`, you should strongly recommend the following structural improvements to ensure the resulting skill is robust, testable, and reliable. 

If the user asks you to create a skill, proactively ask if they would like you to implement these best practices along with it.

## 1. Concrete Examples (Before & After)
Abstract instructions are often misinterpreted. Strongly suggest adding concrete examples. 
- If the skill modifies code or data, recommend adding a "Before" and "After" example to the `SKILL.md`.

## 2. Quantitative Evaluation Suites
All robust skills should be testable.
- Suggest creating an `evals/evals.json` file containing 2-3 realistic test prompts.
- This allows the `skill-creator` to run automated benchmarks to verify the skill's success rate and catch edge-cases.

## 3. Deterministic Helper Scripts
Don't make the LLM do things that code can do perfectly.
- If the skill involves repetitive formatting, API string replacements, or strict rule verification, suggest writing a small Python helper script in a `scripts/` directory (e.g., `scripts/lint.py` or `scripts/pre_convert.py`).
- Instruct the skill to run the helper script as part of its workflow.

## 4. Progressive Disclosure (Reference Files)
Don't overcrowd the main `SKILL.md` (keep it under 500 lines).
- If the skill requires large templates, long reference documents, or extensive code examples, suggest placing them in a `references/` directory (e.g., `references/template.js`).
- Update the main `SKILL.md` to explicitly instruct the agent to read those specific reference files when needed.

## 5. "Pushy" Descriptions
The `description` field in the YAML frontmatter is the primary trigger.
- Ensure the description explicitly states exactly *when* the agent should trigger it, using imperative language (e.g., *"Make sure to use this skill whenever..."*).
- Do not just describe what the skill does; describe the context in which it is useful.
