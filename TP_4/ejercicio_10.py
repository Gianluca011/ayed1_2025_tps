def reemplazar_palabra(
    cadena: str, palabra_original: str, palabra_nueva: str
) -> tuple[str, int]:
    """Reemplaza todas las apariciones de una palabra completa por otra

    Pre: cadena, palabra_original y palabra_nueva son cadenas no vacías

    Post: devuelve una tupla con la cadena modificada y la cantidad de reemplazos realizados

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(palabra_original, str), "La palabra original debe ser de tipo str"
    assert isinstance(palabra_nueva, str), "La palabra nueva debe ser de tipo str"
    assert palabra_original != "", "La palabra original no puede ser vacía"

    try:
        # Dividir la cadena en palabras
        palabras = cadena.split()

        # Contador de reemplazos
        reemplazos = 0

        # Recorremos las palabras y reemplazamos solo si coincide exactamente
        nuevas_palabras = []
        for palabra in palabras:
            if palabra == palabra_original:
                nuevas_palabras.append(palabra_nueva)
                reemplazos += 1
            else:
                nuevas_palabras.append(palabra)

        cadena_modificada = " ".join(nuevas_palabras)

        return cadena_modificada, reemplazos

    except Exception as e:
        print("Ocurrió un error al reemplazar palabras:", e)
        return "", 0
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: ejecuta una prueba de reemplazo de palabras y muestra los resultados por pantalla

    """

    texto = "El auto azul está al lado del auto rojo"
    original = "auto"
    nueva = "coche"

    print("Texto original:", texto)
    print(f"Palabra a reemplazar: '{original}' por '{nueva}'")

    cadena_modificada, cantidad = reemplazar_palabra(texto, original, nueva)
    print("\nCadena modificada:", cadena_modificada)
    print("Cantidad de reemplazos realizados:", cantidad)


if __name__ == "__main__":
    main()
