from typing import Dict, Tuple


# Crea y devuelve un diccionario con los productos y sus precios
def crear_lista_precios() -> Dict[str, float]:
    """Crear lista de precios de la librería

    Pre: no recibe parámetros

    Post: devuelve un diccionario donde las claves son nombres de artículos
            y los valores son sus precios positivos

    """

    try:
        lista: Dict[str, float] = {
            "cuaderno rayado": 1200.0,
            "cuaderno tapa dura": 2500.0,
            "lapicera": 300.0,
            "regla": 450.0,
            "marcador": 800.0,
            "carpeta": 1800.0,
        }

        for precio in lista.values():
            assert precio > 0, "El precio debe ser positivo."

        return lista

    except AssertionError as ae:
        print(f"Error en la creación de la lista: {ae}")
        return {}
    finally:
        pass


# Incrementa el precio de todos los cuadernos en un porcentaje dado
def incrementar_cuadernos(lista: Dict[str, float], porcentaje: float) -> None:
    """Incrementar precios de cuadernos

    Pre: lista es un diccionario con precios y porcentaje es un número positivo

    Post: modifica la lista incrementando el precio de los artículos cuyo
            nombre contiene la palabra cuaderno

    """

    assert isinstance(lista, dict), "La lista debe ser un diccionario."
    assert porcentaje > 0, "El porcentaje debe ser positivo."

    try:
        for item in lista:
            if "cuaderno" in item.lower():
                lista[item] *= 1 + porcentaje / 100

    except Exception as e:
        print(f"Error al incrementar los precios: {e}")
    finally:
        pass


# Devuelve el ítem más costoso del diccionario
def obtener_item_mas_costoso(lista: Dict[str, float]) -> Tuple[str, float]:
    """Obtener el ítem más costoso

    Pre: lista es un diccionario no vacío con precios positivos

    Post: devuelve una tupla con el artículo más caro

    """

    assert isinstance(lista, dict), "La lista debe ser un diccionario."
    assert len(lista) > 0, "La lista no puede estar vacía."

    try:
        item = max(lista.items(), key=lambda elem: elem[1])
        return item

    except Exception as e:
        print(f"Error buscando el ítem más costoso: {e}")
        return ("", 0.0)
    finally:
        pass


# Imprime todos los elementos de la lista de precios
def imprimir_lista(lista: Dict[str, float]) -> None:
    """Imprimir lista de precios

    Pre: lista es un diccionario válido

    Post: muestra por pantalla todos los productos y sus precios

    """

    assert isinstance(lista, dict), "La lista debe ser un diccionario."

    for item, precio in lista.items():
        print(f"- {item}: ${precio:.2f}")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """

    print("--- Lista de Precios ---")

    try:
        lista = crear_lista_precios()
        assert lista != {}, "La lista no se pudo crear."

        incrementar_cuadernos(lista, 15)

        print("\nListado actualizado:")
        imprimir_lista(lista)

        item, precio = obtener_item_mas_costoso(lista)
        print(f"\nÍtem más costoso: {item} (${precio:.2f})")

    except Exception as e:
        print(f"Error en el programa principal: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
