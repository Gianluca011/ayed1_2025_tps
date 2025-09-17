# Esta función genera una lista de múltiplos de 7 que no son múltiplos de 5
def generar_lista_multiplos(inicio: int, fin: int) -> list[int]:

    """ Genera una lista de múltiplos de 7 que no son múltiplos de 5, en un rango dado
    
    Pre: inicio y fin son números enteros

    Post: Devuelve una lista de enteros que cumplen con las condiciones

    """

    return [
        numero
        for numero in range(min(inicio, fin), max(inicio, fin) + 1)
        if numero % 7 == 0 and numero % 5 != 0
    ]

# Programa principal
def main():

    """ Programa nucleo
    
    Pre: recibe dos numeros enteros positivos, a y b

    Post: muestra por pantalla la lista de números generada

    """

    try:
        a = int(input("Ingrese el número de inicio (A): "))
        b = int(input("Ingrese el número de fin (B): "))
        
        lista_resultante = generar_lista_multiplos(a, b)
        
        print(f"\nLa lista de múltiplos de 7 que no son múltiplos de 5 entre {a} y {b} es:")
        print(lista_resultante)

    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()