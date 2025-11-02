# Carga una lista de números enteros
def cargar_lista() -> list[int]:
    """Carga una lista de números enteros ingresados por teclado

    Pre: el usuario debe ingresar números enteros, finalizando con -1

    Post: devuelve una lista con los valores ingresados, sin incluir el -1

    """

    lista = []
    while True:
        try:
            valor = int(input("Ingrese un número entero (-1 para terminar): "))
            if valor == -1:
                break
            lista.append(valor)
        except ValueError:
            print("Error: debe ingresar un número entero.")
    return lista


def buscar_posicion(lista: list[int], valor: int) -> int:
    """Busca la posición de un valor en la lista usando el método index()

    Pre: lista debe ser una lista de enteros y valor un entero

    Post: devuelve la posición del valor si se encuentra, lanza ValueError si no está

    """

    assert isinstance(lista, list), "El primer parámetro debe ser una lista."
    assert all(
        isinstance(x, int) for x in lista
    ), "La lista debe contener solo enteros."
    assert isinstance(valor, int), "El valor buscado debe ser un número entero."
    return lista.index(valor)


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: permite buscar elementos hasta que se detecten 3 errores

    """

    lista = cargar_lista()
    print(f"\nLista cargada: {lista}")

    errores = 0
    while errores < 3:
        try:
            valor = int(input("\nIngrese un número para buscar su posición: "))
            pos = buscar_posicion(lista, valor)
            print(f"El número {valor} se encuentra en la posición {pos}.")
        except ValueError:
            errores += 1
            print(
                f"Error: el número no se encuentra en la lista. ({errores}/3 errores)"
            )
        except AssertionError as e:
            print(f"Error de tipo: {e}")
        finally:
            if errores == 3:
                print("\nSe alcanzó el límite de errores. Programa finalizado.")


if __name__ == "__main__":
    main()
