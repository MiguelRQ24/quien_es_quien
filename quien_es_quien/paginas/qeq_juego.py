import reflex as rx
import quien_es_quien.estado as est
from reflex_dynoselect import dynoselect
caracteristicas = [
    {"value": "pelo marron", "label": "pelo marron"},
]

def pregunta():
    return rx.hstack(rx.text("Tu personaje tiene:"), dynoselect(caracteristicas, placeholder="Caracteristica", search_placeholder="Busca caracteristica"), direction="row",)

def juego():
    return rx.center(pregunta(), )