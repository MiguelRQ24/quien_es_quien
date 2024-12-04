import reflex as rx
import quien_es_quien.personajes.personajes as pjs
from src.escoger_personaje import escoger_personaje
from src.comprobar_caracteristica import caracteristica_valida
from src.girar_personajes import girar_pjs
from src.comprobador_personaje import comprobador_pers

personajes = ['robert', 'susan', 'claire', 'david', 'anne', 'george', 'joe', 'anita', 'bill', 'alfred', 'max', 'tom', 'alex', 'sam', 'richard', 'paul', 'maria', 'frans', 'philip', 'eric', 'peter', 'herman', 'bernard', "charles"]

class escoger(rx.State):
    personaje_escogido: str
    girados: dict
    def jugar(self):
        return rx.redirect("/previa")
    
    def escoger(self):
        self.personaje_escogido = ""
        self.caracteristica = ""
        self.validacion = True
        self.personajes_girar = []
        self.personajes_rectos = list(personajes)
        self.girados = {
                    "susan": False, 'robert': False, 'claire': False, 'david': False, 'anne': False, 'george': False, 
                    'joe': False, 'anita': False, 'bill': False, 'alfred': False, 'max': False, 'tom': False, 'alex': False, 
                    'sam': False, 'richard': False, 'paul': False, 'maria': False, 'frans': False, 'philip': False, 
                    'eric': False, 'peter': False, 'herman': False, 'bernard': False
}
        self.personaje_escogido = escoger_personaje(personajes)
        self.intento_acierto = ""
        return rx.redirect("/juego")
    
    caracteristica: str
    validacion: bool
    def validar(self): 
        self.validacion = caracteristica_valida(self.caracteristica)
        self.cual_girar()

    personajes_girar: list
    def cual_girar(self):
        if self.validacion:
            self.personajes_girar += girar_pjs(self.caracteristica, self.personajes_girar, self.personaje_escogido)
        self.girar()
        
    personajes_rectos: list


    def girar(self):
        for personaje in self.personajes_girar:
            if personaje in self.personajes_rectos:
                self.girados[personaje] = True
                self.personajes_rectos.remove(personaje)
 
    intento_acierto: str
    gano: bool 
    def comprobar_pj(self):
        self.gano = comprobador_pers(self.personaje_escogido, self.intento_acierto)
           