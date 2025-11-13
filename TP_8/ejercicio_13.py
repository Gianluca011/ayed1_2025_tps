from typing import Dict, List, Any


# Busca y devuelve todas las claves que tengan el valor buscado
def buscarclave(diccionario: Dict[Any, Any], valor: Any) -> List[Any]:
    """Buscar claves asociadas a un valor

    Pre: diccionario es un diccionario válido y valor puede ser de cualquier tipo

    Post: devuelve una lista con todas las claves cuyo valor coincida con valor

    """

    assert isinstance(diccionario, dict), "El parámetro debe ser un diccionario."

    try:
        claves: List[Any] = [
            clave for clave, val in diccionario.items() if val == valor
        ]
        return claves

    except Exception as e:
        print(f"Error buscando las claves: {e}")
        return []
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: solicita un valor al usuario, busca las claves que lo contienen
            y muestra el resultado por pantalla

    """

    print("--- Buscar Claves por Valor ---")

    diccionario: Dict[str, int] = {
        "manzanas": 10,
        "bananas": 5,
        "naranjas": 10,
        "uvas": 7,
        "peras": 5,
    }

    try:
        print("Diccionario de ejemplo:")
        print(diccionario)

        entrada = input("\nIngrese el valor que desea buscar: ")

        try:
            valor_buscado: Any = int(entrada)
        except ValueError:
            valor_buscado = entrada

        claves = buscarclave(diccionario, valor_buscado)

        print("\nResultado:")
        if len(claves) > 0:
            print(f"Claves que apuntan al valor '{valor_buscado}': {claves}")
        else:
            print("No se encontraron claves con ese valor.")

    except Exception as e:
        print(f"Error en el programa principal: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
