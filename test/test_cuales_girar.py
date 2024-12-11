import pytest
from src.girar_personajes import cuales_girar_pjs

def test_correcto():
    assert cuales_girar_pjs("pelo rubio", ['anita'], 'philip') == ['david','joe','eric','charles']
    assert cuales_girar_pjs("pelo rubio", [], 'anita') == ['robert', 'susan', 'claire', 'anne', 'george', 'bill', 'alfred', 'max', 'tom', 'alex', 'sam', 'richard', 'paul', 'maria', 'frans', 'philip', 'peter', 'herman', 'bernard']
