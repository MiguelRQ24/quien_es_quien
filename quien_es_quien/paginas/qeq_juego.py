import reflex as rx
import quien_es_quien.estado as est
import quien_es_quien.estilos as estilo

def vista_persnajes():
    return rx.grid( rx.cond(est.escoger.girados["susan"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjSusan.jpg", width="100px", height="auto"), rx.text("Susan"), direction="column")),
                    rx.cond(est.escoger.girados["robert"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjRobert.jpg", width="100px", height="auto"),rx.text("Robert"))),
                    rx.cond(est.escoger.girados["claire"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjClaire.jpg", width="100px", height="auto"),rx.text("Claire"))),
                    rx.cond(est.escoger.girados["david"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjDavid.jpg", width="100px", height="auto"),rx.text("David"))),
                    rx.cond(est.escoger.girados["anne"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjAnne.jpg", width="100px", height="auto"),rx.text("Anne"))),
                    rx.cond(est.escoger.girados["george"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjGeorge.jpg", width="100px", height="auto"),rx.text("George"))),
                    rx.cond(est.escoger.girados["joe"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjJoe.jpg", width="100px", height="auto"),rx.text("Joe"))),
                    rx.cond(est.escoger.girados["anita"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjAnita.jpg", width="100px", height="auto"),rx.text("Anita"))),
                    rx.cond(est.escoger.girados["bill"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjBill.jpg", width="100px", height="auto"),rx.text("Bill"))),
                    rx.cond(est.escoger.girados["alfred"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjAlfred.jpg", width="100px", height="auto"),rx.text("Alfred"))),
                    rx.cond(est.escoger.girados["max"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjMax.jpg", width="100px", height="auto"),rx.text("Max"))),
                    rx.cond(est.escoger.girados["tom"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjTom.jpg", width="100px", height="auto"),rx.text("Tom"))),
                    rx.cond(est.escoger.girados["sam"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjSam.jpg", width="100px", height="auto"),rx.text("Sam"))),
                    rx.cond(est.escoger.girados["richard"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjRichard.jpg", width="100px", height="auto"),rx.text("Richard"))),
                    rx.cond(est.escoger.girados["paul"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjPaul.jpg", width="100px", height="auto"),rx.text("Paul"))),
                    rx.cond(est.escoger.girados["maria"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjMaria.jpg", width="100px", height="auto"),rx.text("Maria"))),
                    rx.cond(est.escoger.girados["frans"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjFrans.jpg", width="100px", height="auto"),rx.text("Frans"))),
                    rx.cond(est.escoger.girados["philip"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjPhilip.jpg", width="100px", height="auto"),rx.text("Philip"))),
                    rx.cond(est.escoger.girados["eric"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjEric.jpg", width="100px", height="auto"),rx.text("Eric"))),
                    rx.cond(est.escoger.girados["peter"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjPeter.jpg", width="100px", height="auto"),rx.text("Peter"))),
                    rx.cond(est.escoger.girados["herman"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjHerman.jpg", width="100px", height="auto"),rx.text("Herman"))), 
                    rx.cond(est.escoger.girados["bernard"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjBernard.jpg", width="100px", height="auto"),rx.text("Bernard"))),
                    rx.cond(est.escoger.girados["charles"], rx.text("girado", color_scheme="red") , rx.vstack(rx.image(src="/pjCharles.jpg", width="100px", height="auto"),rx.text("Charles"))),
                    rx.cond(est.escoger.girados["alex"], rx.text("girado", color_scheme="red"), rx.vstack(rx.image(src="/personajes_qsq_01.png", width="100px", height="auto"), rx.text("Alex"))),
                    columns="8", rows="3", spacing="3")
def pregunta():
    return rx.vstack(
        rx.hstack(  rx.text("Tu personaje tiene:"),
                    rx.input(placeholder="Caracteristica", on_change=est.escoger.set_caracteristica, size="1" ),
                    rx.button("Enviar", on_click=est.escoger.validar, size="1"),
                    rx.text("Tu personaje es:"),

                    direction="row"), 
                    rx.text(rx.cond(est.escoger.validacion, "", "caracteristica incorrecta, prueba otra vez")),)

def enviar_pj():
    return  rx.hstack(
                      rx.input(placeholder="Personaje", on_change=est.escoger.set_intento_acierto, size='1'),
                      rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.button("Enviar", on_click=est.escoger.comprobar_pj),
                        ),
                        rx.alert_dialog.content(
                            rx.alert_dialog.title(rx.cond(est.escoger.gano, "¡Usted ha ganado!", "¡Usted ha perdido!")),
                            rx.alert_dialog.description(rx.cond(est.escoger.gano, 
                                                                f"¡Felicidades! El personaje era {est.escoger.personaje_escogido}",
                                                                f"El personaje era {est.escoger.personaje_escogido} y usted ha elegido a {est.escoger.intento_acierto}")
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
                    )                      
                      ) 



 
                    
def personajes_volteados():
    return rx.grid(rx.foreach(est.personajes,
                              lambda i: rx.vstack(rx.image(src="/pjAzul.jpg", width="100px", height="auto"), rx.text("¿?¿?¿?")),
                              ),
                   columns="8", rows="3", spacing="3")

def escoger_personaje_aleatorio():
    return rx.button(rx.text("Escoger Personaje Aleatorio", size="7"), size="4",
                     color_scheme="blue",
                     on_click=est.escoger.escoger
                     )
def previa():
    return rx.center( personajes_volteados(), escoger_personaje_aleatorio(), direction="column")       

def juego():
    return rx.center(rx.vstack(vista_persnajes(), 
                               rx.hstack(pregunta(),enviar_pj()), 
                               direction="column", align="center" ))