# Separa un correo electrónico en sus partes y valida el formato
def descomponer_correo(correo: str) -> tuple[str, ...]:
    """Descomposición de una dirección de correo electrónico

    Pre: recibe una cadena con el formato de correo electrónico

    Post: devuelve una tupla con las partes del correo separadas

    """

    assert isinstance(correo, str), "El parámetro debe ser una cadena de texto."

    try:
        # Validar que haya exactamente un '@'
        if correo.count("@") != 1:
            raise ValueError("Formato inválido: debe contener exactamente un '@'.")

        usuario, dominio = correo.split("@")
        # Validar que el usuario y dominio no estén vacíos
        if not usuario or not dominio or "." not in dominio:
            raise ValueError("Formato inválido: faltan partes del correo.")

        partes_dominio = dominio.split(".")
        partes = (usuario, *partes_dominio)
        return partes

    except ValueError as e:
        print(f"Error: {e}")
        return ()
    except Exception:
        print("Error inesperado al procesar el correo.")
        return ()
    finally:
        pass


# Permite ingresar un correo por teclado
def ingresar_correo() -> str:
    """Ingreso de un correo electrónico

    Pre: el usuario ingresa una cadena representando una dirección de correo electrónico

    Post: devuelve la cadena ingresada

    """

    try:
        correo = input("Ingrese una dirección de correo electrónico: ").strip()
        return correo
    except Exception:
        print("Error al ingresar el correo.")
        return ""
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """

    print("--- Descomposición de correo electrónico ---")

    try:
        correo = ingresar_correo()
        partes = descomponer_correo(correo)

        if partes:
            print("Partes del correo:", partes)
        else:
            print("El formato del correo es inválido.")
    except Exception:
        print("Error inesperado en la ejecución.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
