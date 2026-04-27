---
name: discord-effect-converter
description: Instructions for converting legacy Discord animations into the modern modular format in src/animation/effects. Make sure to use this skill whenever you are asked to "update scripts in the new-submissions folder" or convert any Discord animation scripts.
compatibility: Foundry VTT V11+
---

# Discord Animation to Modular Format Conversion

When asked to update scripts in the `new-submissions` folder or to convert Discord animations to the modular format, execute the following transformations. You MUST reference the template files in the `references/` directory to understand the exact target structure:
- For standard or token animations, read `references/template_token.js`
- For active effects, read `references/template_active_effect.js`

## Code Style

*   **Apply Style Guide:** Ensure that all generated or updated code adheres strictly to the project's coding conventions. You MUST refer to the `style-guide` skill (located in `.agent/skills/style-guide/SKILL.md`) and apply its rules (e.g., 4-space indentation, semicolons, single quotes, 1TBS brace style, single-line if-statements) to the resulting module file.

## General Transformations

*   **Modular Structure:** Encapsulate the animation logic within an `export async function create(source, target(s) (optional), config)` function. This function MUST return a `Sequence` object. Replace any global `token` and `target` variables with the `source` and `target` arguments passed to the functions.
*   **Play Function:** Export an `async function play(source, target(s) (optional), config)` function that executes the sequence created by the `create` function.
*   **Stop Function:** Export an `async function stop(source, { id = 'effectId' } = {})` function to support stopping persistent effects.
*   **Parameter Handling:**
    *   Pass the casting token as `source`.
    *   Pass target tokens as an array `targetTokens` or as a singular `target`.
    *   Manage animation-specific configurations via a `config` object (passed as the last argument) to support default values and user overrides.
*   **File Relocation:** Move the newly converted file from its input folder (e.g., `new-submissions`) to `src/animation/effects/`.
*   **Module Integration:** Update `src/animation/effects/_effects.js` to import and export the new modular animation.
*   **Variable Renaming:** Rename global variables like `targets` to `targetTokens` to fit the modular function signature.
*   **Image Path Conversion:** Convert any `.file("path/to/image.webp")` calls to `.file(img("path/to/image.webp"))`. Make sure to import `img` from `../../lib/filemanager.js` (adjusting the relative path as necessary).
*   **Effect Comments:** Add descriptive comments explaining the visual or functional purpose of each effect or sequence chunk.
*   **Helper Functions:** Extract complex sequences of effects into smaller, logically grouped helper functions (e.g., `_castSpellEffects(sequence, token)`).

## API Updates

Ensure the script uses the latest Foundry VTT API patterns:

*   Replace `target.data.name` with `target.name`.
*   Replace `target.document.data.width` with `target.document.width`.
*   Replace `warpgate.crosshairs.show` with `Sequencer.Crosshair.show`.
*   Change the `t` property in the crosshairs configuration from `'line'` to `'ray'` for valid measured template types.
*   Replace deprecated `.from()` methods with `.copySprite()`.

## Bug Fixes

*   Add a validation check to ensure `canvas.scene.background.src` exists before creating effects that rely on it, preventing errors on scenes without background images.

## Attribution

*   **Original Author:** Include a comment at the top of the file crediting the original author of the animation.
*   **Updater:** Add a comment at the top of the file crediting `bakanabaka` as the author of the modular conversion.
