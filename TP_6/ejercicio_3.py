# Permite registrar alturas de atletas por disciplina, calcular promedios
# y mostrar las disciplinas cuyos atletas superan la altura promedio general
def GrabarRangoAlturas(nombre_archivo: str) -> None:
    """Grabación de alturas de atletas por deporte

    Pre: recibe el nombre de un archivo donde se grabarán las alturas

    Post: graba en el archivo los deportes y las alturas de los atletas

    """

    assert isinstance(nombre_archivo, str), "El nombre del archivo debe ser una cadena."

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            while True:
                deporte = input(
                    "Ingrese el nombre del deporte (ENTER para finalizar): "
                ).strip()
                if deporte == "":
                    break
                archivo.write(deporte + "\n")

                while True:
                    altura = input(
                        "Ingrese altura del atleta (ENTER para pasar al siguiente deporte): "
                    ).strip()
                    if altura == "":
                        break
                    try:
                        altura_num = float(altura)
                        archivo.write(str(altura_num) + "\n")
                    except ValueError:
                        print("Altura inválida, intente nuevamente.")
        print(f"Datos guardados correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error al grabar el archivo: {e}")


def GrabarPromedio(nombre_archivo_alturas: str, nombre_archivo_promedios: str) -> None:
    """Cálculo y grabación de promedios por deporte

    Pre: recibe el nombre del archivo con alturas y el nombre del archivo destino para los promedios

    Post: crea un nuevo archivo donde se graba el nombre de cada deporte y su promedio de alturas

    """

    assert isinstance(
        nombre_archivo_alturas, str
    ), "El nombre del archivo de alturas debe ser una cadena."
    assert isinstance(
        nombre_archivo_promedios, str
    ), "El nombre del archivo de promedios debe ser una cadena."

    try:
        with open(nombre_archivo_alturas, "r", encoding="utf-8") as archivo_in, open(
            nombre_archivo_promedios, "w", encoding="utf-8"
        ) as archivo_out:

            deporte = None
            alturas = []

            for linea in archivo_in:
                linea = linea.strip()
                if linea == "":
                    continue
                if not linea.replace(".", "", 1).isdigit():
                    if deporte and alturas:
                        promedio = sum(alturas) / len(alturas)
                        archivo_out.write(f"{deporte}\n{promedio:.2f}\n")
                    deporte = linea
                    alturas = []
                else:
                    alturas.append(float(linea))

            if deporte and alturas:
                promedio = sum(alturas) / len(alturas)
                archivo_out.write(f"{deporte}\n{promedio:.2f}\n")

        print(f"Promedios grabados correctamente en '{nombre_archivo_promedios}'.")
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo_alturas}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al calcular los promedios: {e}")


def MostrarMasAltos(nombre_archivo_promedios: str) -> None:
    """Mostrar disciplinas con atletas más altos que el promedio general

    Pre: recibe el nombre de un archivo con los promedios por deporte

    Post: muestra por pantalla las disciplinas cuyos promedios superan
            la estatura promedio general entre todos los deportes

    """

    assert isinstance(
        nombre_archivo_promedios, str
    ), "El nombre del archivo debe ser una cadena."

    try:
        with open(nombre_archivo_promedios, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip() != ""]

        deportes = lineas[::2]
        promedios = [float(x) for x in lineas[1::2]]

        if not promedios:
            print("No hay datos disponibles.")
            return

        promedio_general = sum(promedios) / len(promedios)
        print(f"\nPromedio general de alturas: {promedio_general:.2f}")

        print("Deportes con atletas más altos que el promedio general:")
        [
            print(f"- {deportes[i]} ({promedios[i]:.2f})")
            for i in range(len(deportes))
            if promedios[i] > promedio_general
        ]

    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo_promedios}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """
    
    try:
        archivo_alturas = "alturas.txt"
        archivo_promedios = "promedios.txt"

        GrabarRangoAlturas(archivo_alturas)
        GrabarPromedio(archivo_alturas, archivo_promedios)
        MostrarMasAltos(archivo_promedios)

    except Exception as e:
        print(f"Ocurrió un error en el programa principal: {e}")
    finally:
        print("--- Programa finalizado ---")


if __name__ == "__main__":
    main()
