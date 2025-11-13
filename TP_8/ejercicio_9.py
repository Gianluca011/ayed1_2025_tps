# Función para generar la tabla de multiplicar
def generar_tabla_multiplicar(n: int) -> dict[int, int]:
    """Generar tabla de multiplicar

    Pre: n debe ser un número entero

    Post: devuelve un diccionario donde las claves van del 1 al 12,
            y los valores son el resultado de multiplicar cada clave por n
    """
    assert isinstance(n, int), "El parámetro debe ser un número entero."

    tabla = {i: n * i for i in range(1, 13)}
    return tabla


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: solicita al usuario un número entero n, genera y muestra en pantalla
            la tabla de multiplicar de n del 1 al 12

    """

    print("--- Tabla de multiplicar con diccionario ---")

    try:
        n = int(input("Ingrese un número entero: "))
        tabla = generar_tabla_multiplicar(n)

        print(f"\nTabla de multiplicar del {n}:\n")
        for multiplicador, resultado in tabla.items():
            print(f"{n} × {multiplicador:2} = {resultado}")

    except ValueError:
        print("Error: debe ingresar un número entero.")
    except AssertionError as e:
        print(f"Error: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
