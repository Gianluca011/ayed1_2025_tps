# Verifica si las fichas de dominó encajan
def encajan(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """Verificación de encaje entre fichas de dominó

    Pre: recibe dos tuplas, cada una representando una ficha de dominó

    Post: devuelve True si las fichas encajan o False si no encajan o si los datos son inválidos

    """

    assert isinstance(ficha1, tuple) and isinstance(
        ficha2, tuple
    ), "Las fichas deben ser tuplas."
    assert len(ficha1) == 2 and len(ficha2) == 2, "Cada ficha debe tener dos valores."

    try:
        for valor in (*ficha1, *ficha2):
            if not isinstance(valor, int) or not (0 <= valor <= 6):
                raise ValueError(
                    "Los valores de las fichas deben ser enteros entre 0 y 6."
                )

        return not set(ficha1).isdisjoint(ficha2)

    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception:
        print("Error inesperado al verificar las fichas.")
        return False
    finally:
        pass


# Ingresar fichas
def ingresar_ficha(numero: int) -> tuple[int, int]:
    """Ingreso de una ficha de dominó

    Pre: recibe un número entero indicando el orden de la ficha

    Post: devuelve una tupla de dos enteros representando la ficha ingresada

    """

    try:
        print(f"Ficha {numero}:")
        lado1 = int(input("  Ingrese el primer valor (0-6): "))
        lado2 = int(input("  Ingrese el segundo valor (0-6): "))
        return (lado1, lado2)
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")
        return ()
    except Exception:
        print("Error inesperado al ingresar la ficha.")
        return ()
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: permite ingresar dos fichas de dominó y muestra si encajan o no

    """

    print("--- Fichas de Dominó ---")

    try:
        ficha1 = ingresar_ficha(1)
        ficha2 = ingresar_ficha(2)

        if not ficha1 or not ficha2:
            print("No se pudieron ingresar correctamente las fichas.")
            return

        if encajan(ficha1, ficha2):
            print(f"Las fichas {ficha1} y {ficha2} encajan")
        else:
            print(f"Las fichas {ficha1} y {ficha2} no encajan")
    except Exception:
        print("Error inesperado en el programa principal.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
