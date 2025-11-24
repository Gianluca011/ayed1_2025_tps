# La función convierte recursivamente un número binario a su equivalente decimal
def binario_a_decimal(b: int) -> int:
    """Conversión de binario a decimal de manera recursiva

    Pre: b es un número entero compuesto únicamente por dígitos 0 y 1

    Post: devuelve el equivalente decimal del número binario recibido

    """

    try:
        if not isinstance(b, int):
            raise TypeError("El valor debe ser un entero.")

        if b < 0:
            raise ValueError("El número binario no puede ser negativo.")

        if b not in (0, 1) and b % 10 not in (0, 1):
            raise ValueError("El número binario debe contener solo dígitos 0 y 1.")

        if b in (0, 1):
            return b

        ultimo = b % 10
        resto = b // 10

        if ultimo not in (0, 1):
            raise ValueError("El número binario contiene dígitos inválidos.")

        return ultimo + 2 * binario_a_decimal(resto)

    except Exception as e:
        print(f"Error: {e}")
        raise


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: ejecuta un ciclo para ingresar números binarios y mostrarlos en decimal

    """

    while True:
        try:
            entrada = input("Ingresá un número binario (o 'salir' para terminar): ")
            if entrada.lower() == "salir":
                print("Programa finalizado.")
                break

            numero = int(entrada)
            resultado = binario_a_decimal(numero)
            print(f"Decimal: {resultado}")

        except ValueError:
            print("Entrada inválida. Debés ingresar solo dígitos 0 y 1.")


if __name__ == "__main__":
    main()
