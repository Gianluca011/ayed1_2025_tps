# Función para obtener el mayor unico
def mayor_unico(a :int, b: int, c :int) -> int:

    """ Obtener el mayor unico

    Pre: recibe tres numeros enteros positivos

    Post: devuelve el mayor unico, en caso de que no haya, devuelve -1

    """

    #Se verifica que los numeros sean enteros
    assert (a, int), "El numero ingresado debe ser entero"
    assert (a, int), "El numero ingresado debe ser entero"
    assert (a, int), "El numero ingresado debe ser entero"

    # Primer input y cuantas veces aparece
    m = a
    aparece = 1

    # Comparamos con b
    if b > m:
        m = b
        aparece = 1
    elif b == m:
        aparece = 2
    
    # Comparamos con c
    if c > m:
        m = c
        aparece = 1
    elif c == m:
        aparece = 2
    
    # Si el maximo aparece una sola vez, es unico
    if aparece == 1:
        return m
    else:
        return -1

# Programa para ejecutar la función
def main():

    """ Programa nucleo

    Pre: el usuario debe ingresar tres numeros enteros y positivos

    Post: se imprime si el numero es o no mayor unico
    
    """

    print("")
    print("Bienvenido al calculador de mayores unicos")
    print("")

    a = int(input("Ingrese el primer entero positivo: "))
    b = int(input("Ingrese el segundo entero positivo: "))
    c = int(input("Ingrese el tercer entero positivo: "))

    res = mayor_unico(a, b, c)

    if res != -1:
        print(f"El mayor unico es: {res}")
    else:
        print("No hay un mayor unico (esta repetido)")

if __name__ == "__main__":
    main()