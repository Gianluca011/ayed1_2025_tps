import string
from typing import Dict


# Cuenta las vocales en una sola palabra y devuelve un diccionario con la cantidad de cada una
def contarvocales(palabra: str) -> Dict[str, int]:
    """Contar vocales en una palabra

    Pre: palabra es una cadena

    Post: devuelve un diccionario con las vocales encontradas como claves y su cantidad como valores

    """

    assert isinstance(palabra, str), "El parámetro debe ser una cadena de texto."

    vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")

    try:
        contador: Dict[str, int] = {v: 0 for v in vocales}

        palabra_l = palabra.lower()

        for ch in palabra_l:
            if ch in contador:
                contador[ch] += 1

        resultado = {v: c for v, c in contador.items() if c > 0}
        return resultado

    except Exception as e:
        print(f"Error al contar vocales en '{palabra}': {e}")
        return {}
    finally:
        pass


# Limpia una palabra de signos de puntuación y espacios
def limpiar_palabra(p: str) -> str:
    """Limpiar palabra

    Pre: p es una cadena que puede contener signos de puntuación

    Post: devuelve la palabra sin signos de puntuación y sin espacios

    """

    assert isinstance(p, str), "El parámetro debe ser una cadena."
    try:
        return p.strip().strip(string.punctuation)
    except Exception:
        return p.strip()
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: para cada palabra de la frase muestra la palabra original y un diccionario con las vocales halladas
    """
    print("--- Contar vocales por palabra ---")

    try:
        frase = input("Ingrese una frase: ").strip()
        assert frase != "", "No ingresó ninguna frase."

        palabras = [
            limpiar_palabra(w) for w in frase.split() if limpiar_palabra(w) != ""
        ]

        if not palabras:
            print("No se encontraron palabras válidas en la frase.")
            return

        print("Resultados por palabra:")
        for palabra in palabras:
            try:
                resultado = contarvocales(palabra)
                total_vocales = sum(resultado.values())
                print(f"- {palabra} → {resultado} (total: {total_vocales})")
            except Exception as e:
                print(f"Error procesando la palabra '{palabra}': {e}")

    except AssertionError as ae:
        print(f"Error de entrada: {ae}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
