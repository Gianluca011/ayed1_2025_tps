from typing import List, Any

# Verifica si la lista está ordenada en forma ascendente
def esta_ordenada(lista: List[Any]) -> bool:

    """ Verificar si una lista está ordenada en forma ascendente
    
    Pre: lista debe estar definida

    Post: devuelve True si la lista está ordenada ascendentemente, False en caso contrario

    """

    assert isinstance(lista, list), "El parámetro debe ser una lista"

    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Programa principal para probar la función
def main() -> None:

    """ Programa nucleo

    Pre: ninguna

    Post: muestra el resultado de la funcion por pantalla

    """

    lista1 = [1, 2, 3]
    lista2 = [3, 2, 1]
    lista3 = ['a', 'b', 'c']
    lista4 = ['b', 'a']
    lista5 = []

    print(f"{lista1} -> {esta_ordenada(lista1)}")
    print(f"{lista2} -> {esta_ordenada(lista2)}")
    print(f"{lista3} -> {esta_ordenada(lista3)}")
    print(f"{lista4} -> {esta_ordenada(lista4)}")
    print(f"{lista5} -> {esta_ordenada(lista5)}")


if __name__ == "__main__":
    main()