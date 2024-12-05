import pytest
from src.comprobar_caracteristica import caracteristica_valida

caracteristicas = ["gafas", "pelo castaño oscuro", "pelo escaso", "nariz mediana", "pelo rubio", "pelirojo", "boca pequeña", "ojos marrones", "pelo castaño", "nariz grande", "boca grande", "ojos azules", "mofletes colorados", "aspecto risueño", "aspecto triste", "pelo blanco", "nariz pequeña",  "mofletes estirados", "aspecto serio"]

def test_caracteristica_erronea():
    assert not caracteristica_valida("sdaf")

def test_caracteristica_vacia():
    assert not caracteristica_valida("")

def test_caracteristica():
    assert caracteristica_valida("Pelo blanco")
    for caracteristica in caracteristicas:
        assert caracteristica_valida(caracteristica)