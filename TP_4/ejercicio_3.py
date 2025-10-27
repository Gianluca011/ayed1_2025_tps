# Separa los dígitos en posiciones impares y pares de una clave maestra
def obtener_claves(clave_maestra: int) -> tuple[int, int]:
    """Separa una clave maestra en dos claves según las posiciones de los dígitos

    Pre: clave_maestra es un número entero positivo

    Post: devuelve una tupla, donde: clave1 contiene los dígitos en posiciones impares y clave2 contiene los dígitos en posiciones pares

    """

    assert isinstance(clave_maestra, int), "La clave maestra debe ser un número entero"
    assert clave_maestra > 0, "La clave maestra debe ser positiva"

    clave_str: str = str(clave_maestra)
    clave1: str = ""
    clave2: str = ""

    for i in range(len(clave_str)):
        if i % 2 == 0:
            clave1 += clave_str[i]
        else:
            clave2 += clave_str[i]

    clave1_int: int = int(clave1) if clave1 else 0
    clave2_int: int = int(clave2) if clave2 else 0

    return clave1_int, clave2_int


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita una clave maestra entera

    Post: muestra las claves separadas

    """

    try:
        clave_maestra: int = int(input("Ingrese la clave maestra (entero positivo): "))
        clave1, clave2 = obtener_claves(clave_maestra)
        print(f"Clave 1 (posiciones impares): {clave1}")
        print(f"Clave 2 (posiciones pares): {clave2}")
    except ValueError:
        print("Error: debe ingresar un número entero.")
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
