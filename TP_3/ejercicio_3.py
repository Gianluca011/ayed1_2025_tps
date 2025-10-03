import random
from typing import List

# Imprime la matriz de forma ordenada en consola
def imprimir_matriz(matriz: List[List[int]]) -> None:

    """ Imprime la matriz con formato

    Pre: matriz no vacía, representada como lista de listas de enteros

    Post: muestra la matriz en consola, cada fila en una línea con los valores alineados

    """

    for fila in matriz:
        print(" ".join(f"{x:3}" for x in fila))
    print()

def generar_matriz_sin_repetidos(n: int) -> List[List[int]]:

    """ Genera una matriz n por n con números enteros únicos aleatorios

    Pre: n mayor que 0

    Post: retorna una matriz de tamaño n por n, donde cada número dentro del rango aparece exactamente una vez

    """

    assert n > 0, "El tamaño de la matriz debe ser mayor que cero."

    # Generamos todos los números posibles
    numeros = list(range(n * n))

    # Los mezclamos para que queden en orden aleatorio
    random.shuffle(numeros)

    # Armamos la matriz n por n a partir de la lista mezclada
    matriz = [numeros[i * n:(i + 1) * n] for i in range(n)]

    return matriz

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: el usuario ingresa un número entero positivo n

    Post: genera una matriz de tamaño n por n con números aleatorios únicos y la muestra por consola

    """

    n = int(input("Ingrese el tamaño de la matriz N: "))
    matriz = generar_matriz_sin_repetidos(n)
    print("\nMatriz generada:\n")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()