import random


def generar_numero() -> int:
    """Genera y devuelve un número aleatorio entre 1 y 500"""
    return random.randint(1, 500)


def adivinar_numero(objetivo: int) -> None:
    """Permite al usuario intentar adivinar el número generado por el programa

    Pre: objetivo debe ser un número entero entre 1 y 500

    Post: informa la cantidad de intentos que tomó adivinarlo

    """

    assert isinstance(objetivo, int), "El número objetivo debe ser un entero."
    assert 1 <= objetivo <= 500, "El número objetivo debe estar entre 1 y 500."

    intentos = 0
    while True:
        try:
            intento = int(input("Adiviná el número entre 1 y 500: "))
            intentos += 1

            if intento < objetivo:
                print("El número secreto es mayor.")
            elif intento > objetivo:
                print("El número secreto es menor.")
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                break

        except ValueError:
            intentos += 1
            print("Entrada inválida. Debés ingresar un número entero.")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: juega con el usuario a adivinar un número

    """

    print("--- Bienvenido al juego de adivinar el número ---")
    numero_secreto = generar_numero()
    adivinar_numero(numero_secreto)


if __name__ == "__main__":
    main()
