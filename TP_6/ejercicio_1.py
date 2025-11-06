# Clasifica apellidos según su terminación y los guarda en distintos archivos
def clasificar_apellidos(nombre_archivo: str) -> None:
    """Clasificación de apellidos por terminación

    Pre: recibe el nombre de un archivo de texto existente que contiene líneas con nombres en el formato "Apellido, Nombre"

    Post: crea o sobrescribe tres archivos, guardando en cada uno los nombres cuyo apellido termina en ian, ini, ez,
        los apellidos con otras terminaciones son descartados

    """

    assert isinstance(nombre_archivo, str), "El nombre del archivo debe ser una cadena."

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]

        # Abrimos los archivos de salida
        archivos_salida = {
            "IAN": open("ARMENIA.TXT", "w", encoding="utf-8"),
            "INI": open("ITALIA.TXT", "w", encoding="utf-8"),
            "EZ": open("ESPAÑA.TXT", "w", encoding="utf-8"),
        }

        for persona in lineas:
            try:
                apellido, nombre = persona.split(",")
                apellido = apellido.strip().upper()
                nombre = nombre.strip()
            except ValueError:
                print(f"Formato incorrecto: {persona}")
                continue

            if apellido.endswith("IAN"):
                archivos_salida["IAN"].write(persona + "\n")
            elif apellido.endswith("INI"):
                archivos_salida["INI"].write(persona + "\n")
            elif apellido.endswith("EZ"):
                archivos_salida["EZ"].write(persona + "\n")
            else:
                print(f"{persona} -> descartado")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        # Cerramos los archivos de salida si se abrieron
        for f in locals().get("archivos_salida", {}).values():
            f.close()


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: clasifica apellidos según su terminación y los guarda

    """

    nombre_archivo = input("Ingrese el nombre del archivo de texto con los apellidos: ")
    clasificar_apellidos(nombre_archivo)
    print("\nClasificación finalizada.")


if __name__ == "__main__":
    main()
