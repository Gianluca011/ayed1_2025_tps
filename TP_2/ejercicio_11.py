# Esta función carga los datos de los pacientes en listas separadas
def cargar_pacientes() -> tuple[list[int], list[int]]:

    """ Carga los pacientes en dos listas separadas, hasta que se ingresa -1 como número de afiliado

    Pre: ninguna

    Post: devuelve una tupla con dos listas, la de pacientes por urgencia y la de pacientes por turno

    """

    pacientes_urgencia = []
    pacientes_turno = []
    
    print("--- Bienvenido al sistema de carga de pacientes (ingrese -1 para finalizar) ---")
    while True:
        try:
            afiliado = int(input("Ingrese número de afiliado (4 dígitos): "))
            if afiliado == -1:
                break
            
            tipo = int(input("Tipo de atención (0: Urgencia, 1: Turno): "))
            
            if not (1000 <= afiliado <= 9999):
                print("Número de afiliado inválido. Debe ser de 4 dígitos.")
                continue
            
            if tipo == 0:
                pacientes_urgencia.append(afiliado)
            elif tipo == 1:
                pacientes_turno.append(afiliado)
            else:
                print("Tipo de atención inválido.")
        
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    return pacientes_urgencia, pacientes_turno

# Esta función muestra los listados de pacientes cargados
def mostrar_listados(urgencia: list[int], turno: list[int]):

    """ Muestra los listados de pacientes atendidos por urgencia y por turno

    Pre: urgencia y turno son listas de números enteros

    Post: imprime el contenido de ambas listas

    """

    print("\n--- Listado de Pacientes ---")
    print(f"Pacientes atendidos por Urgencia: {urgencia}")
    print(f"Pacientes atendidos por Turno: {turno}")
    print("----------------------------")

# Esta función busca la cantidad de atenciones de un afiliado
def buscar_paciente(urgencia: list[int], turno: list[int]):

    """ Permite buscar un número de afiliado y reporta el número de atenciones por turno y por urgencia

    Pre: urgencia y turno son listas de números enteros

    Post: imprime los resultados de las búsquedas solicitadas

    """

    print("--- Búsqueda de Afiliado ---")
    while True:
        try:
            afiliado_a_buscar = int(input("Ingrese el número de afiliado a buscar (-1 para salir): "))
            if afiliado_a_buscar == -1:
                break
            
            veces_urgencia = 0
            veces_turno = 0

            for paciente in urgencia:
                if paciente == afiliado_a_buscar:
                    veces_urgencia += 1
            
            for paciente in turno:
                if paciente == afiliado_a_buscar:
                    veces_turno += 1
            
            print(f"El afiliado {afiliado_a_buscar} fue atendido:")
            print(f"- {veces_urgencia} veces por Urgencia")
            print(f"- {veces_turno} veces por Turno")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

# Funcion principal
def main():

    """ Programa nucleo
    
    Pre: ninguna

    Post: ejecuta las funciones de carga, visualización y búsqueda de pacientes

    """

    pacientes_urgencia, pacientes_turno = cargar_pacientes()
    
    mostrar_listados(pacientes_urgencia, pacientes_turno)
    
    buscar_paciente(pacientes_urgencia, pacientes_turno)
    
    print("\nPrograma finalizado, gracias por usar el sistema.")

if __name__ == "__main__":
    main()