import math

def media(lista):
    """
        calcula a media de uma lista de numeros
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    return sum(lista) / len(lista)


def mediana(lista):
    """
        calcula a mediana de uma lista de numeros
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        return lista[n // 2]


def desvio_padrao(lista):
    """
        calcula o desvio padrao de uma lista de numeros
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    m = media(lista)
    return math.sqrt(sum((x - m) ** 2 for x in lista) / len(lista))


def detectar_outliers(lista):
    """
        detecta outliers em uma lista de numeros
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    dp = desvio_padrao(lista)
    m = media(lista)
    return [x for x in lista if abs(x - m) > 2 * dp]


#print(detectar_outliers([1, 99, 100, 98,  97, 99, 99]))