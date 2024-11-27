import reflex as rx
import quien_es_quien.personajes.personajes as pjs
from src.escoger_personaje import escoger_personaje
from src.comprobar_caracteristica import caracteristica_valida
from src.tiene_caracteristica import tiene_caracteristica

personajes = ("susan", "claire", "david", "anne", "robert", "anita", "joe", "george", "bill", "alfred", "max", "tom", "alex", "sam", "richard", "paul")

class escoger(rx.State):
    personaje_escogido: str
    def escoger(self):
        self.personaje_escogido = ""
        self.personaje_escogido = escoger_personaje(personajes)
        return rx.redirect("/juego")
    caracteristica: str
    validacion: str
    def validar(self): 
        self.validacion = caracteristica_valida(self.caracteristica)
