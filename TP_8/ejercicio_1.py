# Permite ingresar una fecha y valida que sea correcta
def ingresar_fecha() -> tuple[int, int, int]:
    """Ingreso y validación de una fecha

    Pre: el usuario debe ingresar día, mes y año

    Post: devuelve una tupla si la fecha es válida

    """

    while True:
        try:
            dia = int(input("Ingrese día: "))
            mes = int(input("Ingrese mes: "))
            anio = int(input("Ingrese año: "))

            assert dia > 0 and mes > 0 and anio > 0, "Los valores deben ser positivos."

            # Días máximos por mes
            dias_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

            # Verificar año bisiesto
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_mes = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

            if mes < 1 or mes > 12:
                raise ValueError("Mes inválido.")

            if dia < 1 or dia > dias_mes[mes - 1]:
                raise ValueError("Día inválido para el mes ingresado.")

            return (dia, mes, anio)

        except (ValueError, AssertionError) as e:
            print(f"Error: {e}. Intente nuevamente.")
        finally:
            pass


# Suma n días a una fecha dada
def sumar_dias(fecha: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    """Sumar días a una fecha

    Pre: fecha es una tupla válida y n es un entero

    Post: devuelve una nueva tupla resultante de sumar n días a la fecha original

    """

    assert (
        isinstance(fecha, tuple) and len(fecha) == 3
    ), "La fecha debe ser una tupla de tres elementos."
    assert isinstance(n, int), "n debe ser un número entero."

    dia, mes, anio = fecha
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajustar febrero si el año es bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_mes[1] = 29

    try:
        dia += n
        while True:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_mes[1] = 29
            else:
                dias_mes[1] = 28

            if dia > dias_mes[mes - 1]:
                dia -= dias_mes[mes - 1]
                mes += 1
                if mes > 12:
                    mes = 1
                    anio += 1
            elif dia < 1:
                mes -= 1
                if mes < 1:
                    mes = 12
                    anio -= 1
                dia += dias_mes[mes - 1]
            else:
                break
        return (dia, mes, anio)
    except Exception:
        print("Error al sumar días.")
        return fecha
    finally:
        pass


# Permite ingresar un horario y valida que sea correcto
def ingresar_horario() -> tuple[int, int]:
    """Ingreso y validación de un horario

    Pre: el usuario debe ingresar hora y minutos

    Post: devuelve una tupla si el horario es válido

    """

    while True:
        try:
            hora = int(input("Ingrese la hora: "))
            minuto = int(input("Ingrese los minutos: "))

            assert 0 <= hora < 24, "La hora debe estar entre 0 y 23."
            assert 0 <= minuto < 60, "Los minutos deben estar entre 0 y 59."

            return (hora, minuto)
        except (ValueError, AssertionError) as e:
            print(f"Error: {e}. Intente nuevamente.")
        finally:
            pass


# Calcula la diferencia en horas entre dos horarios
def diferencia_horas(h1: tuple[int, int], h2: tuple[int, int]) -> float:
    """Calcular la diferencia entre dos horarios

    Pre: h1 y h2 son tuplas válidas

    Post: devuelve la diferencia en horas entre ambos horarios

    """

    assert isinstance(h1, tuple) and isinstance(
        h2, tuple
    ), "Ambos parámetros deben ser tuplas."
    assert len(h1) == 2 and len(h2) == 2, "Cada tupla debe tener dos elementos."

    try:
        minutos1 = h1[0] * 60 + h1[1]
        minutos2 = h2[0] * 60 + h2[1]
        dif = minutos2 - minutos1

        if dif < 0:
            dif += 24 * 60

        return dif / 60
    except Exception:
        print("Error al calcular la diferencia de horarios.")
        return 0.0
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """

    print("--- Fechas y Horarios con Tuplas ---")

    try:
        print("Ingreso de fecha:")
        fecha = ingresar_fecha()
        print("Fecha válida:", fecha)

        n = int(input("Ingrese cantidad de días a sumar: "))
        nueva_fecha = sumar_dias(fecha, n)
        print(f"Fecha resultante tras sumar {n} días:", nueva_fecha)

        print("Ingreso de horarios:")
        h1 = ingresar_horario()
        h2 = ingresar_horario()
        print("Diferencia en horas:", diferencia_horas(h1, h2))

    except Exception:
        print("Ocurrió un error durante la ejecución.")
    finally:
        print("--- Fin del programa ---")


if __name__ == "__main__":
    main()
