def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """Devuelve los últimos n caracteres de una cadena

    Pre: cadena es una cadena no vacía y n es un entero no negativo

    Post: devuelve una subcadena con los últimos n caracteres. Si n es mayor que la longitud de la cadena, devuelve la cadena completa

    """

    assert isinstance(cadena, str), "La cadena debe ser de tipo str"
    assert isinstance(n, int), "n debe ser un entero"
    assert n >= 0, "n debe ser un número no negativo"

    try:
        # Manejo del caso donde n supera la longitud
        if n > len(cadena):
            return cadena
        else:
            return cadena[-n:]
    except Exception as e:
        print("Ocurrió un error al obtener los últimos caracteres:", e)
        return ""
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: ejecuta pruebas mostrando los últimos n caracteres de una cadena por pantalla

    """

    texto = "El número de teléfono es 4356-7890"
    n = 9

    print("Texto original:", texto)
    print("Cantidad de caracteres a extraer:", n)

    resultado = ultimos_n_caracteres(texto, n)
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
