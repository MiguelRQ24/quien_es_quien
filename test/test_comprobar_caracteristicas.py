import pytest
from src.comprobar_caracteristica import caracteristica_valida

def test_caracteristica_erronea():
    assert not caracteristica_valida("sdaf")

def test_caracteristica():
    assert caracteristica_valida("pelo blanco")