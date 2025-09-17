# Esta función intercala los elementos de una lista en otra, modificando la primera
def intercalar_listas(lista1: list, lista2: list):

    """ Intercala los elementos de lista2 en lista1, modificando lista1 en su lugar
    
    Pre: lista1 y lista2 son listas de cualquier tipo de datos

    Post: lista1 es modificada para incluir los elementos de lista2 intercalados

    """

    # Se itera sobre la segunda lista para insertar cada elemento en la primera
    for i in range(len(lista2)):
        posicion = i * 2 + 1
        lista1[posicion:posicion] = [lista2[i]]

# Programa principal
def main():

    """ Programa nucleo
    
    Pre: ninguna

    Post: muestra por pantalla los resultados de las pruebas

    """

    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    print(f"Lista 1 original: {lista1}")
    print(f"Lista 2 a intercalar: {lista2}")
    
    intercalar_listas(lista1, lista2)
    
    print(f"Lista 1 después de intercalar: {lista1}")
    assert lista1 == [8, 5, 1, 9, 3, 7], "Error en el caso de prueba 1"

    lista3 = [10, 20]
    lista4 = [30, 40, 50, 60]
    print("\n---")
    print(f"Lista 3 original: {lista3}")
    print(f"Lista 4 a intercalar: {lista4}")
    
    intercalar_listas(lista3, lista4)
    
    print(f"Lista 3 después de intercalar: {lista3}")
    assert lista3 == [10, 30, 20, 40, 50, 60], "Error en el caso de prueba 2"

if __name__ == "__main__":
    main()