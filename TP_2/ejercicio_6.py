# Función que normaliza una lista de números enteros.
def normalizar(numeros: list[int]) -> list[float]:

    """ Normaliza una lista de números enteros para que la suma de sus elementos sea 1.0
    
    Pre: numeros es una lista de números enteros, la suma de los elementos no puede ser 0

    Post: devuelve una nueva lista con los elementos normalizados

    """

    # Se calcula la suma total de todos los elementos de la lista
    suma_total = sum(numeros)

    # Se verifica que la suma total no sea cero para evitar la división por cero
    if suma_total == 0:
        return [0.0] * len(numeros)

    # Se utiliza una lista por comprensión para crear la nueva lista normalizada
    return [num / suma_total for num in numeros]

# Programa principal
def main():

    """ Programa nucleo

    Pre: ninguna

    Post: muestra el resultado de la funcion por pantalla

    """

    lista1 = [1, 1, 2]
    lista1_normalizada = normalizar(lista1)
    print(f"La lista {lista1} normalizada es: {lista1_normalizada}")
    
    lista2 = [10, 20, 30]
    lista2_normalizada = normalizar(lista2)
    print(f"La lista {lista2} normalizada es: {lista2_normalizada}")

    lista3 = [5, -10, 15]
    lista3_normalizada = normalizar(lista3)
    print(f"La lista {lista3} normalizada es: {lista3_normalizada}")

if __name__ == "__main__":
    main()