# Elimina claves de un diccionario
def eliminarclaves(dic: dict, claves: list) -> tuple[dict, int]:
    """Eliminar claves de un diccionario

    Pre: dic debe ser un diccionario y claves debe ser una lista

    Post: devuelve una tupla, donde cantidad_eliminadas es la cantidad de claves eliminadas

    """
    assert isinstance(dic, dict), "El primer parámetro debe ser un diccionario."
    assert isinstance(claves, list), "El segundo parámetro debe ser una lista."

    eliminadas = 0

    for clave in claves:
        try:
            dic.pop(clave)
            eliminadas += 1
        except KeyError:
            pass

    return dic, eliminadas


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: llama a eliminarclaves y muestra el resultado
    """
    print("--- Eliminar claves de un diccionario ---")

    # Diccionario de ejemplo para probar
    dic = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(f"Diccionario inicial: {dic}")

    try:
        entrada = input("Ingrese claves a eliminar separadas por coma: ")
        lista_claves = [x.strip() for x in entrada.split(",")]

        dic_modif, cant = eliminarclaves(dic, lista_claves)

        print("\nResultados:")
        print(f"Diccionario modificado: {dic_modif}")
        print(f"Cantidad de claves eliminadas: {cant}")

    except AssertionError as e:
        print(f"Error: {e}")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
