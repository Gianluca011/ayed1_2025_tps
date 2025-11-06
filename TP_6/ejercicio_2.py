# Divide un archivo de texto en partes sin cargarlo completamente en memoria
def dividir_archivo(nombre_archivo: str, tamano_maximo: int) -> None:
    """División de archivo de texto en partes

    Pre: recibe el nombre de un archivo de texto existente y un tamaño máximo para las partes

    Post: crea varios archivos nuevos, numerados secuencialmente, que contienen el contenido del archivo original
        sin dividir ningún registro

    """

    assert isinstance(nombre_archivo, str), "El nombre del archivo debe ser una cadena."
    assert isinstance(tamano_maximo, int), "El tamaño máximo debe ser un entero."
    assert tamano_maximo > 0, "El tamaño máximo debe ser mayor que cero."

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            parte = 1
            bytes_actuales = 0
            nombre_base, extension = (
                nombre_archivo.rsplit(".", 1)
                if "." in nombre_archivo
                else (nombre_archivo, "")
            )
            archivo_salida = open(
                f"{nombre_base}_parte{parte}.{extension}", "w", encoding="utf-8"
            )

            for linea in archivo:
                bytes_linea = len(linea.encode("utf-8"))
                # Si agregar esta línea supera el límite, crea un nuevo archivo
                if bytes_actuales + bytes_linea > tamano_maximo:
                    archivo_salida.close()
                    parte += 1
                    archivo_salida = open(
                        f"{nombre_base}_parte{parte}.{extension}", "w", encoding="utf-8"
                    )
                    bytes_actuales = 0
                archivo_salida.write(linea)
                bytes_actuales += bytes_linea

            archivo_salida.close()

    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    except PermissionError:
        print(
            f"Error: no se tiene permiso para leer o escribir el archivo '{nombre_archivo}'."
        )
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        # Cerramos el archivo si quedó abierto por algún motivo
        try:
            archivo_salida.close()
        except:
            pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: llama a la función dividir_archivo() con los valores ingresados y muestra un
        mensaje indicando si la división fue exitosa o si ocurrió algún error

    """

    try:
        nombre = input("Ingrese el nombre del archivo a dividir: ").strip()
        tamano = int(input("Ingrese el tamaño máximo (en bytes) por parte: "))
        dividir_archivo(nombre, tamano)
        print("División completada correctamente.")
    except ValueError:
        print("Error: el tamaño máximo debe ser un número entero válido.")


if __name__ == "__main__":
    main()
