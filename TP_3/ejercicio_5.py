import random
from typing import List, Tuple

# Constantes
libre = 0
ocupado = 1

# Muestra por pantalla el estado de la sala
def mostrar_butacas(sala: List[List[int]]) -> None:

    """ Muestra el estado de las butacas en la sala

    Pre: sala es una matriz no vacía con valores 0 o 1

    Post: muestra la sala en consola, indicando fila y butacas

    """

    print("\nEstado de la sala (0 = libre, 1 = ocupado):")
    for i, fila in enumerate(sala):
        print(f"Fila {i+1:2}: " + " ".join(str(b) for b in fila))
    print()

# Reservar una butaca si está libre
def reservar(sala: List[List[int]], fila: int, butaca: int) -> bool:

    """ Reservar una butaca si está libre

    Pre: fila y butaca tienen que ser índices válidos de la sala

    Post: devuelve True si la reserva fue exitosa, False si ya estaba ocupada

    """

    if sala[fila][butaca] == libre:
        sala[fila][butaca] = ocupado
        return True
    return False

# Rellena la sala con 0 y 1 aleatorio para simular ocupación
def cargar_sala(sala: List[List[int]]) -> None:

    """ Cargar la sala con valores aleatorios de ocupación

    Pre: sala es una matriz inicializada en 0

    Post: modifica la sala, asignando al azar butacas libres u ocupadas

    """

    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = random.choice([libre, ocupado])

# Cuenta cuántas butacas están libres en toda la sala
def butacas_libres(sala: List[List[int]]) -> int:

    """ Contar butacas libres

    Pre: la sala no debe estar vacía

    Post: devuelve el número total de butacas libres en la sala

    """

    return sum(fila.count(libre) for fila in sala)

# Busca la secuencia más larga de butacas libres en la misma fila
def butacas_contiguas(sala: List[List[int]]) -> Tuple[int, int, int]:

    """ Buscar la secuencia más larga de butacas libres contiguas

    Pre: la sala no debe estar vacía

    Post: devuelve fila, inicio y longitud de la secuencia más larga

    """

    mejor_fila, mejor_inicio, mejor_longitud = -1, -1, 0

    for i, fila in enumerate(sala):
        inicio, longitud = -1, 0
        for j, butaca in enumerate(fila):
            if butaca == libre:
                if inicio == -1:  # empieza una nueva secuencia
                    inicio = j
                longitud += 1
                if longitud > mejor_longitud:
                    mejor_fila, mejor_inicio, mejor_longitud = i, inicio, longitud
            else:
                inicio, longitud = -1, 0  # se corta la secuencia
    return mejor_fila, mejor_inicio, mejor_longitud

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: el usuario ingresa enteros positivos para filas y columnas

    Post: muestra toda la información que solicita el problema

    """

    filas = int(input("Ingrese cantidad de filas: "))
    columnas = int(input("Ingrese cantidad de butacas por fila: "))

    # Crea una sala vacía
    sala = [[libre for _ in range(columnas)] for _ in range(filas)]

    # Carga ocupación aleatoria
    cargar_sala(sala)
    mostrar_butacas(sala)

    # Muestra las butacas libres
    print(f"Butacas libres en la sala: {butacas_libres(sala)}")

    # Reservar
    f = int(input("Ingrese fila a reservar (1-indexada): ")) - 1
    b = int(input("Ingrese butaca a reservar (1-indexada): ")) - 1
    if reservar(sala, f, b):
        print("Reserva exitosa")
    else:
        print("La butaca ya está ocupada")

    mostrar_butacas(sala)

    # Buscar la secuencia más larga
    fila, inicio, longitud = butacas_contiguas(sala)
    if longitud > 0:
        print(f"La mayor secuencia de butacas libres es de {longitud} "
              f"en fila {fila+1}, desde la butaca {inicio+1}")
    else:
        print("No hay butacas libres contiguas.")

if __name__ == "__main__":
    main()