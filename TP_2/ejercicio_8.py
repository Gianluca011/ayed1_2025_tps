# Esta función crea una lista de números impares usando una lista por comprensión
def crear_lista_impares() -> list[int]:

    """ Crea una lista con todos los números impares entre 100 y 200
    
    Pre: ninguna

    Post: devuelve una lista de enteros que son impares y están en el rango [100, 200]

    """

    return [numero for numero in range(100, 201) if numero % 2 != 0]

# Programa principal
def main():

    """ Programa nucleo
    
    Pre: ninguna

    Post: imprime la lista de números impares generada

    """

    impares = crear_lista_impares()
    print(f"Los números impares entre 100 y 200 son: {impares}")

if __name__ == "__main__":
    main()