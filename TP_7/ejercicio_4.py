# La función calcula el producto de dos enteros usando únicamente sumas sucesivas
def producto_sumas_sucesivas(a: int, b: int) -> int:
    """Producto mediante sumas sucesivas

    Pre: a y b son números enteros

    Post: devuelve el producto entre a y b utilizando sumas sucesivas

    """

    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Ambos valores deben ser enteros.")

        if b < 0:
            return -producto_sumas_sucesivas(a, -b)

        if b == 0:
            return 0

        return a + producto_sumas_sucesivas(a, b - 1)

    except Exception as e:
        print(f"Error: {e}")
        raise


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: ejecuta un ciclo que permite ingresar dos enteros y muestra su producto por sumas sucesivas

    """

    while True:
        try:
            entrada = input(
                "Ingresá dos enteros separados por espacio (o 'salir' para terminar): "
            )
            if entrada.lower() == "salir":
                print("Programa finalizado.")
                break

            partes = entrada.split()
            if len(partes) != 2:
                print("Debés ingresar exactamente dos números.")
                continue

            a, b = int(partes[0]), int(partes[1])
            print(f"Resultado: {producto_sumas_sucesivas(a, b)}")

        except ValueError:
            print("Entrada inválida. Debés ingresar números enteros.")


if __name__ == "__main__":
    main()
