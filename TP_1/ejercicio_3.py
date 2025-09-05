# Función para calcular el total gastado en viajes
def calcular_gastos(viajes: int) -> int:
    """ Calcula el total gastado en viajes de subte considerando descuentos por cantidad
    
    Pre: recibe un entero 'viajes' mayor a 0

    Post: devuelve el total de dinero gastado en el mes

    """
    tarifa_maxima = 960  # valor máximo del pasaje
    total = 0
    
    if viajes <= 20:
        total = viajes * tarifa_maxima
    elif viajes <= 30:
        total = viajes * tarifa_maxima * 0.8  # 20% de descuento
    elif viajes <= 40:
        total = viajes * tarifa_maxima * 0.7  # 30% de descuento
    else:
        total = viajes * tarifa_maxima * 0.6  # 40% de descuento
        
    return total


# Programa principal para probar la función
def main():
        
    """ Programa nucleo
    
    Pre: se tiene que ingresar un numero entero positivo que represente la cantidad de viajes

    Post: se imprime el gasto del mes segun la cantidad de viajes, con su respectivo descuento

    """

    print("")
    print("Calculadora de descuentos para viajantes en subte")
    print("")

    cantidad_viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
    total_gastado = calcular_gastos(cantidad_viajes)
    print(f"El total gastado en el mes es: ${total_gastado:.2f}")

if __name__ == "__main__":
    main()