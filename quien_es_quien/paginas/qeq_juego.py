import reflex as rx
import quien_es_quien.estado as est

def vista_persnajes():
    return rx.grid( rx.cond( est.escoger.girados["susan"], rx.text("girado") , rx.text("Susan")) , rx.text("Clarie"), rx.text("David"), columns="6", rows="4")
def pregunta():
    return rx.hstack(rx.text("Tu personaje tiene:"), 
                     rx.input(placeholder="Caracteristica", on_change=est.escoger.set_caracteristica), 
                     rx.text(est.escoger.personajes_girar),
                     rx.text(est.escoger.personaje_escogido),
                     rx.button("Enviar", on_click=est.escoger.validar),
                     rx.text(rx.cond(est.escoger.validacion, "", "caracteristica incorrecta, prueba otra vez")),
                     direction="row",)

def juego():
    return rx.center(rx.vstack(vista_persnajes(), pregunta(), direction="column" ))