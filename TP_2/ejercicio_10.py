import random

# Esta función verifica si un número es impar
def es_impar(numero: int) -> bool:

    """ Verifica si un número entero es impar

    Pre: numero es un entero

    Post: devuelve True si el número es impar, de lo contrario False

    """

    return numero % 2 != 0

# Programa principal
def main():

    """ Programa nucleo

    Pre: ninguna

    Post: muestra por pantalla las dos listas generadas

    """

    lista_original = [random.randint(1, 100) for _ in range(10)]
    
    lista_impares = list(filter(es_impar, lista_original))
    
    print(f"Lista original de números: {lista_original}")
    print(f"Lista con los números impares: {lista_impares}")

if __name__ == "__main__":
    main()