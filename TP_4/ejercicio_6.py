# Con rebanadas
def extraer_subcadena_rebanadas(cadena: str, inicio: int, cantidad: int) -> str:
    """Extrae una subcadena utilizando rebanadas

    Pre: cadena es una cadena no vacía, inicio y cantidad son enteros válidos

    Post: devuelve una subcadena de cadena que comienza en inicio y tiene cantidad caracteres

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(inicio, int) and isinstance(
        cantidad, int
    ), "Los parámetros deben ser enteros"
    assert inicio >= 0 and cantidad >= 0, "Los valores deben ser no negativos"

    try:
        subcadena = cadena[inicio : inicio + cantidad]
        return subcadena
    except Exception as e:
        print("Ocurrió un error al extraer la subcadena:", e)
        return ""
    finally:
        pass


# Sin usar rebanadas
def extraer_subcadena_manual(cadena: str, inicio: int, cantidad: int) -> str:
    """Extrae una subcadena sin utilizar rebanadas

    Pre: cadena es una cadena no vacía, inicio y cantidad son enteros válidos

    Post: devuelve una subcadena de cadena construida carácter por carácter desde la posición inicio con cantidad caracteres

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(inicio, int) and isinstance(
        cantidad, int
    ), "Los parámetros deben ser enteros"
    assert inicio >= 0 and cantidad >= 0, "Los valores deben ser no negativos"

    try:
        subcadena = "".join(
            [cadena[i] for i in range(inicio, inicio + cantidad) if i < len(cadena)]
        )
        return subcadena
    except Exception as e:
        print("Ocurrió un error al construir la subcadena:", e)
        return ""
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones que contiene

    """

    texto = "El número de teléfono es 4356-7890"
    inicio = 25
    cantidad = 9

    print("Texto original:", texto)
    print("\n--- Usando rebanadas ---")
    resultado1 = extraer_subcadena_rebanadas(texto, inicio, cantidad)
    print("Subcadena extraída:", resultado1)

    print("\n--- Sin usar rebanadas ---")
    resultado2 = extraer_subcadena_manual(texto, inicio, cantidad)
    print("Subcadena extraída:", resultado2)


if __name__ == "__main__":
    main()
