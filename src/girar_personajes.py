import reflex as rx
import quien_es_quien.personajes.personajes as pjs
def pj_principal_la_tiene(caracteristica, personaje_principal):
    return True if caracteristica in pjs.personajes[personaje_principal] else False

def cuales_girar_pjs(caracteristica, personaje_girados, personaje_principal):
    personajes_a_girar = []
    la_tiene = pj_principal_la_tiene(caracteristica, personaje_principal)
    for personaje in pjs.personajes.keys():
        if personaje not in personaje_girados:
            if la_tiene:
                if caracteristica not in pjs.personajes[personaje]:
                    personajes_a_girar.append(personaje)
            else:
                if caracteristica in pjs.personajes[personaje]:
                    personajes_a_girar.append(personaje)
    return personajes_a_girar

def girar_pjs(girados, personajes_girar):
    for personaje in personajes_girar:
        girados[personaje] = True
    return girados
