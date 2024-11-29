from src.comprobador_personaje import comprobador_pers
import pytest 


def test_correctos():
    assert comprobador_pers("susan", "susan")

def test_erroneo():
    assert not comprobador_pers("philip", "ñiñiñiñi")
