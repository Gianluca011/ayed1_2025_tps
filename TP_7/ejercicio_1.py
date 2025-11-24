# La función cuenta recursivamente los dígitos de un número entero, manejando casos negativos
def contar_digitos(n: int) -> int:
    """Contar dígitos recursivamente

    Pre: n es un número entero

    Post: devuelve la cantidad de dígitos del número sin utilizar cadenas de caracteres

    """

    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")

        n = abs(n)

        if 0 <= n <= 9:
            return 1

        return 1 + contar_digitos(n // 10)

    except Exception as e:
        print(f"Error: {e}")
        raise


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: ejecuta un ciclo interactivo para pedir números y mostrar la cantidad de dígitos

    """

    while True:
        try:
            valor = int(input("Ingresá un número entero (o escriba 0 para salir): "))
            if valor == 0:
                print("Programa finalizado.")
                break
            print(f"Cantidad de dígitos: {contar_digitos(valor)}")
        except ValueError:
            print("Entrada inválida. Por favor ingresá un número entero.")


if __name__ == "__main__":
    main()
