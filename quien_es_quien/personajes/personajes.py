import reflex as rx
personajes = {
    "robert": ("pelo marrón", "nariz grande", "boca grande", "ojos azules", "mofletes colorados", "aspecto triste"),
    "susan": ("pelo blanco", "nariz pequeña", "boca grande", "ojos castaños claros", "mofletes colorados", "aspecto risueño"),
    "clarie": ("pelo naranja", "nariz pequeña", "boca pequeña", "ojos castaños", "sombrero de flores", "pendientes"),
    "david": ("pelo rubio", "nariz pequeña", "boca grande", "ojos castaño claro", "mofletes estirados", "aspecto serio"),
    "anne": ("pelo marron", "nariz grande", "boca pequeña", "ojos castaño", "pendientes", "papada"),
    "george": ("pelo blanco", "nariz mediana", "boca grande", "ojos castaño claro", "mandibula prominente", "aspecto triste"),
    "joe": ("pelo rubio", "nariz media", "boca pequeña", "ojos castaño claro", "gafas", "aspecto risueño"),
    "anita": ("pelo rubio", "nariz pequeña", "boca pequeña", "ojos grises", "mofletes rojizos", "coletas"),
    "bill": ("pelo escaso", "pelo naranja", "nariz pequeña", "boca pequeña", "ojos castaño", "mofletes abundantes", "aspecto risueño"),
    "alfred":("pelo naranja", "nariz mediana", "boca pequeña", "ojos azules", "bigote", "aspecto serio"),
    "max": ("pelo negro", "nariz grande", "boca grande", "ojos castaño", "bigote", "pelo rizado"),
    "tom": ("pelo negro", "nariz pequeña", "boca pequeña", "ojos azules", "mofletes estirados", "pelo escaso"),
    "alex": ("pelo negro", "nariz pequeña", "boca grande", "ojos castaño claro", "mandibula prominente", "bigote"),
    "sam": ("pelo blanco", "nariz media", "boca pequeña", "ojos castaño oscuro", "mofletes rellenos", "pelo escaso"),
    "richard": ("pelo marron", "nariz media", "boca pequeña", "ojos castaño", "barba abundante", "pelo escaso"),
    "paul":("pelo blanco", "nariz pequeña", "boca pequeña", "ojos castaño", "mofletes estirados", "aspecto sereno"),
    "maria":("pelo castaño", "nariz pequeña", "boca mediana", "ojos castaño", "boina", "pendientes"),
    "frans":("pelo naranja", "nariz pequeña", "boca pequeñas", "ojos castaño claro", "mofletes estirados", "cara cuadrada"),
    "philip": ("pelo marron oscuro", "nariz pequeña", "boca grande", "ojos castaño claro", "pelo ruloso", "mofletes colorados"),
    "eric":("pelo rubio", "nariz pequeña", "boca grande", "ojos castaño claro", "gorra", "cara cuadrada"),
    "david":("pelo rubio", "nariz mediana", "boca grande", "ojos castaño claro", "bigote", "orejas grandes"),
    "peter": ("pelo blanco", "nariz grande", "boca grande", "ojos azules", "mofletes prominentes"),
    "herman":("pelo naranja", "nariz grande", "boca pequeña", "ojos castaño claro", "mandibula pronunciada", "aspecto serio", "pelo escaso"),
    "bernard":("pelo marron", "nariz grande", "boca pequeña", "ojos castaño", "gorra", "aspecto serio")

}

class robert(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo marrón", "nariz grande", "boca grande", "ojos azules", "mofletes colorados", "aspecto triste")

class susan(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo blanco", "nariz pequeña", "boca grande", "ojos castaños claros", "mofletes colorados", "aspecto risueño")

class claire(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo naranja", "nariz pequeña", "boca pequeña", "ojos castaños", "sombrero de flores", "pendientes")

class david(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz pequeña", "boca grande", "ojos castaño claro", "mofletes estirados", "aspecto serio")
    
class anne(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo marron", "nariz grande", "boca pequeña", "ojos castaño", "pendientes", "papada")

class george(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo blanco", "nariz mediana", "boca grande", "ojos castaño claro", "mandibula prominente", "aspecto triste")

class joe (rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz media", "boca pequeña", "ojos castaño claro", "gafas", "aspecto risueño")

class anita(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz pequeña", "boca pequeña", "ojos grises", "mofletes rojizos", "coletas")

class bill(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo escaso", "pelo naranja", "nariz pequeña", "boca pequeña", "ojos castaño", "mofletes abundantes", "aspecto risueño")
    
class alfred(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo naranja", "nariz mediana", "boca pequeña", "ojos azules", "bigote", "aspecto serio")

class max(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo negro", "nariz grande", "boca grande", "ojos castaño", "bigote", "pelo rizado")

class tom(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo negro", "nariz pequeña", "boca pequeña", "ojos azules", "mofletes estirados", "pelo escaso")

class alex(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo negro", "nariz pequeña", "boca grande", "ojos castaño claro", "mandibula prominente", "bigote")

class sam(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo blanco", "nariz media", "boca pequeña", "ojos castaño oscuro", "mofletes rellenos", "pelo escaso")

class richard(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo marron", "nariz media", "boca pequeña", "ojos castaño", "barba abundante", "pelo escaso")

class paul(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo blanco", "nariz pequeña", "boca pequeña", "ojos castaño", "mofletes estirados", "aspecto sereno")

class maria(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo castaño", "nariz pequeña", "boca mediana", "ojos castaño", "boina", "pendientes")

class frans(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo naranja", "nariz pequeña", "boca pequeñas", "ojos castaño claro", "mofletes estirados", "cara cuadrada")

class philip(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo marron oscuro", "nariz pequeña", "boca grande", "ojos castaño claro", "pelo ruloso", "mofletes colorados")
    
class eric(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz pequeña", "boca grande", "ojos castaño claro", "gorra", "cara cuadrada")

class david(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz mediana", "boca grande", "ojos castaño claro", "bigote", "orejas grandes")

class david(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo rubio", "nariz pequeña", "boca grande", "ojos castaño claro", "mofletes estirados", "aspecto serio")
    
class peter(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo blanco", "nariz grande", "boca grande", "ojos azules", "mofletes prominentes")

class herman(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo naranja", "nariz grande", "boca pequeña", "ojos castaño claro", "mandibula pronunciada", "aspecto serio", "pelo escaso")

class bernard(rx.State):

    # Crear la constante atributos del personaje
    ATRIBUTOS: tuple
    # Adjudicar atributos personaje
    ATRIBUTOS = ("pelo marron", "nariz grande", "boca pequeña", "ojos castaño", "gorra", "aspecto serio")

    
       
    
    
    

        
    
    
    
    
    