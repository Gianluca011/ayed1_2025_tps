# Comprueba si la cadena es capicúa
def es_capicua(cadena: str) -> bool:
    """Determina si una cadena es capicúa

    Pre: cadena es una cadena de caracteres no vacía

    Post: devuelve True si la cadena es capicúa, False en caso contrario

    """

    assert isinstance(cadena, str), "El parámetro debe ser una cadena"
    assert len(cadena) > 0, "La cadena no puede estar vacía"

    i: int = 0
    j: int = len(cadena) - 1

    while i < j:
        if cadena[i] != cadena[j]:
            return False
        i += 1
        j -= 1

    return True


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita una cadena al usuario

    Post: informa si es capicúa o no

    """

    try:
        cadena: str = input("Ingrese una cadena: ").strip()
        resultado: bool = es_capicua(cadena)
        if resultado:
            print(f"La cadena '{cadena}' es capicúa.")
        else:
            print(f"La cadena '{cadena}' no es capicúa.")
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
