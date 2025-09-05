# Funcion para ver si el año es bisiesto
def bisiesto(año :int) -> int:

    """ Determina si el año es bisiesto

    Pre: año debe ser un numero entero y positivo

    Post: devuelve True si el año es bisiesto y False en caso contrario

    """

    # Verifica que los numeros sean enteros y positivos
    assert isinstance(año, int), "El año debe ser entero"
    assert año > 0, "El año debe ser positivo"

    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Funcion para ver si una fecha es valida
def fecha_valida(dia :int, mes :int, año :int):
    """ Verifica si una fecha es valida

    Pre: dia, mes y año deben ser enteros y positivos

    Post: devuelve True si la fecha existe y False en el caso contrario

    """
    # Verifica que los numeros sean enteros y positivos
    assert isinstance(dia, int) and isinstance(mes, int) and isinstance(año, int), "Deben ser numeros enteros"
    assert dia > 0 and mes > 0 and año > 0, "Deben ser positivos"

    # Validar mes
    if mes < 1 or mes > 12:
        return False
    
    # Dias de cada mes (no bisiesto)
    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Si es bisiesto en febrero
    if mes == 2 and bisiesto(año):
        dias_mes = 29
    else:
        dias_mes = dias_del_mes[mes - 1]
    
    # Validar dia
    if dia < 1 or dia > dias_mes:
        return False
    
    return True

# Programa para ejecutar la función
def main():
    """ Programa nucleo
    
    Pre: el usuario debe ingresar tres numeros enteros y positivos

    Post: se imprime si la fecha ingresada es valida o no
    
    """

    print("")
    print("Bienvenido al validador de fechas")
    print("")

    dia = int(input("Ingrese dia: "))
    mes = int(input("Ingrese mes: "))
    año = int(input("Ingrese año: "))

    if fecha_valida(dia, mes, año):
        print("La fecha es valida")
    else:
        print("La fecha es invalida")

if __name__ == "__main__":
    main()