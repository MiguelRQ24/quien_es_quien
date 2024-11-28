import reflex as rx
import quien_es_quien.personajes.personajes as pjs
from src.escoger_personaje import escoger_personaje
from src.comprobar_caracteristica import caracteristica_valida
from src.girar_personajes import girar_pjs

personajes = ("susan", "claire", "david", "anne", "robert", "anita", "joe", "george", "bill", "alfred", "max", "tom", "alex", "sam", "richard", "paul")

class escoger(rx.State):
    personaje_escogido: str
    def escoger(self):
        self.personajes_girar.clear()
        self.personaje_escogido = ""
        self.personaje_escogido = escoger_personaje(personajes)
        return rx.redirect("/juego")
    caracteristica: str
    validacion: bool
    def validar(self): 
        self.validacion = caracteristica_valida(self.caracteristica)
        self.cual_girar()
    personajes_girar: list = []
    def cual_girar(self):
        if self.validacion:
            self.personajes_girar += girar_pjs(self.caracteristica, self.personajes_girar, self.personaje_escogido)
    def susan(self):
        return rx.cond(self.personajes_girar.__contains__("susan"), rx.text("girado") , rx.text("Susan"))