import reflex as rx
from src.escoger_personaje import escoger_personaje 

personajes = ("Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul")

class escoger(rx.State):
    personaje_escogido: str
    def escoger(self):
        self.personaje_escogido = escoger_personaje(personajes)
        return rx.redirect("/juego")
    