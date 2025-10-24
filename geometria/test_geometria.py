import pytest
from geometria import area_triangulo

def test_area_triangulo():
    """
        Testa o cálculo da área de um triângulo com base e altura positivas.
    """
    assert area_triangulo(3, 4) == 6.0

def test_area_triangulo_valores_negativos():
    """
        Testa se uma exceção ValueError é levantada quando base ou altura são negativas.
    """
    with pytest.raises(ValueError):
        area_triangulo(-3, 4)

def test_area_triangulo_valores_zero():
    """
        Testa o cálculo da área de um triângulo com base ou altura zero.
    """
    assert area_triangulo(0, 4) == 0.0
    assert area_triangulo(4, 0) == 0.0

