
def area_triangulo(base, altura):
    """
        calcula a area de um triangulo
    """

    if base < 0 or altura < 0:
        raise ValueError("Base e altura devem ser maiores que zero")
    return (base * altura) / 2


#base = int(input("Digite o valor da base do triângulo: "))
#altura = int(input("Digite o valor da altura do triângulo: "))
#print(area_triangulo(base, altura))