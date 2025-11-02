# Recibe dos cadenas con números reales, los convierte a float, los suma y devuelve el resultado
def sumar_reales(cad1: str, cad2: str) -> float:
    """Suma de números reales expresados en cadenas

    Pre: cad1 y cad2 son cadenas que representan números reales

    Post: devuelve la suma de ambos como número real o -1 si alguna cadena no es válida

    """

    assert isinstance(cad1, str) and isinstance(
        cad2, str
    ), "Los parámetros deben ser cadenas."

    try:
        num1 = float(cad1)
        num2 = float(cad2)
        resultado = num1 + num2
    except ValueError:
        print("Error: una de las cadenas no contiene un número real válido.")
        return -1
    finally:
        print("Operación finalizada.\n")

    return resultado


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: el usuario ingresa dos cadenas representando números reales

    Post: muestra la suma o un mensaje de error si alguna cadena no es válida

    """
    try:
        cad1 = input("Ingrese el primer número real: ")
        cad2 = input("Ingrese el segundo número real: ")
        resultado = sumar_reales(cad1, cad2)

        if resultado != -1:
            print(f"La suma de ambos números es: {resultado}")
        else:
            print("No se pudo realizar la suma por datos inválidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
