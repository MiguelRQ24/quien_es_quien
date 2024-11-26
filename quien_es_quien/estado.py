import reflex as rx
from src.escoger_personaje import escoger_personaje 
import src.tiene_caracteristica as tiene_caracteristica

personajes = ("Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul")

class escoger(rx.State):
    personaje_escogido: str
    def escoger(self):
        self.personaje_escogido = escoger_personaje(personajes)
        return rx.redirect("/juego")

class caracteristicas(rx.State):
    caracteristica: str
    def tiene_caracteristica(self):
        tiene_caracteristica.tiene_caracteristica(caracteristicas.caracteristica, escoger.personaje_escogido)