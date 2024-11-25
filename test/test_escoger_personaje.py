import pytest
from src.escoger_personaje import escoger_personaje

personajes = ("Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul")


def test_escoger():
    assert escoger_personaje(personajes)