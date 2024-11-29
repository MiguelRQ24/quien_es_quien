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
                    rx.input(placeholder="Personaje", on_change=est.escoger.set_intento_acierto, size='1'), 
                    rx.button("Enviar", on_click=est.escoger.enviar_personaje),
                    direction="row"), 
                    rx.text(rx.cond(est.escoger.validacion, "", "caracteristica incorrecta, prueba otra vez")),)
            
                    

def juego():
    return rx.center(rx.vstack(vista_persnajes(), pregunta(), direction="column" ))