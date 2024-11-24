import reflex as rx
import quien_es_quien.paginas.menu_inicio as menu
import quien_es_quien.paginas.qeq_juego as juego
from rxconfig import config

app = rx.App()
app.add_page(menu.index)
app.add_page(juego.juego)