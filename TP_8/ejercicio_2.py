# Convierte una fecha en formato extendido según el año de corte
def fecha_a_texto(fecha: tuple[int, int, int]) -> str:
    """Conversión de una fecha a formato extendido

    Pre: el año puede tener 2 o 4 dígitos, si tiene 2 dígitos, se interpreta según un año de corte

    Post: devuelve una cadena de texto con la fecha en formato extendido

    """

    assert (
        isinstance(fecha, tuple) and len(fecha) == 3
    ), "Debe ingresarse una tupla con tres elementos."
    dia, mes, anio = fecha
    assert 1 <= dia <= 31, "El día debe estar entre 1 y 31."
    assert 1 <= mes <= 12, "El mes debe estar entre 1 y 12."

    try:
        meses = (
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        )

        ANIO_CORTE = 30

        if anio < 100:
            if anio <= ANIO_CORTE:
                anio += 2000
            else:
                anio += 1900

        return f"{dia} de {meses[mes - 1]} de {anio}"

    except Exception as e:
        print(f"Error al procesar la fecha: {e}")
        return "Fecha inválida."
    finally:
        pass


# Permite ingresar una fecha
def ingresar_fecha() -> tuple[int, int, int]:
    """Ingreso de una fecha

    Pre: el usuario ingresa día, mes y año como números enteros

    Post: devuelve una tupla

    """

    try:
        dia = int(input("Ingrese día: "))
        mes = int(input("Ingrese mes: "))
        anio = int(input("Ingrese año (2 o 4 dígitos): "))
        return (dia, mes, anio)
    except ValueError:
        print("Error: debe ingresar solo números.")
        return (1, 1, 2000)
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """

    print("--- Fecha en formato extendido ---")

    try:
        fecha = ingresar_fecha()
        texto = fecha_a_texto(fecha)
        print("Fecha en formato extendido:", texto)
    except Exception:
        print("Ocurrió un error en la ejecución.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
