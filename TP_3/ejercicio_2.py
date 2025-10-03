from typing import List

# Matriz con valores en la diagonal principal, impares consecutivos
def matriz_a(n: int) -> List[List[int]]:

    """ Genera una matriz con números impares consecutivos en la diagonal principal

    Pre: n mayor que 0

    Post: devuelve una matriz n por n en la diagonal principal y ceros en el resto

    """

    assert n > 0
    return [[(2*i+1) if i == j else 0 for j in range(n)] for i in range(n)]

# Matriz con números impares decrecientes en diagonal secundaria
def matriz_b(n: int) -> List[List[int]]:

    """ Genera una matriz con números impares decrecientes en la diagonal secundaria

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con valores impares descendentes en diagonal secundaria y ceros en el resto

    """

    assert n > 0
    val = 2*n - 1
    return [[(val - 2*i) if i + j == n-1 else 0 for j in range(n)] for i in range(n)]

# Matriz con números decrecientes por fila desde n hasta 1 en diagonal inferior
def matriz_c(n: int) -> List[List[int]]:

    """ Genera una matriz con números decrecientes por fila en diagonal inferior

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con i+1 en fila i y en columnas desde 0 hasta i

    """

    assert n > 0
    return [[i+1 if j <= i else 0 for j in range(n)] for i in range(n)]

# Matriz con números decrecientes en bloque
def matriz_d(n: int) -> List[List[int]]:

    """ Generar matriz con filas decrecientes de potencias de 2

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con cada fila igual a n dividido 2 potencia de fila

    """

    assert n > 0
    val = n*2
    return [[val//(2**i) for j in range(n)] for i in range(n)]

# Matriz con números ascendentes por columnas
def matriz_e(n: int) -> List[List[int]]:

    """ Genera una matriz con números ascendentes por columnas

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con números desde 0 hasta n por 2 en columnas pares

    """

    assert n > 0
    return [[i+j for j in range(n)] for i in range(n)]

# Matriz con números en forma triangular invertida
def matriz_f(n: int) -> List[List[int]]:

    """ Genera una matriz con valores crecientes desde la esquina inferior izquierda

    Pre: n mayor que 0

    Post: devuelve una matriz n por n triangular invertida con valores desde 1 hasta n por n

    """

    assert n > 0
    val = 1
    matriz = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            if i+j >= n-1:
                matriz[i][j] = val
                val += 1
    return matriz

# Matriz con valores ascendentes por filas normales
def matriz_g(n: int) -> List[List[int]]:

    """ Genera una matriz con números consecutivos por filas

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con números desde 1 hasta n por n en orden fila por fila

    """

    assert n > 0
    return [[i*n + j + 1 for j in range(n)] for i in range(n)]

# Matriz con valores en zig-zag
def matriz_h(n: int) -> List[List[int]]:

    """ Genera una matriz con valores en zig-zag por columnas

    Pre: n > 0

    Post: devuelve una matriz n por n con números consecutivos distribuidos en columnas alternadas

    """

    assert n > 0
    matriz = [[0]*n for _ in range(n)]
    val = 1
    for j in range(n):
        if j % 2 == 0:
            for i in range(n):
                matriz[i][j] = val
                val += 1
        else:
            for i in range(n-1, -1, -1):
                matriz[i][j] = val
                val += 1
    return matriz

# Matriz con valores consecutivos por columnas normales
def matriz_i(n: int) -> List[List[int]]:

    """ Genera una matriz con números consecutivos por columnas

    Pre: n mayor que 0

    Post: devuelve una matriz n por n con números del 1 a n por n en orden columna por columna

    """

    assert n > 0
    return [[i + j*n + 1 for j in range(n)] for i in range(n)]

# Imprime la matriz de forma ordenada en consola
def imprimir_matriz(matriz: List[List[int]]) -> None:

    """ Imprimir matriz con formato

    Pre: matriz no vacía, representada como lista de listas de enteros

    Post: muestra la matriz en consola, cada fila en una línea con los valores alineados

    """

    for fila in matriz:
        print(" ".join(f"{x:2}" for x in fila))
    print()

# Programa para ejecutar la función
def main() -> None:

    """ Programa nucleo

    Pre: el usuario ingresa un entero n mayor que 0

    Post: genera e imprime las matrices de a a i según sus patrones definidos

    """

    n = int(input("Ingrese el valor de N: "))
    assert n > 0, "N debe ser mayor a 0"

    print("Matriz a:")
    imprimir_matriz(matriz_a(n))

    print("Matriz b:")
    imprimir_matriz(matriz_b(n))

    print("Matriz c:")
    imprimir_matriz(matriz_c(n))

    print("Matriz d:")
    imprimir_matriz(matriz_d(n))

    print("Matriz e:")
    imprimir_matriz(matriz_e(n))

    print("Matriz f:")
    imprimir_matriz(matriz_f(n))

    print("Matriz g:")
    imprimir_matriz(matriz_g(n))

    print("Matriz h:")
    imprimir_matriz(matriz_h(n))

    print("Matriz i:")
    imprimir_matriz(matriz_i(n))

if __name__ == "__main__":
    main()