# Funcion para concatenar numeros
def concatenar_numeros(a: int, b: int) -> int:
    """ Concatena a y b
    
    Pre: a y b tienen que ser numeros enteros positivos

    Post: devuelve un numero entero que resulta de concatenar a y b
          
    """
    btemp = b
    multiplicador = 1
    
    # Calcula cuantos dígitos tiene b para desplazar a
    while btemp > 0:
        multiplicador *= 10
        btemp //= 10
    
    # Concatena a y b
    resultado = a * multiplicador + b
    return resultado

def main():
    """ Programa nucleo
    
    Pre: recibe dos numeros enteros positivos

    Post: solicita al usuario dos números enteros positivos y muestra en pantalla
    el número resultante de concatenarlos

    """

    print("=== Concatenador de números ===")
    
    # Pide al usuario los números
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    # Concatena los numeros y muestra el resultado
    resultado = concatenar_numeros(num1, num2)
    print("Número concatenado:", resultado)

if __name__ == "__main__":
    main()