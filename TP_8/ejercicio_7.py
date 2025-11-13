# Función para eliminar valores del conjunto
def eliminar_valores(conjunto: set[int]) -> None:
    """Eliminación interactiva de elementos en un conjunto

    Pre: recibe un conjunto con números enteros entre 0 y 9

    Post: elimina los valores ingresados mostrando el conjunto
            actualizado luego de cada eliminación

    """

    assert isinstance(conjunto, set), "El parámetro debe ser un conjunto."

    while True:
        try:
            valor = int(input("Ingrese un número a eliminar (-1 para finalizar): "))

            if valor == -1:
                print("Finalizando proceso...")
                break

            # Intenta eliminar el valor del conjunto
            conjunto.remove(valor)
            print(f"Elemento {valor} eliminado correctamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except KeyError:
            print(f"Error: El elemento {valor} no se encuentra en el conjunto.")
        finally:
            print(f"Conjunto actual: {conjunto}\n")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: crea un conjunto con los números del 0 al 9

    """

    print("--- Conjunto de números (0 a 9) ---")

    # Crear el conjunto inicial
    numeros = set(range(10))
    print(f"Conjunto inicial: {numeros}\n")

    try:
        eliminar_valores(numeros)
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
