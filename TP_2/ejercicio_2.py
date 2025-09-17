import random
from typing import List

# Genera una lista de n números aleatorios entre 1 y 100
def generar_lista_aleatoria(n: int) -> List[int]:

    """ Generar una lista de n números aleatorios del 1 al 100
    
    Pre: n debe ser un número entero positivo

    Post: devuelve una lista de longitud n con valores enteros entre 1 y 100

    """

    assert n > 0, "El tamaño de la lista debe ser positivo"
    lista = [random.randint(1, 100) for _ in range(n)]
    return lista

# Revisa si la lista tiene números repetidos
def contiene_repetidos(lista: List[int]) -> bool:

    """ Verificar si una lista contiene elementos repetidos
    
    Pre: una lista definida

    Post: devuelve True si hay elementos repetidos, False en caso contrario

    """

    return len(lista) != len(set(lista))

# Devuelve una nueva lista con solo los elementos únicos
def elementos_unicos(lista: List[int]) -> List[int]:

    """ Devolver una nueva lista con los elementos únicos de la lista original
    
    Pre: una lista definida

    Post: devuelve una lista que contiene solo los elementos únicos, sin importar el orden

    """

    unicos = list(set(lista))
    return unicos

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: un numero entero positivo

    Post: muestra el resultado de las funciones por pantalla

    """

    n = int(input("Ingrese el tamaño de la lista: "))
    lista = generar_lista_aleatoria(n)
    print(f"Lista generada: {lista}")

    hay_repetidos = contiene_repetidos(lista)
    print(f"¿La lista contiene repetidos? {hay_repetidos}")

    lista_unicos = elementos_unicos(lista)
    print(f"Lista con elementos únicos: {lista_unicos}")


if __name__ == "__main__":
    main()