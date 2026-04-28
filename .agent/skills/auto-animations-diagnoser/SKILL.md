---
name: auto-animations-diagnoser
description: Determines whether an animation effect should be registered with the automated animations integration and provides instructions for doing so. Make sure to use this skill whenever you convert a new effect or create an animation effect from scratch.
---

# Automated Animations Diagnoser

Whenever you create or convert an animation effect, you must evaluate whether it qualifies to be registered with the `autoanimations` integration.

## Diagnostic Criteria

Effects should be registered for automated animations if they meet **ANY** of the following criteria:

1.  **On a single token:** The animation simply plays on or around the casting token (e.g., self-buffs, simple actions).
2.  **Active effect on a token:** The animation is persistent and tied to an active effect on a token (e.g., Banishment, ongoing damage).
3.  **Ranged/Melee attack:** The animation travels between two tokens (e.g., shooting an arrow, swinging a sword).
4.  **Template attack:** The attack uses a measured template (circle, cone, line, ray) or uses a position (like `Sequencer.Crosshair.show`) to place effects.

## Valid Triggers
When registering an effect, you must pass the correct category trigger string:
- `"token"` : Self targeting ability
- `"template"` : Template using ability or relies on a position/crosshair
- `"effect"` : Active effect applied
- `"melee-target"` : Source -> Target melee animation
- `"ranged-target"` : Source -> Target ranged animation

## Registration Implementation

If the effect meets any of the above criteria, you MUST register it at the bottom of the effect's module file.

1.  **Import the integration:**
    Add the following import at the top of the file (adjusting the relative path as necessary):
    ```javascript
    import { autoanimations } from '../../../integration/autoanimations.js';
    ```

2.  **Call the register method:**
    At the bottom of the file, after the exports, call the register method. Make sure to pass the `DEFAULT_CONFIG` object defined in your script.
    ```javascript
    autoanimations.register("Name of Effect", "trigger", "eskie.effect.effectName", DEFAULT_CONFIG, '0.1.0');
    ```
    *   `"Name of Effect"`: The human-readable name (e.g., `"Tasha's Caustic Brew"`).
    *   `"trigger"`: The correct trigger string from the Valid Triggers list (e.g., `"template"` or `"effect"`).
    *   `"eskie.effect.effectName"`: The path to the effect within the exported module structure.
    *   `DEFAULT_CONFIG`: The default configuration object for the effect.
    *   `'0.1.0'`: The initial version number.
