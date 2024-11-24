import reflex as rx

def titulo():
    return rx.heading("¿Quién eis quién?",size="9")

def jugar():
    return rx.button("JUGAR")

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(rx.heading(" "), titulo(), jugar(), direction="column", align="center", spacing="9")
