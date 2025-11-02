# Solicita al usuario un número natural, controlando errores
def ingresar_numero_natural() -> int:
    """Pide al usuario que ingrese un número natural y controla errores

    Pre: el usuario debe ingresar un valor a través del teclado

    Post: devuelve un número entero mayor que cero si la entrada es válida

    """

    while True:
        try:
            valor = input("Ingrese un número natural: ")
            assert valor != "", "No se puede ingresar una cadena vacía."

            numero = int(valor)  # Puede lanzar ValueError si no es un número
            assert numero > 0, "El número debe ser mayor que 0."

        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")
        except AssertionError as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Número ingresado correctamente.")
            return numero
        finally:
            print("--- Fin del intento de ingreso ---")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: solicita un número al usuario

    Post: muestra el número válido ingresado por el usuario

    """

    numero: int = ingresar_numero_natural()
    print(f"\nEl número ingresado es: {numero}")


if __name__ == "__main__":
    main()
