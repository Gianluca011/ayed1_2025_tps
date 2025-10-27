# Verifica si una dirección de correo electrónico es válida
def es_valido(correo: str) -> bool:
    """Determina si una dirección de correo electrónico es válida

    Pre: correo es una cadena no vacía

    Post: devuelve True si el correo cumple con el formato requerido, False en caso contrario

    """

    assert isinstance(correo, str), "El correo debe ser una cadena."
    correo = correo.lower().strip()

    # Verifica que haya un solo '@'
    if correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@")

    # Solo caracteres alfanuméricos para usuario
    if not usuario.isalnum():
        return False

    # Dominio debe tener al menos un punto y terminar en .com o .com.ar
    if "." not in dominio:
        return False
    if not (dominio.endswith(".com") or dominio.endswith(".com.ar")):
        return False

    # Dominio debe tener algo antes del punto
    if dominio[0] == ".":
        return False

    return True


# Extrae el dominio de una dirección de correo válida
def obtener_dominio(correo: str) -> str:
    """Devuelve el dominio de una dirección de correo

    Pre: correo es una cadena válida y contiene @

    Post: devuelve la parte del dominio en minúsculas

    """

    assert "@" in correo, "El correo debe contener '@'."
    return correo.split("@")[1].lower()


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: el usuario ingresa direcciones de correo o una cadena vacía para finalizar

    Post: muestra los dominios válidos sin repetir, en orden alfabético

    """

    dominios: list[str] = []

    while True:
        correo = input("Ingrese una dirección de correo (o vacío para salir): ").strip()

        if correo == "":
            break

        try:
            if es_valido(correo):
                dominio = obtener_dominio(correo)
                dominios.append(dominio)
                print("Correo válido")
            else:
                print("Correo inválido")
        except Exception as e:
            print("Ocurrió un error al validar el correo:", e)
        finally:
            print("--- Validación finalizada para este intento ---")

    # Elimina duplicados y ordena alfabéticamente
    dominios_unicos = sorted({d for d in dominios})

    print("\nDominios encontrados:")
    for d in dominios_unicos:
        print("-", d)


if __name__ == "__main__":
    main()
