import reflex as rx

def titulo():
    return rx.heading("¿Quién es quién?",size="9")

def jugar():
    return rx.button(rx.text("JUGAR", size="7"),
                     size="4",
                     color_scheme="grass",
                     on_click=rx.redirect("/juego")
                     )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(rx.heading(" "), titulo(), jugar(), direction="column", align="center", spacing="9")
