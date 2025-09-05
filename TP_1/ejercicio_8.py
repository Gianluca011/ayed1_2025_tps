# Función que calcula el día de la semana
def diadelasemana(dia: int, mes: int, año: int) -> int:

    """ Calcula el día de la semana para una fecha dada

    Pre: dia, mes y año son enteros que representan una fecha válida

    Post: devuelve un entero del 0 al 6 representando el día de la semana

    """

    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2

    siglo = año // 100
    año2 = año % 100

    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem += 7
    return diasem

# Función que devuelve la cantidad de días de un mes, considerando bisiestos
def dias_del_mes(mes: int, año: int) -> int:

    """ Devuelve la cantidad de días de un mes dado y año

    Pre: mes entre 1 y 12, año entero positivo

    Post: devuelve un entero con la cantidad de días del mes

    """

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verifica bisiesto
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            return 29
    return dias_mes[mes - 1]

# Función que imprime el calendario del mes
def imprimir_calendario(mes: int, año: int) -> None:

    """ Imprime el calendario completo de un mes y año dado

    Pre: mes entre 1 y 12, año entero positivo

    Post: muestra por pantalla el calendario del mes con semanas empezando en domingo

    """

    print(f"Calendario de {mes}/{año}")
    print("Do Lu Ma Mi Ju Vi Sa")  # Encabezado de días

    # Día de la semana del primer día del mes
    primer_dia = diadelasemana(1, mes, año)

    # Imprime espacios iniciales
    print("   " * primer_dia, end="")

    total_dias = dias_del_mes(mes, año)

    for dia in range(1, total_dias + 1):
        print(f"{dia:2d} ", end="")
        # Salto de línea cada vez que llega al sábado
        if (primer_dia + dia) % 7 == 0:
            print()

# Función main
def main() -> None:

    """ Permite al usuario ingresar un mes y año y muestra el calendario

    Pre: recibe dos numeros enteros positivos

    Post: imprime el calendario del mes ingresado

    """

    print("")
    print("=== Bienvenido al python calendar ===")
    print("")

    mes: int = int(input("Ingrese el mes (1-12): "))
    año: int = int(input("Ingrese el año: "))

    imprimir_calendario(mes, año)

if __name__ == "__main__":
    main()