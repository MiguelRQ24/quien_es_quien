import reflex as rx
import quien_es_quien.estado as est

def vista_persnajes():
    return rx.grid( rx.cond(est.escoger.girados["susan"], rx.text("girado") , rx.text("Susan")),
                    rx.cond(est.escoger.girados["robert"], rx.text("girado") , rx.text("Robert")),
                    rx.cond(est.escoger.girados["claire"], rx.text("girado") , rx.text("Claire")),
                    rx.cond(est.escoger.girados["david"], rx.text("girado") , rx.text("David")),
                    rx.cond(est.escoger.girados["anne"], rx.text("girado") , rx.text("Anne")),
                    rx.cond(est.escoger.girados["george"], rx.text("girado") , rx.text("George")),
                    rx.cond(est.escoger.girados["joe"], rx.text("girado") , rx.text("Joe")),
                    rx.cond(est.escoger.girados["anita"], rx.text("girado") , rx.text("Anita")),
                    rx.cond(est.escoger.girados["bill"], rx.text("girado") , rx.text("Bill")),
                    rx.cond(est.escoger.girados["alfred"], rx.text("girado") , rx.text("Alfred")),
                    rx.cond(est.escoger.girados["max"], rx.text("girado") , rx.text("Max")),
                    rx.cond(est.escoger.girados["tom"], rx.text("girado") , rx.text("Tom")),
                    rx.cond(est.escoger.girados["alex"], rx.text("girado") , rx.text("Alex")),
                    rx.cond(est.escoger.girados["sam"], rx.text("girado") , rx.text("Sam")),
                    rx.cond(est.escoger.girados["richard"], rx.text("girado") , rx.text("Richard")),
                    rx.cond(est.escoger.girados["paul"], rx.text("girado") , rx.text("Paul")),
                    rx.cond(est.escoger.girados["maria"], rx.text("girado") , rx.text("Maria")),
                    rx.cond(est.escoger.girados["frans"], rx.text("girado") , rx.text("Frans")),
                    rx.cond(est.escoger.girados["philip"], rx.text("girado") , rx.text("Philip")),
                    rx.cond(est.escoger.girados["eric"], rx.text("girado") , rx.text("Eric")),
                    rx.cond(est.escoger.girados["peter"], rx.text("girado") , rx.text("Peter")),
                    rx.cond(est.escoger.girados["herman"], rx.text("girado") , rx.text("Herman")), 
                    rx.cond(est.escoger.girados["bernard"], rx.text("girado") , rx.text("Bernard")),
                    rx.cond(est.escoger.girados["charles"], rx.text("girado") , rx.text("Charles")),
                    columns="6", rows="4", spacing="3")
def pregunta():
    return rx.vstack(rx.hstack(rx.text("Tu personaje tiene:"),
                               rx.input(placeholder="Caracteristica", on_change=est.escoger.set_caracteristica), 
                               rx.button("Enviar", on_click=est.escoger.validar),
                               direction="row",
                              ),
                     rx.text(rx.cond(est.escoger.validacion, "", "caracteristica incorrecta, prueba otra vez")),
                     )

def juego():
    return rx.center(rx.vstack(vista_persnajes(), pregunta(), direction="column" ))