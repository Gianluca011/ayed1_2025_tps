# Función para generar el diccionario
def generar_diccionario_cuadrados(inicio: int = 1, fin: int = 20) -> dict[int, int]:
    """Generar diccionario con cuadrados de las claves

    Pre: inicio y fin deben ser números enteros (inicio <= fin)

    Post: devuelve un diccionario donde las claves son los números entre inicio y fin (inclusive)
            y los valores son el cuadrado de cada clave

    """

    assert isinstance(inicio, int) and isinstance(
        fin, int
    ), "Los límites deben ser enteros."
    assert inicio <= fin, "El valor inicial debe ser menor o igual al final."

    diccionario = {i: i**2 for i in range(inicio, fin + 1)}
    return diccionario


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: genera y muestra en pantalla un diccionario con números del 1 al 20
            como claves y sus cuadrados como valores

    """

    print("--- Diccionario de cuadrados ---")

    try:
        dicc = generar_diccionario_cuadrados(1, 20)
        print("Diccionario generado correctamente:\n")
        for clave, valor in dicc.items():
            print(f"{clave} → {valor}")
    except AssertionError as e:
        print(f"Error en los parámetros: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
