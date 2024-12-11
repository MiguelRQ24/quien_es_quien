import pytest
from src.girar_personajes import pj_principal_la_tiene

def test_incorrecto():
    assert not pj_principal_la_tiene("pelo rubio", "philip")
    assert not pj_principal_la_tiene("ojos marrones", "anita")
    assert not pj_principal_la_tiene("ojouhyuyguygy", "anita")
    

def test_correcto():
    assert pj_principal_la_tiene("pelo blanco", "susan")
    assert pj_principal_la_tiene("boca grande", "susan")
    