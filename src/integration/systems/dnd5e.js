function getSpellLevel({aaHandler}) {
    if (aaHandler) { return aaHandler.systemData?.spellLevel; }
    return undefined;
}

export const dnd5e = {
    getSpellLevel,
}