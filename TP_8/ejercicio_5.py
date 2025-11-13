# Función que calcula si dos vectores son ortogonales
def son_ortogonales(v1: tuple[float, float], v2: tuple[float, float]) -> bool:
    """Determinación de ortogonalidad entre dos vectores

    Pre: recibe dos tuplas (v1 y v2) representando los vectores en el plano (x, y)

    Post: devuelve True si los vectores son ortogonales, devuelve False si no lo son

    """

    assert isinstance(v1, tuple) and isinstance(
        v2, tuple
    ), "Los vectores deben ser tuplas."
    assert len(v1) == 2 and len(v2) == 2, "Cada vector debe tener dos componentes."

    try:
        for valor in (*v1, *v2):
            if not isinstance(valor, (int, float)):
                raise ValueError("Los componentes deben ser números reales.")

        producto_escalar = v1[0] * v2[0] + v1[1] * v2[1]
        return producto_escalar == 0

    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception:
        print("Error inesperado al verificar los vectores.")
        return False
    finally:
        pass


# Función auxiliar para ingresar un vector
def ingresar_vector(numero: int) -> tuple[float, float]:
    """Ingreso de un vector en el plano

    Pre: recibe un número entero indicando el orden del vector

    Post: devuelve una tupla (x, y) con los componentes del vector ingresado

    """

    try:
        print(f"\nVector {numero}:")
        x = float(input("  Ingrese la componente x: "))
        y = float(input("  Ingrese la componente y: "))
        return (x, y)
    except ValueError:
        print("Error: debe ingresar números reales.")
        return ()
    except Exception:
        print("Error inesperado al ingresar el vector.")
        return ()
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: permite ingresar dos vectores y muestra si son ortogonales o no

    """
    print("--- Vectores Ortogonales ---")

    try:
        v1 = ingresar_vector(1)
        v2 = ingresar_vector(2)

        if not v1 or not v2:
            print("No se pudieron ingresar correctamente los vectores.")
            return

        if son_ortogonales(v1, v2):
            print(f"Los vectores {v1} y {v2} son ortogonales")
        else:
            print(f"Los vectores {v1} y {v2} no son ortogonales")

    except Exception:
        print("Error inesperado en el programa principal.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
