import { dnd5e } from "./systems/dnd5e.js";

function getSpellLevel(config) {
    switch (game?.system?.id) {
        case 'dnd5e': return dnd5e.getSpellLevel(config);
        default: return undefined;
    }
}

export const system = {
    getSpellLevel
};