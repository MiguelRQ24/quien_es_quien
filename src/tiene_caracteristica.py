def tiene_caracteristica(caracteristica, personaje):
    if caracteristica in personajes[personaje]:
        return 'la tiene'
    else:
        return 'no la tiene'
