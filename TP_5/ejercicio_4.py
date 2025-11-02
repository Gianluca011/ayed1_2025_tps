# Este programa imprime los números del 1 al 100000 y permite interrumpir la ejecución con Ctrl + C
def imprimir_numeros() -> None:
    """Imprime los números del 1 al 100000 con manejo de interrupción por teclado

    Pre: no recibe parámetros

    Post: imprime los números uno por uno hasta que el usuario confirme detener la ejecución

    """

    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        try:
            confirmar = input("\n¿Desea detener el programa? (si/no): ").strip().lower()
            assert confirmar in ("si", "no"), "Debe ingresar 'si' o 'no'."
            if confirmar == "si":
                print("Programa detenido por el usuario.")
                return
            else:
                print("Continuando la ejecución...\n")
                imprimir_numeros()  # Reanuda el ciclo
        except AssertionError as e:
            print(f"Error: {e}. Se continuará la ejecución.\n")
            imprimir_numeros()
    finally:
        print("Ejecución finalizada.\n")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: imprime los números y controla interrupciones por teclado

    """

    imprimir_numeros()


if __name__ == "__main__":
    main()
