import reflex as rx
import quien_es_quien.estado as est
from quien_es_quien.personajes.personajes import caracteristicas 
def caracteristica_valida(atributo):
    if atributo in caracteristicas:
        return ""
    else:
        return "caracteristica incorrecta, introduzca otra"

    # return "correcto" if rx.cond(personajes['anita'].__contains__(atributo)) else "caracteristica incorrecta, introduzca otra"

