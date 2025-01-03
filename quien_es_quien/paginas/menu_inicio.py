import reflex as rx
import quien_es_quien.estado as est
def titulo():
    return rx.heading("¿Quién es quién?",size="9")

def jugar():
    return rx.button(rx.text("JUGAR", size="7"), size="4",
                     color_scheme="grass",
                     on_click=est.estado.jugar
                     )

def index() -> rx.Component:
    
    return rx.center(rx.heading(" "), titulo(), jugar(), direction="column", align="center", spacing="9")
