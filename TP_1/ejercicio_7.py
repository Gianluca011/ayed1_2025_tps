# Funcion que calcula el dia siguiente a una fecha
def diasiguiente(dia: int, mes: int, año: int) -> int:
    """ Calcula la fecha siguiente a una fecha dada

    Pre: dia, mes y año son enteros que representan una fecha valida

    Post: devuelve tres enteros: dia, mes y año correspondientes al día siguiente

    """
    # Define la cantidad de dias por mes
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Comprueba si es año bisiesto y actualiza a febrero
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_mes[1] = 29
    
    dia += 1  # Pasa al siguiente dia

    # Si el dia supera los dias del mes, reinicia y pasa al mes siguiente
    if dia > dias_mes[mes - 1]:
        dia = 1
        mes += 1
    
    # Si el mes supera 12, reinicia y pasa al año siguiente
    if mes > 12:
        mes = 1
        año += 1
    
    return dia, mes, año

# Función para sumar N dias a una fecha
def sumar_dias(dia, mes, año, N):

    """ Suma N dias a una fecha usando la funcion diasiguiente

    Pre: dia, mes, año son enteros validos, N es entero positivo

    Post: devuelve la fecha resultante como dia, mes y año

    """

    for _ in range(N):
        dia, mes, año = diasiguiente(dia, mes, año)
    return dia, mes, año

# Funcion para calcular cantidad de dias entre dos fechas
def dias_entre_fechas(dia1, mes1, año1, dia2, mes2, año2):

    """ Calcula la cantidad de dias entre dos fechas usando diasiguiente

    Pre: las fechas son validas y la primera fecha no es posterior a la segunda

    Post: devuelve un entero con la cantidad de dias entre las dos fechas

    """
    contador = 0
    while (dia1, mes1, año1) != (dia2, mes2, año2):
        dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)
        contador += 1
    return contador

# Funcion main
def main():

    """ Permite al usuario sumar N dias a una fecha o calcular dias entre fechas

    Pre: recibe varios enteros positivos, como dia, mes, etc

    Post: solicita al usuario la opción deseada y las fechas, mostrando el resultado

    """

    print("")
    print("=== Programa de cálculo de fechas ===")
    print("")
    print("Opciones:")
    print("1. Sumar N días a una fecha")
    print("2. Calcular días entre dos fechas")
    
    opcion = int(input("Ingrese opción (1 o 2): "))
    
    if opcion == 1:
        dia = int(input("Ingrese día: "))
        mes = int(input("Ingrese mes: "))
        año = int(input("Ingrese año: "))
        N = int(input("Ingrese cantidad de días a sumar: "))
        nuevo_dia, nuevo_mes, nuevo_año = sumar_dias(dia, mes, año, N)
        print(f"Fecha resultante: {nuevo_dia}/{nuevo_mes}/{nuevo_año}")
    
    elif opcion == 2:
        print("Ingrese la primera fecha:")
        dia1 = int(input("Día: "))
        mes1 = int(input("Mes: "))
        año1 = int(input("Año: "))
        print("Ingrese la segunda fecha:")
        dia2 = int(input("Día: "))
        mes2 = int(input("Mes: "))
        año2 = int(input("Año: "))
        cantidad = dias_entre_fechas(dia1, mes1, año1, dia2, mes2, año2)
        print(f"Días entre fechas: {cantidad}")
    
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()