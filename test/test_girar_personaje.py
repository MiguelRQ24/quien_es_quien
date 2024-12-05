import pytest
from src.girar_personajes import girar_pjs
girados = {
            "susan": False, 'robert': False, 'claire': False, 'david': False, 'anne': False, 'george': False, 
            'joe': False, 'anita': False, 'bill': False, 'alfred': False, 'max': False, 'tom': False, 'alex': False, 
            'sam': False, 'richard': False, 'paul': False, 'maria': False, 'frans': False, 'philip': False, 
            'eric': False, 'peter': False, 'herman': False, 'bernard': False, "charles": False
            }

def test_correcto():
    assert girar_pjs(girados, ["susan", "robert", "claire", "charles"]) == {
            "susan": True, 'robert': True, 'claire': True, 'david': False, 'anne': False, 'george': False, 
            'joe': False, 'anita': False, 'bill': False, 'alfred': False, 'max': False, 'tom': False, 'alex': False, 
            'sam': False, 'richard': False, 'paul': False, 'maria': False, 'frans': False, 'philip': False, 
            'eric': False, 'peter': False, 'herman': False, 'bernard': False, "charles": True
            }

    assert girar_pjs(girados, ['robert', 'susan', 'claire', 'david', 'anne', 'george', 'joe', 'anita', 'bill', 'alfred', 'max', 'tom', 'alex', 'sam', 'richard', 'paul', 'maria', 'frans', 'philip', 'eric', 'peter', 'herman', 'bernard', "charles"]) == {
            "susan": True, 'robert': True, 'claire': True, 'david': True, 'anne': True, 'george': True, 
            'joe': True, 'anita': True, 'bill': True, 'alfred': True, 'max': True, 'tom': True, 'alex': True, 
            'sam': True, 'richard': True, 'paul': True, 'maria': True, 'frans': True, 'philip': True, 
            'eric': True, 'peter': True, 'herman': True, 'bernard': True, "charles": True
            }
    