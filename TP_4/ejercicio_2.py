# Centra una cadena dentro de un ancho fijo de 80 columnas
def centrar_cadena(cadena: str) -> str:
    """Centra una cadena en un espacio de 80 columnas

    Pre: cadena es una cadena de caracteres no vacía

    Post: devuelve la cadena centrada en un ancho total de 80 caracteres

    """

    assert isinstance(cadena, str), "El parámetro debe ser una cadena"
    assert len(cadena) > 0, "La cadena no puede estar vacía"

    ancho_total: int = 80
    espacios_izquierda: int = (ancho_total - len(cadena)) // 2

    if espacios_izquierda < 0:
        return cadena

    return " " * espacios_izquierda + cadena


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita una cadena al usuario

    Post: la muestra centrada en 80 columnas

    """

    try:
        cadena: str = input("Ingrese una cadena: ").strip()
        centrada: str = centrar_cadena(cadena)
        print(centrada)
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
