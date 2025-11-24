# La función calcula recursivamente la suma de los primeros n números naturales
def suma_n(n: int) -> int:
    """Suma recursiva de los n primeros números naturales

    Pre: n es un entero mayor o igual a 0

    Post: devuelve la suma de los primeros n números naturales

    """

    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")
        if n < 0:
            raise ValueError("n debe ser un entero no negativo.")

        if n == 0:
            return 0

        return n + suma_n(n - 1)

    except Exception as e:
        print(f"Error: {e}")
        raise


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: ejecuta un ciclo que permite ingresar un número n y muestra la suma correspondiente

    """

    while True:
        try:
            entrada = input("Ingresá un número natural n (o 'salir' para terminar): ")
            if entrada.lower() == "salir":
                print("Programa finalizado.")
                break

            n = int(entrada)
            print(f"La suma de los primeros {n} números naturales es: {suma_n(n)}")

        except ValueError:
            print(
                "Entrada inválida. Debés ingresar un número entero que no sea negativo."
            )


if __name__ == "__main__":
    main()
