# Convierte un número entero entre 1 y 3999 a número romano
def entero_a_romano(numero: int) -> str:
    """Convierte un número entero a número romano

    Pre: numero es un entero entre 1 y 3999 inclusive

    Post: devuelve una cadena con el número romano correspondiente

    """

    assert isinstance(numero, int), "El parámetro debe ser un número entero"
    assert 0 < numero <= 3999, "El número debe estar entre 1 y 3999"

    valores: list[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos: list[str] = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]

    resultado: str = ""
    i: int = 0

    while numero > 0:
        if numero >= valores[i]:
            numero -= valores[i]
            resultado += simbolos[i]
        else:
            i += 1

    return resultado


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita un número entero al usuario

    Post: muestra su equivalente romano

    """

    try:
        numero: int = int(input("Ingrese un número entre 1 y 3999: "))
        romano: str = entero_a_romano(numero)
        print(f"El número romano equivalente es: {romano}")
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
