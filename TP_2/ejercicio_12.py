# Esta función carga los registros de socios que entran al club
def cargar_registros() -> list[int]:

    """ Carga los números de socios que visitan el club hasta que se ingresa 0
    
    Pre: ninguna

    Post: devuelve una lista con todos los números de socios registrados

    """

    registros = []
    print("--- Bienvenido al sistema de registro de socios (ingrese 0 para finalizar) ---")
    while True:
        try:
            socio = int(input("Ingrese número de socio (5 dígitos): "))
            if socio == 0:
                break
            
            if not (10000 <= socio <= 99999):
                print("Número de socio inválido. Debe ser de 5 dígitos.")
                continue
            
            registros.append(socio)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    
    return registros

# Esta función cuenta las entradas de cada socio y las muestra
def contar_entradas(registros: list[int]):

    """ Informa para cada socio cuantas veces ingresó al club

    Pre: registros es una lista de números enteros

    Post: imprime el informe de entradas por socio

    """

    print("--- Informe de Ingresos por Socio ---")
    
    socios_unicos = sorted(list(set(registros)))
    
    for socio in socios_unicos:
        ingresos = registros.count(socio)
        print(f"Socio {socio}: {ingresos} ingresos")
    
    print("--------------------------------------")

# Esta función elimina todas las entradas de un socio dado
def eliminar_socio(registros: list[int], socio_a_eliminar: int):

    """ Elimina todas las entradas de un socio de la lista de registros
    
    Pre: registros es una lista de números enteros, socio_a_eliminar es un entero

    Post: registros es modificada, y se informa la cantidad de ingresos eliminados

    """

    print("Eliminando ingresos del socio {socio_a_eliminar}...")
    
    ingresos_eliminados = registros.count(socio_a_eliminar)
    
    while socio_a_eliminar in registros:
        registros.remove(socio_a_eliminar)
    
    print(f"Se eliminaron {ingresos_eliminados} ingresos del socio {socio_a_eliminar}.")

# Programa principal
def main():

    """ Programa nucleo
    
    Pre: ninguna

    Post: ejecuta las funciones de carga, reporte y eliminación

    """

    registros = cargar_registros()
    
    contar_entradas(registros)
    
    print("--- Eliminación de Socio ---")
    try:
        socio_a_dar_de_baja = int(input("Ingrese el número de socio a dar de baja: "))
        
        print(f"Registros antes de la eliminación: {registros}")
        
        eliminar_socio(registros, socio_a_dar_de_baja)
        
        print(f"Registros después de la eliminación: {registros}")
        
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    
    print("\nPrograma finalizado. ¡Gracias por usar nuestro servicio!")

if __name__ == "__main__":
    main()