---
name: module-to-macro
description: How to convert an effect in src/animation into a stand-alone macro to run inside of Foundry VTT. Make sure to use this skill whenever the user asks to convert an animation, create a standalone macro from an effect, or change a module animation to a macro, even if they don't explicitly say "module to macro".
---

# Module to Macro Conversion

When a user asks to convert an effect from the `src/animation/` directory into a stand-alone macro for Foundry VTT, follow these instructions to ensure the macro is self-contained, fully functional, and well-formatted.

## Core Conversion Steps

1. **Locate the Effect File**: Find the relevant animation script in `src/animation/effects/`.
2. **Handle Multiple Variants**: Check if the effect has multiple variants (e.g., `rage` has `_rage.js` which exports `v1`, `v2`, `v3`, etc.). 
   > **CRITICAL**: If the user specifies an effect with multiple variants (such as the Rage effect), **STOP** and ask the user to clarify which version they want output before proceeding. Do not guess or output all variants.
3. **Extract the Sequence**: Extract the core `new Sequence()` logic from the `create` or `play` functions of the effect.
4. **Remove Module Dependencies**: 
   - Remove any `import` statements (like `import { closest }` or `import { autoanimations }`).
   - Macros run directly in Foundry VTT and do not support ES module imports in the same way.
   - For `closest()`, remove the function call and just use the string (e.g., change `closest('jb2a.magic_missile')` to `'jb2a.magic_missile'`). Sequencer natively handles these strings when the JB2A module is installed.
5. **Set up Target/Source Variables**: 
   - In a module, `source`, `token`, or `target` are passed as arguments.
   - In a macro, you must define these at the top of the script using Foundry globals (e.g., `const token = canvas.tokens.controlled[0];` or `const target = game.user.targets.first();`).
   - Add safety checks to return early if the necessary tokens are not selected.
   - **Note**: Remember the project rule: *If adding or changing an if statement that immediately returns, it should be a single line. For example: `if (!token) return ui.notifications.warn("No token");`*
6. **Implement Toggle Functionality (Play/Stop)**:
   - The first time the macro is called, the effect should be played.
   - If the original effect includes a `stop()` function, or if it persists an effect on a token using `.persist()`, the macro should function as a toggle.
   - The second time the macro is called, the effect should be stopped using the logic from the `stop()` function (e.g. `Sequencer.EffectManager.endEffects({ name: label, object: token })`).
   - Use `Sequencer.EffectManager.getEffects({ name: label, object: token }).length > 0` to check if the effect is currently playing.
7. **Output the Macro**: Write the resulting JavaScript code into `src/standalone-macros/` following the naming convention of the existing files. For effects with multiple variants, the filename should   
    include the variant name (e.g. `rage-electric.js`, `rage-super-saiyan.js`, etc.).

## Concrete Example: Before & After

### Before: Module Effect (e.g., src/animation/effects/buff/example.js)
```javascript
import { closest } from "../../../../lib/filemanager.js";
import { autoanimations } from "../../../../integration/autoanimations.js";

const DEFAULT_CONFIG = { color: 'red' };

function create(token, config = {}) {
    const { color } = foundry.utils.mergeObject(DEFAULT_CONFIG, config);
    let seq = new Sequence()
        .effect()
        .name(`exampleBuff - ${token.id}`)
        .file(closest(`jb2a.impact.ground_crack.${color}.02`))
        .atLocation(token)
        .size(3.5, { gridUnits: true })
        .persist();
    return seq;
}

export const exampleBuff = { 
    create, 
    play: async (t, c) => (await create(t, c))?.play(),
    stop: async (t) => Sequencer.EffectManager.endEffects({ name: `exampleBuff - ${t.id}`, object: t })
};
```

### After: Standalone Macro
```javascript
// Standalone Macro
const token = canvas.tokens.controlled[0];
if (!token) return ui.notifications.warn("Please select a token!");

const color = 'red';
const label = `exampleBuff - ${token.id}`;

const isPlaying = Sequencer.EffectManager.getEffects({ name: label, object: token }).length > 0;

if (isPlaying) {
    Sequencer.EffectManager.endEffects({ name: label, object: token });
} else {
    new Sequence()
        .effect()
        .name(label)
        .file(`jb2a.impact.ground_crack.${color}.02`)
        .atLocation(token)
        .size(3.5, { gridUnits: true })
        .persist()
        .play();
}
```

## Evals

To ensure the reliability of this skill, test cases should be maintained in `evals/evals.json` covering various effect formats (e.g., simple template animations vs multi-target active effects).
