import math


def calcular_raiz(numero: float) -> float:
    """Calcula la raíz cuadrada de un número dado.

    Pre: numero debe ser un valor numérico mayor o igual a 0

    Post: devuelve la raíz cuadrada del número si es válido, o lanza una excepción si es negativo

    """

    assert isinstance(numero, (int, float)), "El valor debe ser numérico."
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra en pantalla la raíz cuadrada si el número es válido, o un mensaje de error en caso contrario

    """

    try:
        entrada = input("Ingrese un número para calcular su raíz cuadrada: ")
        numero = float(entrada)
        resultado = calcular_raiz(numero)
        print(f"La raíz cuadrada de {numero} es {resultado:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except AssertionError as e:
        print(f"Error de tipo: {e}")
    finally:
        print("--- Programa finalizado ---")


if __name__ == "__main__":
    main()
