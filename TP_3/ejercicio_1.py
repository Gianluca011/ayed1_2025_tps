from typing import List

# Cargar números en una matriz n por n
def cargar_matriz(n: int) -> List[List[int]]:

    """ Cargar matriz n por n con enteros desde teclado

    Pre: n mayor que 0

    Post: devuelve una matriz de dimensión n por n con números enteros ingresados

    """

    assert n > 0
    matriz: List[List[int]] = []
    for i in range(n):
        fila = [int(input(f"Ingrese número en posición ({i},{j}): ")) for j in range(n)]
        matriz.append(fila)
    return matriz

# Ordenar en forma ascendente cada fila
def ordenar_filas(matriz: List[List[int]]) -> None:

    """ Ordenar filas de la matriz en forma ascendente

    Pre: matriz no vacía

    Post: modifica la matriz ordenando cada fila

    """

    assert len(matriz) > 0
    for fila in matriz:
        fila.sort()

# Intercambiar dos filas dadas
def intercambiar_filas(matriz: List[List[int]], f1: int, f2: int) -> None:

    """ Intercambiar filas en la matriz

    Pre: 0 menor o igual que f1 y f2 menor que len(matriz)

    Post: se intercambian las filas f1 y f2 en la matriz

    """

    assert 0 <= f1 < len(matriz) and 0 <= f2 < len(matriz)
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]

# Intercambiar dos columnas dadas
def intercambiar_columnas(matriz: List[List[int]], c1: int, c2: int) -> None:

    """ Intercambiar columnas en la matriz

    Pre: 0 menor o igual que c1 y c2 menor que len(matriz)

    Post: se intercambian las columnas c1 y c2 en la matriz

    """

    n = len(matriz)
    assert 0 <= c1 < n and 0 <= c2 < n
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]

# Transponer la matriz
def transponer(matriz: List[List[int]]) -> None:

    """ Transponer la matriz sobre sí misma

    Pre: matriz cuadrada

    Post: intercambia A[i][j] por A[j][i]

    """

    n = len(matriz)
    assert n == len(matriz[0])
    for i in range(n):
        for j in range(i+1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

# Promedio de los elementos de una fila
def promedio_fila(matriz: List[List[int]], fila: int) -> float:

    """ Calcular promedio de una fila

    Pre: 0 menor o igual fila y menor que len(matriz)

    Post: devuelve el promedio de los elementos de la fila

    """

    assert 0 <= fila < len(matriz)
    return sum(matriz[fila]) / len(matriz[fila])

# Porcentaje de elementos impares en una columna
def porcentaje_impares_columna(matriz: List[List[int]], col: int) -> float:

    """ Calcular porcentaje de impares en una columna

    Pre: 0 menor o igual que col y menor que len(matriz)

    Post: devuelve el porcentaje de impares sobre el total de elementos de la columna

    """

    n = len(matriz)
    assert 0 <= col < n
    impares = sum(1 for i in range(n) if matriz[i][col] % 2 != 0)
    return (impares / n) * 100

# Verificar si matriz es simétrica respecto diagonal principal
def es_simetrica_principal(matriz: List[List[int]]) -> bool:

    """ Verificar simetría respecto diagonal principal

    Pre: matriz cuadrada

    Post: devuelve True si A[i][j] == A[j][i] para todo i,j

    """

    n = len(matriz)
    assert n == len(matriz[0])
    for i in range(n):
        for j in range(i+1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Verificar si matriz es simétrica respecto diagonal secundaria
def es_simetrica_secundaria(matriz: List[List[int]]) -> bool:

    """ Verificar simetría respecto diagonal secundaria

    Pre: matriz cuadrada

    Post: devuelve True si A[i][j] == A[n-1-j][n-1-i] para todo i,j

    """

    n = len(matriz)
    assert n == len(matriz[0])
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n-1-j][n-1-i]:
                return False
    return True

# Devolver columnas que son palíndromos
def columnas_palindromas(matriz: List[List[int]]) -> List[int]:

    """ Determinar columnas palíndromas

    Pre: matriz no vacía

    Post: devuelve una lista con los índices de las columnas que son palíndromos

    """

    n = len(matriz)
    assert n > 0
    columnas: List[int] = []
    for col in range(n):
        col_vals = [matriz[f][col] for f in range(n)]
        if col_vals == col_vals[::-1]:
            columnas.append(col)
    return columnas

def imprimir_matriz(matriz: List[List[int]]) -> None:
    for fila in matriz:
        print(fila)

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: el usuario ingresará un entero N mayor que 0 y luego N por N enteros para la matriz

    Post: carga una matriz NxN, ejecuta las funciones e imprime los resultados paso a paso

    """

    n = int(input("Ingrese el valor de N: "))
    matriz = cargar_matriz(n)

    print("\nMatriz cargada:")
    imprimir_matriz(matriz)

    ordenar_filas(matriz)
    print("\nMatriz con filas ordenadas:")
    imprimir_matriz(matriz)

    intercambiar_filas(matriz, 0, n-1)
    print("\nMatriz tras intercambiar fila 0 y fila última:")
    imprimir_matriz(matriz)

    intercambiar_columnas(matriz, 0, n-1)
    print("\nMatriz tras intercambiar columna 0 y última:")
    imprimir_matriz(matriz)

    transponer(matriz)
    print("\nMatriz transpuesta:")
    imprimir_matriz(matriz)

    print(f"\nPromedio de la fila 0: {promedio_fila(matriz, 0):.2f}")
    print(f"Porcentaje de impares en columna 0: {porcentaje_impares_columna(matriz, 0):.2f}%")

    print(f"\n¿Es simétrica respecto a la diagonal principal? {es_simetrica_principal(matriz)}")
    print(f"¿Es simétrica respecto a la diagonal secundaria? {es_simetrica_secundaria(matriz)}")

    print(f"\nColumnas palíndromas: {columnas_palindromas(matriz)}")

if __name__ == "__main__":
    main()