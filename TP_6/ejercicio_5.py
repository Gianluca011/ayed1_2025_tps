import csv


# Conversión de archivos de texto con formato a CSV
def convertir_formato1(origen: str, destino: str) -> None:
    """Conversión de archivo con formato 1 a CSV

    Pre: recibe el nombre de un archivo de texto con registros de longitud fija
            separados por espacios

    Post: genera un archivo CSV con los mismos datos, eliminando espacios innecesarios

    """

    assert isinstance(origen, str), "El nombre del archivo origen debe ser una cadena."
    assert isinstance(
        destino, str
    ), "El nombre del archivo destino debe ser una cadena."

    try:
        with open(origen, "r", encoding="utf-8") as entrada, open(
            destino, "w", newline="", encoding="utf-8"
        ) as salida:
            escritor = csv.writer(salida)
            for linea in entrada:
                linea = linea.strip()
                if not linea:
                    continue
                partes = [campo for campo in linea.split(" ") if campo != ""]
                apellido_nombre = " ".join(partes[0:2])
                fecha = partes[2]
                domicilio = " ".join(partes[3:])
                escritor.writerow(
                    [apellido_nombre.strip(), fecha.strip(), domicilio.strip()]
                )
        print(f"Archivo '{destino}' generado correctamente desde formato 1.")
    except FileNotFoundError:
        print(f"Error: el archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
    finally:
        print("Conversión desde formato 1 finalizada.")


# --- Función para convertir desde formato 2 ---
def convertir_formato2(origen: str, destino: str) -> None:
    """Conversión de archivo con formato 2 a CSV

    Pre: recibe el nombre de un archivo de texto con registros en los que cada campo
            está precedido por un número de dos dígitos que indica su longitud

    Post: genera un archivo CSV con los mismos datos, leyendo dinámicamente los campos

    """

    assert isinstance(origen, str), "El nombre del archivo origen debe ser una cadena."
    assert isinstance(
        destino, str
    ), "El nombre del archivo destino debe ser una cadena."

    try:
        with open(origen, "r", encoding="utf-8") as entrada, open(
            destino, "w", newline="", encoding="utf-8"
        ) as salida:
            escritor = csv.writer(salida)

            for linea in entrada:
                linea = linea.strip()
                if not linea:
                    continue

                campos = []
                i = 0
                while i < len(linea):
                    longitud = int(linea[i : i + 2])
                    i += 2
                    campo = linea[i : i + longitud].strip()
                    campos.append(campo)
                    i += longitud

                escritor.writerow(campos)

        print(f"Archivo '{destino}' generado correctamente desde formato 2.")
    except FileNotFoundError:
        print(f"Error: el archivo '{origen}' no existe.")
    except ValueError:
        print("Error: formato de archivo inválido. Verifique los datos.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
    finally:
        print("Conversión desde formato 2 finalizada.")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: el usuario elige el formato 1 o 2 e ingresa los nombres de los archivos

    Post: convierte el archivo de texto al formato CSV correspondiente

    """

    try:
        print("--- Conversor de Archivos a CSV ---")
        formato = input("Ingrese el formato del archivo (1 o 2): ").strip()
        origen = input("Ingrese el nombre del archivo de entrada: ").strip()
        destino = input("Ingrese el nombre del archivo de salida (.csv): ").strip()

        if formato == "1":
            convertir_formato1(origen, destino)
        elif formato == "2":
            convertir_formato2(origen, destino)
        else:
            print("Formato inválido. Debe ser '1' o '2'.")
    except Exception as e:
        print(f"Error en la ejecución principal: {e}")
    finally:
        print("--- Programa finalizado ---")


if __name__ == "__main__":
    main()
