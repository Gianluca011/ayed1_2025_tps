# Genera y devuelve la lista completa de los naipes de la baraja española
def crear_baraja_espanola() -> list[str]:
    """Crear baraja española

    Pre: no recibe parámetros

    Post: devuelve una lista con todas las cartas de la baraja española en formato "n palo"

    """

    try:
        valores = [str(n) for n in range(1, 8)] + ["Sota", "Caballo", "Rey"]
        palos = ["Oros", "Copas", "Espadas", "Bastos"]

        # assert básicos para verificar que las listas no estén vacías
        assert valores and palos, "Error: listas de valores o palos vacías"

        # lista por comprensión que combina cada valor con cada palo
        baraja: list[str] = [
            f"{valor} de {palo}" for palo in palos for valor in valores
        ]

        return baraja

    except AssertionError as ae:
        print("Error de aserción:", ae)
        return []
    except Exception as e:
        print("Error inesperado al crear la baraja:", e)
        return []
    finally:
        pass


# Imprime la baraja por pantalla
def imprimir_baraja(baraja: list[str]) -> None:
    """Imprimir baraja

    Pre: baraja es una lista de strings, puede estar vacía

    Post: muestra las cartas por pantalla

    """

    assert isinstance(baraja, list), "La baraja debe ser una lista"

    try:
        if not baraja:
            print("No hay cartas para mostrar.")
            return

        print("=== Baraja Española ===")
        for carta in baraja:
            print(carta)
    except Exception as e:
        print("Error al imprimir la baraja:", e)
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: crea e imprime la lista de naipes españoles

    """

    try:
        baraja = crear_baraja_espanola()
        imprimir_baraja(baraja)
    except Exception as e:
        print("Error en la ejecución del programa principal:", e)
    finally:
        print("=== Ejecución finalizada ===")


if __name__ == "__main__":
    main()
