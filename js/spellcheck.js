// Diccionario para corrección ortográfica
const spellcheckDict = {
    'asensor': 'ascensor',
    'ascensor': 'ascensor',
    'asensores': 'ascensores',
    'ascensores': 'ascensores',
    'elevdor': 'elevador',
    'electrica': 'eléctrica',
    'escalera electrica': 'escalera eléctrica',
    'escalera mecanica': 'escalera mecánica',
    'mecancia': 'mecánica',
    'mantenimieto': 'mantenimiento',
    'manteminiento': 'mantenimiento',
    'mantención': 'mantenimiento',
    'reparacion': 'reparación',
    'modernisacion': 'modernización',
    'modernisación': 'modernización',
    'cotisacion': 'cotización',
    'cotisasión': 'cotización',
    'presupesto': 'presupuesto',
    'puedeshacerme': 'puedes hacerme',
    'nesesito': 'necesito',
    'necesitoun': 'necesito un',
    'economico': 'económico',
    'economica': 'económica',
    'barata': 'económica',
    'colejio': 'colegio',
    'colejgio': 'colegio',
    'montauto': 'monta auto',
    'montaauto': 'monta auto',
    'montacarga': 'monta cargas',
    'hidraulico': 'hidráulico',
    'hidraúlico': 'hidráulico',
    'platafoma': 'plataforma',
    'discapacitado': 'discapacitados',
    'salvaescalera': 'salvaescaleras',
    'informe': 'información',
    'porfa': 'por favor',
    'info': 'información',
    'ascnesor': 'ascensor',
    'sala de maquinas': 'cuarto de máquinas',
    'sin sala de maquinas': 'sin cuarto de máquinas',
    'gearles': 'gearless',
    'montanary': 'Montanari',
    'fermator': 'Fermator'
};

function correctSpelling(text) {
    let corrected = text.toLowerCase();
    for (const [wrong, right] of Object.entries(spellcheckDict)) {
        corrected = corrected.replace(new RegExp(`\\b${wrong}\\b`, 'gi'), right);
    }
    // Correcciones adicionales para frases comunes
    corrected = corrected.replace(/puedeshacerme/gi, 'puedes hacerme');
    corrected = corrected.replace(/necesitoun/gi, 'necesito un');
    corrected = corrected.replace(/sin sala de maquinas/gi, 'sin cuarto de máquinas');
    corrected = corrected.replace(/con sala de maquinas/gi, 'con cuarto de máquinas');
    return corrected;
}