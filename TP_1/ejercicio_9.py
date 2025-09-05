import random

# Función para simular el peso de cada naranja y clasificarla
def clasificar_naranjas(cantidad: int):

    """ Simula el peso de cada naranja y determina cuántas van a cajones,
    cuántas son para jugo y cuántas sobran

    Pre: cantidad es un entero positivo indicando la cantidad de naranjas cosechadas

    Post: devuelve una tupla con cantidad de cajones completos, cantidad de naranjas fuera
    del rango de peso y naranjas válidas que no llenan un cajón completo

    """

    naranjas_validas = 0
    naranjas_jugo = 0

    for _ in range(cantidad):
        peso = random.randint(150, 350)  # Peso simulado de la naranja
        if 200 <= peso <= 300:
            naranjas_validas += 1
        else:
            naranjas_jugo += 1

    cajones_llenos = naranjas_validas // 100
    sobrante = naranjas_validas % 100

    return cajones_llenos, naranjas_jugo, sobrante

# Función para calcular cuántos camiones se necesitan
def calcular_camiones(cajones: int, capacidad_camion: int = 500) -> int:

    """ Calcula la cantidad de camiones necesarios para transportar la cosecha

    Pre: cajones es un entero positivo

    Post: devuelve la cantidad de camiones necesarios, considerando que cada uno
          debe ocupar al menos 80% de su capacidad

    """

    peso_cajon_kg = 100 * 0.25  # Promedio 250g por naranja
    camiones = 0
    cajones_restantes = cajones

    while cajones_restantes > 0:
        # Cada camión puede llevar hasta 500 kg
        carga_camion = min(capacidad_camion // peso_cajon_kg, cajones_restantes)
        # Solo despacha si carga >= 80% de la capacidad
        if carga_camion * peso_cajon_kg >= 0.8 * capacidad_camion:
            camiones += 1
        cajones_restantes -= carga_camion

    return camiones


# Función nucleo
def main() -> None:
    """ Programa principal para contabilizar cajones, naranjas para jugo,
    sobrantes y camiones necesarios

    Pre: recibe la cantidad de naranjas cosechadas, o sea, un entero positivo

    Post: solicita la cantidad de naranjas cosechadas y muestra la información completa

    """

    print("")
    print("=== Control de cosecha de naranjas ===")
    print("")
    
    cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))

    # Clasificación de naranjas
    cajones, jugo, sobrante = clasificar_naranjas(cantidad_naranjas)
    print(f"Cajones llenos: {cajones}")
    print(f"Naranjas para jugo: {jugo}")
    print(f"Sobrante de naranjas válidas: {sobrante}")

    # Calcular camiones necesarios
    camiones = calcular_camiones(cajones)
    print(f"Cantidad de camiones necesarios: {camiones}")

if __name__ == "__main__":
    main()