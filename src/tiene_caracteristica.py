import reflex as rx
import quien_es_quien.personajes.personajes as pjs
def tiene_caracteristica(caracteristica, personaje):
    rx.cond(caracteristica in pjs.personajes[personaje], 'la tiene', 'no la tiene')
