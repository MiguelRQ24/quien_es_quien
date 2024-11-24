import reflex as rx
import quien_es_quien.paginas.menu_inicio as menu
from rxconfig import config

app = rx.App()
app.add_page(menu.index)
