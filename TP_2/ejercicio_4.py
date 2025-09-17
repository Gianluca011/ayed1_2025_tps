from typing import List

# Elimina de la lista original los valores que aparecen en otra lista
def eliminar_valores(lista: List[int], a_eliminar: List[int]) -> None:

    """ Eliminar de la lista original todos los valores que estén en la lista a_eliminar
    
    Pre: ambas listas deben estar definidas

    Post: la lista original queda modificada, sin contener los valores de a_eliminar

    """

    assert isinstance(lista, list), "El primer parámetro debe ser una lista"
    assert isinstance(a_eliminar, list), "El segundo parámetro debe ser una lista"

    for valor in lista[:]:
        if valor in a_eliminar:
            lista.remove(valor)

# Programa principal
def main() -> None:

    """ Programa nucleo

    Pre: ninguna

    Post: muestra el resultado de la funcion por pantalla

    """

    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valores_a_eliminar = [2, 4, 6, 8]

    print(f"Lista original: {lista_original}")
    print(f"Valores a eliminar: {valores_a_eliminar}")

    eliminar_valores(lista_original, valores_a_eliminar)

    print(f"Lista resultante: {lista_original}")


if __name__ == "__main__":
    main()