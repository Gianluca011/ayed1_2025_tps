import string


def ordenar_por_longitud(cadena: str) -> str:
    """Ordena las palabras de una cadena según su longitud

    Pre: cadena es una cadena con palabras separadas por uno o más espacios

    Post: devuelve una nueva cadena con las palabras ordenadas por longitud

    """

    assert isinstance(cadena, str), "El parámetro debe ser de tipo str"

    try:
        # Quitar espacios extra y dividir la cadena
        palabras = cadena.split()

        # Función auxiliar para medir la longitud sin signos
        def longitud_sin_puntuacion(palabra: str) -> int:
            return len("".join([c for c in palabra if c not in string.punctuation]))

        # Ordenar las palabras usando la función auxiliar
        palabras_ordenadas = sorted(palabras, key=longitud_sin_puntuacion)

        # Unirlas de nuevo en una cadena separada por un espacio
        return " ".join(palabras_ordenadas)

    except Exception as e:
        print("Ocurrió un error al ordenar las palabras:", e)
        return ""
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: ejecuta una prueba de ordenamiento de palabras y muestra el resultado por pantalla

    """

    texto = "Hola, este   es un ejemplo sencillo!"
    print("Texto original:", texto)

    resultado = ordenar_por_longitud(texto)
    print("Resultado ordenado:", resultado)


if __name__ == "__main__":
    main()
