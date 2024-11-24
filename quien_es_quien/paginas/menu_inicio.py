import reflex as rx

def jugar():
    return rx.button("JUGAR")

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(rx.heading(" "), rx.heading("¿Quién eis quién?",size="9"), jugar(), direction="column", align="center", spacing="9")
