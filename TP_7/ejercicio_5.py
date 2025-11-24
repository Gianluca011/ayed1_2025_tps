# Función recursiva para calcular el resto mediante restas sucesivas
def calcular_resto_recursivo(dividendo: int, divisor: int) -> int:
    """Calcular resto

    Pre: dividendo debe ser un entero >= 0 y divisor un entero > 0

    Post: devuelve el valor entero del resto de la división

    """

    if dividendo < divisor:
        return dividendo

    return calcular_resto_recursivo(dividendo - divisor, divisor)


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: ejecuta la interacción con el usuario y muestra el resultado

    """

    print("Calculadora de resto")

    while True:
        try:
            entrada_dividendo = input("Ingrese el dividendo (o 'salir' para salir): ")
            if entrada_dividendo.lower() == "salir":
                print("Programa finalizado.")
                break

            dividendo = int(entrada_dividendo)
            divisor = int(input("Ingrese el divisor: "))

            if dividendo < 0 or divisor <= 0:
                raise ValueError(
                    "El dividendo debe ser positivo y el divisor mayor a 0."
                )

            resto = calcular_resto_recursivo(dividendo, divisor)

            print(f"El resto de dividir {dividendo} por {divisor} es: {resto}")

        except ValueError:
            print(f"Entrada inválida.")


if __name__ == "__main__":
    main()
