from typing import List

# Genera una lista con los cuadrados de los números entre 1 y n
def cuadrados_hasta_n(n: int) -> List[int]:

    """ Generar una lista con los cuadrados de los números del 1 al n
    
    Pre: n debe ser un número entero positivo

    Post: devuelve una lista con los cuadrados de todos los enteros desde 1 hasta n

    """

    assert n > 0, "n debe ser un número positivo"
    lista = [i ** 2 for i in range(1, n + 1)]
    return lista

# Devuelve los últimos k elementos de una lista
def ultimos_elementos(lista: List[int], k: int) -> List[int]:

    """ Obtener los últimos k elementos de una lista
    
    Pre: la lista debe estar definida, k debe ser un entero positivo

    Post: devuelve una lista con los últimos k elementos

    """

    assert k > 0, "k debe ser positivo"
    return lista[-k:]

# Programa principal
def main() -> None:

    """ Programa nucleo

    Pre: un numero entero positivo

    Post: muestra el resultado de las funciones por pantalla

    """

    n = int(input("Ingrese un número N: "))
    lista_cuadrados = cuadrados_hasta_n(n)
    print(f"Lista completa: {lista_cuadrados}")

    ultimos = ultimos_elementos(lista_cuadrados, 10)
    print(f"Últimos 10 valores: {ultimos}")


if __name__ == "__main__":
    main()