import reflex as rx
import quien_es_quien.estado as est
from quien_es_quien.personajes.personajes import personajes
def caracteristica_valida(atributo, personaje):
    if 'pelo rubio' in personajes[personaje]:
        return "esto va muy  correcto"
    # return "correcto" if rx.cond(personajes['anita'].__contains__(atributo)) else "caracteristica incorrecta, introduzca otra"

