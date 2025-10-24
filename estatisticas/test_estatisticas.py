from estatisticas import *
import pytest

def test_media():
    """
        Testa o cálculo da média de uma lista de números.
    """
    assert media([1, 2, 3, 4, 5]) == 3.0
    assert media([10, 20, 30, 40, 50]) == 30.0


def test_media_valores_negativos():
    """
        Testa o cálculo da média de uma lista de números com valores negativos.
    """
    assert media([-1, -2, -3, -4, -5]) == -3.0
    assert media([-10, -20, -30, -40, -50]) == -30.0


def test_valores_texto():
    """
        Testa se uma exceção ValueError é levantada quando a lista contém valores não numéricos.
    """
    with pytest.raises(TypeError):
        media(["a", "b", "c"])
    with pytest.raises(ValueError):
        media([])


def test_mediana():
    """
        Testa o cálculo da mediana de uma lista de números.
    """
    assert mediana([1, 2, 3, 4, 5]) == 3.0
    assert mediana([10, 20, 30, 40, 50]) == 30.0


def test_mediana_valores_negativos():
    """
        Testa o cálculo da mediana de uma lista de números com valores negativos.
    """
    assert mediana([-1, -2, -3, -4, -5]) == -3.0
    assert mediana([-10, -20, -30, -40, -50]) == -30.0


def test_mediana_texto():
    """
        Testa se uma exceção ValueError é levantada quando a lista contém valores não numéricos.
    """
    with pytest.raises(TypeError):
        mediana(["a", "b", "c"])
    with pytest.raises(ValueError):
        mediana([])


def test_desvio_padrao():
    """
        Testa o cálculo do desvio padrão de uma lista de números.
    """
    assert desvio_padrao([1, 2, 3, 4, 5]) == 1.4142135623730951
    assert desvio_padrao([10, 20, 30, 40, 50]) == 14.142135623730951


def test_desvio_padrao_valores_negativos():
    """
        Testa o cálculo do desvio padrão de uma lista de números com valores negativos.
    """
    assert desvio_padrao([-1, -2, -3, -4, -5]) == 1.4142135623730951
    assert desvio_padrao([-10, -20, -30, -40, -50]) == 14.142135623730951


def test_desvio_padrao_texto():
    """
        Testa se uma exceção ValueError é levantada quando a lista contém valores não numéricos.
    """
    with pytest.raises(TypeError):
        desvio_padrao(["a", "b", "c"])
    with pytest.raises(ValueError):
        desvio_padrao([])


def test_detectar_outliers():
    """
        Testa a detecção de outliers em uma lista de números.
    """
    assert detectar_outliers([1, 2, 3, 4, 5]) == []
    assert detectar_outliers([10, 20, 30, 40, 50, 100]) == [100]
    assert detectar_outliers([1, 99, 100, 98, 97, 99, 99]) == [1]


def test_detectar_outliers_texto():
    """
        Testa se uma exceção ValueError é levantada quando a lista contém valores não numéricos.
    """
    with pytest.raises(TypeError):
        detectar_outliers(["a", "b", "c"])
    with pytest.raises(ValueError):
        detectar_outliers([])