import reflex as rx
import quien_es_quien.estado as est

def pregunta():
    return rx.hstack(rx.text("Tu personaje tiene:"), 
                     rx.input(placeholder="Caracteristica", on_change=est.escoger.set_caracteristica), 
                     rx.text(est.escoger.caracteristica),
                     rx.text(est.escoger.personaje_escogido),
                     rx.button("Enviar", on_click=est.escoger.validar),
                     rx.text(est.escoger.validacion),
                     direction="row",)

def juego():
    return rx.center(pregunta(), )