# Elimina todos los comentarios de un archivo Python
def eliminar_comentarios(nombre_entrada: str, nombre_salida: str) -> None:
    """Eliminación de comentarios de un archivo Python

    Pre: recibe el nombre de un archivo .py de entrada y otro de salida

    Post: genera un nuevo archivo sin comentarios ni docstrings

    """

    assert isinstance(nombre_entrada, str), "El nombre de entrada debe ser una cadena."
    assert isinstance(nombre_salida, str), "El nombre de salida debe ser una cadena."

    try:
        with open(nombre_entrada, "r", encoding="utf-8") as archivo_in, open(
            nombre_salida, "w", encoding="utf-8"
        ) as archivo_out:

            dentro_docstring = False

            for linea in archivo_in:
                linea = linea.rstrip("\n")

                if '"""' in linea or "'''" in linea:
                    if linea.count('"""') == 2 or linea.count("'''") == 2:
                        continue
                    dentro_docstring = not dentro_docstring
                    continue

                if dentro_docstring:
                    continue

                nueva_linea = ""
                dentro_cadena = False
                comillas = ""

                for i, caracter in enumerate(linea):
                    if caracter in ("'", '"'):
                        if not dentro_cadena:
                            dentro_cadena = True
                            comillas = caracter
                        elif caracter == comillas:
                            dentro_cadena = False
                    elif caracter == "#" and not dentro_cadena:
                        break
                    nueva_linea += caracter

                if nueva_linea.strip() != "":
                    archivo_out.write(nueva_linea.rstrip() + "\n")

        print(f"Archivo '{nombre_salida}' generado sin comentarios correctamente.")
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_entrada}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
    finally:
        print("--- Proceso finalizado ---")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: crea un nuevo archivo .py sin comentarios ni docstrings

    """

    try:
        entrada = input("Ingrese el nombre del archivo Python de entrada: ").strip()
        salida = input("Ingrese el nombre del archivo de salida: ").strip()
        eliminar_comentarios(entrada, salida)
    except Exception as e:
        print(f"Error en el programa principal: {e}")
    finally:
        print("--- Programa finalizado ---")


if __name__ == "__main__":
    main()
