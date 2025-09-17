import random

# Cargar lista con números al azar de cuatro dígitos
def cargar_lista() -> list[int]:

    """ Generar lista con números al azar de cuatro dígitos

    Pre: ninguna

    Post: devuelve una lista de enteros entre 1000 y 9999, con cantidad de elementos entre 10 y 99

    """

    cantidad: int = random.randint(10, 99)
    lista: list[int] = [random.randint(1000, 9999) for _ in range(cantidad)]
    return lista


# Producto de todos los elementos de la lista
def producto_lista(lista: list[int]) -> int:

    """ Calcular el producto de los elementos de una lista

    Pre: lista con numeros enteros

    Post: devuelve el producto acumulado de todos los elementos de la lista

    """

    producto: int = 1
    for num in lista:
        producto *= num
    return producto


# Eliminar todas las apariciones de un valor
def eliminar_valor(lista: list[int], valor: int) -> None:

    """ Eliminar todas las apariciones de un valor en la lista

    Pre: lista con al menos un número entero

    Post: la lista queda modificada, sin ninguna aparición del valor indicado

    """

    i: int = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1


# Verificar si una lista es capicúa
def es_capicua(lista: list[int]) -> bool:

    """ Verificar si una lista es capicúa.

    Pre: ninguna

    Post: devuelve True si la lista es capicúa, False en caso contrario

    """

    n: int = len(lista)
    for i in range(n // 2):
        if lista[i] != lista[n - 1 - i]:
            return False
    return True

# Programa para ejecutar la función
def main():

    """ Programa nucleo

    Pre: ninguna

    Post: muestra el resultado de las funciones por pantalla
    
    """

    lista = cargar_lista()
    print("Lista cargada:", lista)
    assert all(1000 <= x <= 9999 for x in lista)

    prod = producto_lista(lista)
    print("Producto de la lista:", prod)
    assert isinstance(prod, int)

    if lista:
        valor = lista[0]
        eliminar_valor(lista, valor)
        print(f"Lista sin el valor {valor}:", lista)
        assert valor not in lista

    ejemplo1 = [50, 17, 91, 17, 50]
    ejemplo2 = [1, 2, 3, 4]
    print("Ejemplo capicúa:", ejemplo1, "->", es_capicua(ejemplo1))
    print("Ejemplo no capicúa:", ejemplo2, "->", es_capicua(ejemplo2))
    assert es_capicua(ejemplo1) is True
    assert es_capicua(ejemplo2) is False

if __name__ == "__main__":
    main()