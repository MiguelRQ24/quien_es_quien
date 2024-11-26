import reflex as rx
import quien_es_quien.estado as est
from reflex_dynoselect import dynoselect
options = [
    {"value": "pelo marron", "label": "pelo marron", "keywords": ["pelo marron", "marron"]},
    {"value": "pelo rubio", "label": "pelo rubio", "keywords": ["pelo rubio", "rubio"]},
]

def pregunta():
    return rx.hstack(rx.text("Tu personaje tiene:"),
                    rx.input(placeholder="Caracteristica", on_change=est.caracteristicas.set_caracteristica),
                    rx.button("Enviar", on_click=est.caracteristicas.tiene_caracteristica), 
                    rx.text(est.caracteristicas.caracteristica), 
                    direction="row",)

def juego():
    return rx.center(pregunta(), )