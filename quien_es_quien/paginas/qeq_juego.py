import reflex as rx
import quien_es_quien.estado as est
import quien_es_quien.estilos as estilo
import quien_es_quien.personajes.personajes as pjs

def vista_persnajes() -> rx.Component:
    return rx.grid(rx.foreach(est.personajes, 
                              lambda personaje: rx.cond(
                                                        est.estado.girados[personaje], 
                                                        rx.vstack(rx.image(src=f"/pj{personaje}BN.jpg", width="100px", height="auto"), rx.text(personaje, color_scheme="red")), 
                                                        rx.vstack(rx.image(src=f"/pj{personaje}.jpg", width="100px", height="auto"), rx.text(personaje))
                                                        )
                             ),
                   columns="8", rows="3", spacing="3",)
def pregunta():
    return rx.vstack(
        rx.hstack(  rx.text("Tu personaje tiene:"),
                    rx.input(placeholder="Caracteristica", on_change=est.estado.set_caracteristica, size="1" ),
                    rx.button("Enviar", on_click=est.estado.validar, size="1"),
                    rx.text("Tu personaje es:"),

                    direction="row"), 
                    rx.text(rx.cond(est.estado.validacion, "", "caracteristica incorrecta, prueba otra vez")),)

def enviar_pj():
    return  rx.hstack(
                      rx.input(placeholder="Personaje", on_change=est.estado.set_intento_acierto, size='1'),
                      rx.cond(est.estado.intento_acierto,
                      rx.alert_dialog.root(
                        rx.alert_dialog.trigger( 
                            rx.button("Enviar", on_click=est.estado.comprobar_pj),
                        ), 
                        rx.alert_dialog.content(
                            rx.alert_dialog.title(rx.cond(est.estado.gano, "¡Usted ha ganado!", "¡Usted ha perdido!")),
                            rx.alert_dialog.description(rx.cond(est.estado.gano, 
                                                                f"¡Felicidades! El personaje era {est.estado.personaje_escogido}",
                                                                f"El personaje era {est.estado.personaje_escogido} y usted ha elegido a {est.estado.intento_acierto}")
                                                       ),
                            rx.flex(
                                rx.alert_dialog.cancel(
                                    rx.button("Volver al menu", on_click=rx.redirect("/")),
                                ),
                                rx.alert_dialog.action(
                                    rx.button("Volver a jugar", on_click=rx.redirect("/previa")),
                                ),
                                spacing="3",
                            ),
                        ),
                        ),
                        rx.button("Enviar")
                        )                     
                      ) 

def caracteristicas():
    return rx.unordered_list(rx.foreach(pjs.caracteristicas, lambda carcateristica : rx.hstack(rx.checkbox(f"{carcateristica}", size="3"))))

def personajes_volteados():
    return rx.grid(rx.foreach(est.personajes,
                              lambda i: rx.vstack(rx.image(src="/pjAzul.jpg", width="100px", height="auto"), rx.text("¿?¿?¿?")),
                              ),
                   columns="8", rows="3", spacing="3")

def escoger_personaje_aleatorio():
    return rx.button(rx.text("Escoger Personaje Aleatorio", size="7"), size="4",
                     color_scheme="blue",
                     on_click=est.estado.escoger
                     )

def tablero_botones():
    return rx.center(rx.vstack(vista_persnajes(), 
                               rx.hstack(pregunta(),enviar_pj()), 
                               direction="column", align="center" ))

def previa():
    return rx.center( personajes_volteados(), escoger_personaje_aleatorio(), direction="column")       

def juego():
    return rx.center(rx.hstack((tablero_botones()), caracteristicas(), align="center", spacing="6" )) 