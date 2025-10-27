# Versión a: usa ciclos normales para filtrar palabras
def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """Devuelve una cadena con las palabras que tienen n o más caracteres

    Pre: frase es una cadena no vacía, n es un entero mayor o igual a 1

    Post: devuelve otra cadena con las palabras de longitud n o mayor

    """

    assert isinstance(frase, str), "La frase debe ser una cadena"
    assert isinstance(n, int), "N debe ser un número entero"
    assert n > 0, "N debe ser mayor que 0"

    palabras: list[str] = frase.split()
    resultado: list[str] = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return " ".join(resultado)


# Versión b: usa listas por comprensión
def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """Devuelve una cadena con las palabras que tienen n o más caracteres

    Pre: frase es una cadena no vacía, n es un entero mayor o igual a 1

    Post: devuelve otra cadena con las palabras de longitud N o mayor

    """

    assert isinstance(frase, str), "La frase debe ser una cadena"
    assert isinstance(n, int), "N debe ser un número entero"
    assert n > 0, "N debe ser mayor que 0"

    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


# Versión c: usa la función filter()
def filtrar_palabras_filter(frase: str, n: int) -> str:
    """Devuelve una cadena con las palabras que tienen N o más caracteres

    Pre: frase es una cadena no vacía, n es un entero mayor o igual a 1

    Post: devuelve otra cadena con las palabras de longitud N o mayor

    """

    assert isinstance(frase, str), "La frase debe ser una cadena"
    assert isinstance(n, int), "N debe ser un número entero"
    assert n > 0, "N debe ser mayor que 0"

    # filter() necesita una función que devuelva True/False para cada palabra
    def tiene_longitud_suficiente(palabra: str) -> bool:
        return len(palabra) >= n

    return " ".join(filter(tiene_longitud_suficiente, frase.split()))


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita una frase y un número n

    Post: muestra el resultado con las tres versiones

    """

    try:
        frase: str = input("Ingrese una frase: ").strip()
        n: int = int(input("Ingrese la longitud mínima de las palabras: "))

        print("\n--- Resultados ---")
        print("a) Con ciclos normales:       ", filtrar_palabras_ciclos(frase, n))
        print("b) Con listas por comprensión:", filtrar_palabras_comprension(frase, n))
        print("c) Con filter():              ", filtrar_palabras_filter(frase, n))
    except ValueError:
        print("Error: debe ingresar un número entero para N.")
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
