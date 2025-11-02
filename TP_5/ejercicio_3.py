# Esta función recibe el número de un mes y devuelve su nombre en texto
def obtener_nombre_mes(num_mes: int) -> str:
    """Devuelve el nombre del mes según su número

    Pre: num_mes es un entero entre 1 y 12

    Post: devuelve el nombre del mes correspondiente o una cadena vacía si el número es inválido

    """

    assert isinstance(num_mes, int), "El número de mes debe ser un entero."

    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    try:
        if num_mes < 1 or num_mes > 12:
            raise ValueError("Número de mes fuera de rango (1-12).")
        return meses[num_mes - 1]
    except ValueError as e:
        print(f"Error: {e}")
        return ""
    finally:
        print("Ejecución finalizada.\n")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: el usuario ingresa un número entero entre 1 y 12

    Post: muestra el nombre del mes o un mensaje de error si el número es inválido

    """

    try:
        num = int(input("Ingrese el número del mes (1-12): "))
        nombre = obtener_nombre_mes(num)

        if nombre != "":
            print(f"El mes correspondiente es: {nombre}")
        else:
            print("Número de mes inválido.")
    except ValueError:
        print("Error: debe ingresar un número entero.")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
