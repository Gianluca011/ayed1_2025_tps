# Con rebanadas
def eliminar_subcadena_rebanadas(cadena: str, inicio: int, cantidad: int) -> str:
    """Elimina una subcadena utilizando rebanadas

    Pre: cadena es una cadena no vacía, inicio y cantidad son enteros válidos

    Post: devuelve una nueva cadena sin los cantidad caracteres a partir de la posición inicio

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(inicio, int) and isinstance(
        cantidad, int
    ), "Los parámetros deben ser enteros"
    assert inicio >= 0 and cantidad >= 0, "Los valores deben ser no negativos"

    try:
        resultado = cadena[:inicio] + cadena[inicio + cantidad :]
        return resultado
    except Exception as e:
        print("Ocurrió un error al eliminar la subcadena:", e)
        return ""
    finally:
        pass


# Sin usar rebanadas
def eliminar_subcadena_manual(cadena: str, inicio: int, cantidad: int) -> str:
    """Elimina una subcadena sin utilizar rebanadas

    Pre: cadena es una cadena no vacía, inicio y cantidad son enteros válidos

    Post: devuelve una nueva cadena construida carácter por carácter, omitiendo los cantidad caracteres a partir de la posición inicio

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(inicio, int) and isinstance(
        cantidad, int
    ), "Los parámetros deben ser enteros"
    assert inicio >= 0 and cantidad >= 0, "Los valores deben ser no negativos"

    try:
        resultado = "".join(
            [
                cadena[i]
                for i in range(len(cadena))
                if not (inicio <= i < inicio + cantidad)
            ]
        )
        return resultado
    except Exception as e:
        print("Ocurrió un error al eliminar la subcadena:", e)
        return ""
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: muestra los resultados por pantalla

    """

    texto = "El número de teléfono es 4356-7890"
    inicio = 25
    cantidad = 9

    print("Texto original:", texto)
    print("\n--- Usando rebanadas ---")
    resultado1 = eliminar_subcadena_rebanadas(texto, inicio, cantidad)
    print("Resultado:", resultado1)

    print("\n--- Sin usar rebanadas ---")
    resultado2 = eliminar_subcadena_manual(texto, inicio, cantidad)
    print("Resultado:", resultado2)


if __name__ == "__main__":
    main()
