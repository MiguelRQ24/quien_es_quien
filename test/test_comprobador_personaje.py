from src.comprobador_personaje import comprobador_pers
import pytest 

def test_correctos():
    assert comprobador_pers("susan", "susan")
    assert comprobador_pers("philip", "philip")
    
def test_erroneo():
    assert not comprobador_pers("philip", "ñiñiñiñi")
    
def test_mensaje_en_mayus():
    assert comprobador_pers('robert','RobErt')
    assert comprobador_pers('robert', 'ROBERT')    
