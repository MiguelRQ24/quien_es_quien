"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(rx.heading(" "), rx.heading("¿Quién es quién?",size="9",),rx.button("JUGAR"), direction="column", align="center", spacing="9")

app = rx.App()
app.add_page(index)
