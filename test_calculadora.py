import pytest
from calculadora import Calculadora

c = Calculadora()

def test_soma():
    assert c.soma(3, 2) == 5

def test_subtrai():
    assert c.subtrai(10, 4) == 6

def test_multiplica():
    assert c.multiplica(2, 3) == 6

def test_divide():
    assert c.divide(9, 3) == 3

def test_divisao_zero():
    with pytest.raises(ValueError):
        c.divide(5, 0)

def test_potencia():
    assert c.potencia(2, 4) == 16

def test_raiz():
    assert c.raiz(25) == 5

def test_raiz_negativa():
    with pytest.raises(ValueError):
        c.raiz(-1)

def test_media():
    assert c.media([2, 4, 6]) == 4

def test_media_vazia():
    with pytest.raises(ValueError):
        c.media([])

def test_modulo():
    assert c.modulo(-8) == 8

def test_percentual():
    assert c.percentual(30, 120) == 25

def test_percentual_total_zero():
    with pytest.raises(ValueError):
        c.percentual(10, 0)
