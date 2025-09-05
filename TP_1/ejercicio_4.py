# Función para calcular el cambio
def calcular_cambio(total_compra: int, dinero_recibido: int) -> int:

    """
    Pre: recibe el total de la compra y el dinero recibido como enteros positivos

    Post: devuelve un diccionario con la cantidad de billetes de cada denominación 
    que se deben entregar como vuelto, o un mensaje de error si no es posible

    """

    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    
    if dinero_recibido < total_compra:
        return "Error: Dinero insuficiente."
    
    vuelto = dinero_recibido - total_compra
    cambio = {}
    
    for billete in billetes:
        cantidad = vuelto // billete  # Calcula cuantos billetes de esa denominacion se pueden dar
        if cantidad > 0:
            cambio[billete] = cantidad
            vuelto -= billete * cantidad  # Actualiza el vuelto restante
    
    if vuelto > 0:
        return "Error: No se puede entregar el cambio exacto con los billetes disponibles."
    
    return cambio

# Función principal
def main():

    """ Programa nucleo
    
    Pre: el usuario debe ingresar dos numeros enteros positivos

    Post: solicita al usuario los datos de la compra, calcula el cambio usando la función
    y muestra en pantalla el resultado

    """

    print("")
    print("=== Calculadora de cambio ===")
    print("")
    
    # Pide datos al usuario
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    
    # Calcula el cambio usando la función
    resultado = calcular_cambio(total_compra, dinero_recibido)
    
    # Muestra el resultado
    if isinstance(resultado, dict):
        print("Vuelto a entregar:")
        for billete, cantidad in resultado.items():
            print(f"{cantidad} billete(s) de ${billete}")
    else:
        print(resultado)

if __name__ == "__main__":
    main()