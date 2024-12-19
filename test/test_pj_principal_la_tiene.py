import pytest
from src.girar_personajes import pj_principal_la_tiene

def test_incorrecto():
    assert not pj_principal_la_tiene("pelo rubio", "Philip")
    assert not pj_principal_la_tiene("ojos marrones", "Anita")
    assert not pj_principal_la_tiene("ojouhyuyguygy", "Anita")
    

def test_correcto():
    assert pj_principal_la_tiene("pelo blanco", "Susan")
    assert pj_principal_la_tiene("boca grande", "Susan")
    