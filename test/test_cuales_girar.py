import pytest
from src.girar_personajes import cuales_girar_pjs

def test_correcto():
    assert cuales_girar_pjs("pelo rubio", ['Anita'], 'Philip') == ['David','Joe','Eric','Charles']
    assert cuales_girar_pjs("pelo rubio", [], 'Anita') == ['Robert', 'Susan', 'Claire', 'Anne', 'George', 'Bill', 'Alfred', 'Max', 'Tom', 'Alex', 'Sam', 'Richard', 'Paul', 'Maria', 'Frans', 'Philip', 'Peter', 'Herman', 'Bernard']
