# Quién es quién

**Tabla de contenidos**

-   [**Introducción**](#introducción)
-   [**Manual**](#manual)
    -   [**Pre-requisitos**](#pre-requisitos)
    -   [**Instalación**](#instalación)
    -   [**Uso**](#uso)
-   [**Metodología**](#metodología)
-   [**Descripción técnica**](#descripción-técnica)
    -   [**Requisitos funcionales/no funcionales, NOT LIST**](#partes-interesadas-y-requisitos-funcionalesno-funcionales)
    -   [**Historias de usuaria**](#historias-de-usuaria)
    -   [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-   [**Diseño**](#diseño)
    -   [**Diagrama de Componentes**](#componentes)
-   [**Implementacion**](#implementacion)
    -   [**Tecnologías y Herramientas utilizadas**](#tecnologías-y-herramientas-elegidas)
    -   [**Backend**](#backend)
    -   [**Frontend**](#frontend)
-   [**Pruebas**](#pruebas)
    -   [**Coverage**](#coverage)
    -   [**Test de unidad**](#test-de-unidad)
    -   [**Test de integración**](#test-de-integración)
-   [**Análisis del tiempo invertido**](#Tiempo-invertido)
    -   [**Clockify + Wakatime**](#clockify)
    -   [**Justificación temporal**](#justificación-temporal)
-   [**Conclusiones**](#conclusiones)
    -   [**Posibles mejoras**](#posibles-mejoras)
    -   [**Dificultades**](#dificultades)

## Introducción

Este proyecto es una adaptación del juego clásico ¿Quién es Quién?, en el que intentarás adivinar por descarte el personaje elegido por la máquina. Lo realizamos [Alberto Orihuela Martínez](https://github.com/LxKarcer) y [Miguel Rodríguez Quintás](https://github.com/MiguelRQ24) durante el ultimo mes del primer trimestre de 1º de Desarrollo de Aplicaciones Multiplataforma en el módulo de Programación. 

En este proyecto usamos [Python](https://www.python.org/) para la lógica, y para la creación de sitio web usamos el framework [Reflex](https://reflex.dev/).

## Manual

### Pre-requisitos

-   `Git`
-   `Python3`
-   `pip`
-   `Reflex`

### Instalación

Se recomienda utilizar en 'virtualenv' para instalar todas las dependencias utilizadas por el programa. En [Windows](https://docs.python.org/es/3.8/library/venv.html) lo puedes instalar siguiendo su guía. En **Linux** ejecuta la siguiente instrucción.

```
$ sudo apt-get install python3-venv
```

En el directorio que quiera clone este repositorio.
```
> git clone https://github.com/MiguelRQ24/quien_es_quien.git
```

Entre dentro de la carpeta que se crea al clonar el repositorio.
```
> cd .\quien_es_quien\
```

En este directorio cree el entorno virtual.
``` 
> python -m venv venv
```

Entre en el entorno virtual.
```
> .\venv\Scripts\activate
```

Dentro del entorno virtual instale [Reflex](https://reflex.dev/docs/getting-started/installation/).
```
> pip install reflex
```

### Uso

Para poder jugar al quien es quien ejecute el siguiente comando:
```
> reflex run
```
Cuando termine de compilar entre en el localhost que ponga en `App running at: http://localhost:3000`
```
───────────────────────────────────────────────────────────────────────────────────────── Starting Reflex App ─────────────────────────────────────────────────────────────────────────────────────────
[12:19:26] Compiling: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 15/15 0:00:00
───────────────────────────────────────────────────────────────────────────────────────────── App Running ─────────────────────────────────────────────────────────────────────────────────────────────
App running at: http://localhost:3000
Backend running at: http://0.0.0.0:8000
```