import reflex as rx
import quien_es_quien.estado as est

def pregunta():
    return rx.hstack(rx.text("Tu personaje tiene:"), rx.input(placeholder="Caracteristica"), rx.text(est.caracteristicas.caracteristica),  direction="row",)

def juego():
    return rx.center(pregunta(), )