# Para eliminar signos de puntuación
import string


# Función que procesa una frase y elimina palabras repetidas
def procesar_frase(frase: str) -> list[str]:
    """Eliminación de palabras repetidas y orden por longitud

    Pre: recibe una cadena de texto ingresada por el usuario

    Post: devuelve una lista con las palabras únicas

    """

    assert isinstance(frase, str), "La frase debe ser una cadena de caracteres."

    try:
        frase = frase.lower()

        # Elimina signos de puntuación usando translate
        frase_sin_puntuacion = frase.translate(
            str.maketrans("", "", string.punctuation)
        )

        palabras = frase_sin_puntuacion.split()

        conjunto_palabras = set(palabras)

        # Ordena las palabras por longitud
        ordenadas = sorted(conjunto_palabras, key=len)

        return ordenadas

    except Exception as e:
        print(f"Error al procesar la frase: {e}")
        return []
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: solicita una frase, elimina las palabras repetidas
            y muestra las palabras únicas ordenadas por longitud
    """
    print("--- Procesamiento de Frases ---")

    try:
        frase = input("Ingrese una frase: ")
        resultado = procesar_frase(frase)

        if resultado:
            print("\nPalabras únicas ordenadas por longitud:")
            print(resultado)
        else:
            print("\nNo se pudo procesar la frase correctamente.")

    except Exception:
        print("Error inesperado en el programa principal.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
