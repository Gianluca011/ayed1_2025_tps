import random
from typing import List, Tuple

# Constantes
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
maxima_produccion = 150

# Crea una matriz con datos aleatorios
def generar_produccion(fabricas: int) -> List[List[int]]:

    """ Genera la producción semanal de bicicletas

    Pre: fabricas tiene que ser mayor que 0

    Post: devuelve una matriz de tamaño fabricas por 6 con valores enteros aleatorios dentro del rango

    """

    assert fabricas > 0, "Debe haber al menos una fábrica."
    return [[random.randint(0, maxima_produccion) for _ in range(len(dias))] for _ in range(fabricas)]

# Imprimir matrices de producción
def imprimir_matriz(matriz: List[List[int]]) -> None:

    """ Imprime la matriz con formato

    Pre: la matriz no debe estar vacía

    Post: muestra la matriz en consola con cabecera de días

    """

    print(" " * 10 + " ".join(f"{d:^10}" for d in dias))
    for i, fila in enumerate(matriz):
        print(f"Fábrica {i+1:<2} " + " ".join(f"{x:^10}" for x in fila))
    print()

# Total de bicicletas por fábrica
def total_por_fabrica(matriz: List[List[int]]) -> List[int]:

    """ Calcular la producción total por fábrica
    
    Pre: la matriz no debe estar vacía

    Post: devuelve una lista con la suma de bicicletas fabricadas por cada fábrica en la semana

    """

    return [sum(fila) for fila in matriz]

# Fábrica y día con mayor producción en un solo día
def max_produccion_un_dia(matriz: List[List[int]]) -> Tuple[int, int, int]:

    """ Encontrar la fábrica y día con mayor producción en un solo día

    Pre: la matriz no debe estar vacía

    Post: retorna una tupla con fábrica, día y valor

    """

    max_val = -1
    fab_max, dia_max = -1, -1
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > max_val:
                max_val = valor
                fab_max, dia_max = i, j
    return fab_max, dia_max, max_val

# Día más productivo considerando todas las fábricas
def dia_mas_productivo(matriz: List[List[int]]) -> Tuple[int, int]:

    """ Encontrar el día más productivo en total

    Pre: la matriz no debe estar vacía

    Post: retorna una tupla con el índice del día y el total de bicicletas
    
    """

    produccion_por_dia = [sum(matriz[i][j] for i in range(len(matriz))) for j in range(len(dias))]
    dia_max = produccion_por_dia.index(max(produccion_por_dia))
    return dia_max, produccion_por_dia[dia_max]

# Lista por comprensión con la menor cantidad fabricada por cada fábrica
def menor_por_fabrica(matriz: List[List[int]]) -> List[int]:

    """ Menor cantidad fabricada por cada fábrica

    Pre: la matriz no debe estar vacía

    Post: retorna una lista con el mínimo de cada fila de la matriz

    """

    return [min(fila) for fila in matriz]

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: el usuario ingresa un número entero positivo fabricas

    Post: muestra toda la información que solicita el problema

    """

    n = int(input("Ingrese la cantidad de fábricas: "))
    matriz = generar_produccion(n)

    print("\nProducción semanal (bicicletas):")
    imprimir_matriz(matriz)

    totales = total_por_fabrica(matriz)
    for i, total in enumerate(totales):
        print(f"Fábrica {i+1}: {total} bicicletas en la semana")
    print()

    fab, dia, valor = max_produccion_un_dia(matriz)
    print(f"La mayor producción fue {valor} bicicletas en Fábrica {fab+1} el día {dias[dia]}")
    print()

    dia_max, total_dia = dia_mas_productivo(matriz)
    print(f"El día más productivo fue {dias[dia_max]} con {total_dia} bicicletas en total")
    print()

    minimos = menor_por_fabrica(matriz)
    for i, minimo in enumerate(minimos):
        print(f"Fábrica {i+1}: menor producción en un día = {minimo} bicicletas")

if __name__ == "__main__":
    main()