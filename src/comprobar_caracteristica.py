from quien_es_quien.personajes.personajes import caracteristicas 
def caracteristica_valida(atributo):
    if atributo in caracteristicas:
        return True
    else:
        return False

    # return "correcto" if rx.cond(personajes['anita'].__contains__(atributo)) else "caracteristica incorrecta, introduzca otra"

