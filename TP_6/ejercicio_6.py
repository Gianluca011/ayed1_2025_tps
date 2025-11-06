import csv
import os
import random
from datetime import datetime
from typing import List, Dict, Optional


ARCHIVO = "huespedes.csv"
PISOS = 10
HABITACIONES_POR_PISO = 6


# Registra huéspedes interactuando por teclado y guarda en CSV
def registrar_huespedes(nombre_archivo: str = ARCHIVO) -> None:
    """Registro de huéspedes en archivo CSV

    Pre: nombre_archivo es una cadena con el nombre del archivo destino

    Post: crea o sobrescribe nombre_archivo con los registros ingresados

    """

    assert isinstance(nombre_archivo, str), "El nombre del archivo debe ser cadena."

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["DNI", "ApellidoNombre", "FechaIngreso", "FechaEgreso", "Ocupantes"]
            )

            while True:
                try:
                    raw = input("Ingrese DNI del huésped (-1 para finalizar): ").strip()
                    if raw == "":
                        print("DNI vacío, intente nuevamente.")
                        continue
                    dni = int(raw)
                except ValueError:
                    print("DNI inválido. Debe ser un número entero.")
                    continue

                if dni == -1:
                    break

                apellido_nombre = input("Apellido y Nombre: ").strip()
                if apellido_nombre == "":
                    print("Apellido y Nombre vacío. Intente nuevamente.")
                    continue

                fecha_ingreso = input("Fecha de ingreso (DDMMAAAA): ").strip()
                fecha_egreso = input("Fecha de egreso (DDMMAAAA): ").strip()

                try:
                    fi = datetime.strptime(fecha_ingreso, "%d%m%Y")
                    fe = datetime.strptime(fecha_egreso, "%d%m%Y")
                    if fe <= fi:
                        print(
                            "Error: la fecha de egreso debe ser posterior a la de ingreso."
                        )
                        continue
                except ValueError:
                    print("Formato de fecha incorrecto. Use DDMMAAAA.")
                    continue

                try:
                    ocupantes = int(input("Cantidad de ocupantes: ").strip())
                    if ocupantes <= 0:
                        print("La cantidad de ocupantes debe ser mayor que 0.")
                        continue
                except ValueError:
                    print("Cantidad de ocupantes inválida. Debe ser un entero.")
                    continue

                try:
                    if os.path.exists(nombre_archivo):
                        with open(nombre_archivo, newline="", encoding="utf-8") as fr:
                            reader = csv.DictReader(fr)
                            dnis = {row["DNI"] for row in reader}
                    else:
                        dnis = set()
                except Exception:
                    dnis = set()

                if str(dni) in dnis:
                    print("Error: DNI repetido. No se permite duplicado.")
                    continue

                writer.writerow(
                    [dni, apellido_nombre, fecha_ingreso, fecha_egreso, ocupantes]
                )
                print("✅ Huésped registrado correctamente.\n")

    except PermissionError:
        print(f"Error: permisos insuficientes para escribir '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al registrar huéspedes: {e}")
    finally:
        print("Proceso de registro finalizado.\n")


# Lee el archivo CSV de huéspedes y devuelve la lista de registros.
def leer_huespedes(nombre_archivo: str = ARCHIVO) -> List[Dict[str, str]]:
    """Lectura de registros de huéspedes

    Pre: nombre_archivo es una cadena con la ruta del CSV generado por registrar_huespedes

    Post: devuelve una lista de diccionarios con las claves

    """

    assert isinstance(nombre_archivo, str), "El nombre del archivo debe ser cadena."

    registros: List[Dict[str, str]] = []
    try:
        if not os.path.exists(nombre_archivo):
            print(f"Advertencia: '{nombre_archivo}' no encontrado.")
            return registros

        with open(nombre_archivo, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                registros.append(row)
    except Exception as e:
        print(f"Error al leer huéspedes: {e}")
    finally:
        return registros


# Asigna piso y habitación aleatoriamente sin repetir habitaciones
def asignar_habitaciones(huespedes: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Asignación de habitaciones

    Pre: huespedes es una lista de diccionarios leídos de leer_huespedes, sin campos 'Piso' ni 'Habitacion'

    Post: devuelve la misma lista con claves adicionales 'Piso' y 'Habitacion' asignadas

    """

    assert isinstance(huespedes, list), "huespedes debe ser una lista."

    try:
        ocupadas = set()
        for h in huespedes:
            assert "DNI" in h and "Ocupantes" in h, "Registro con formato inválido."

        # Asignar aleatoriamente una habitación libre
        for h in huespedes:
            intentos = 0
            while True:
                intentos += 1
                if intentos > 1000:
                    raise RuntimeError(
                        "No se pudo asignar habitación (sin habitaciones libres)."
                    )
                piso = random.randint(1, PISOS)
                habitacion = random.randint(1, HABITACIONES_POR_PISO)
                if (piso, habitacion) not in ocupadas:
                    ocupadas.add((piso, habitacion))
                    h["Piso"] = piso
                    h["Habitacion"] = habitacion
                    break
        return huespedes
    except Exception as e:
        print(f"Error en asignar_habitaciones: {e}")
        return huespedes
    finally:
        pass


# Devuelve el número de piso con más habitaciones ocupadas
def piso_con_mas_ocupadas(huespedes: List[Dict[str, str]]) -> Optional[int]:
    """Piso con mayor cantidad de habitaciones ocupadas

    Pre: huespedes es la lista devuelta por asignar_habitaciones con claves 'Piso'

    Post: devuelve el número de piso con más habitaciones ocupadas o None si no hay datos

    """

    assert isinstance(huespedes, list), "Huespedes debe ser una lista."
    try:
        conteo = {}
        for h in huespedes:
            piso = h.get("Piso")
            if piso is None:
                continue
            conteo[piso] = conteo.get(piso, 0) + 1
        if not conteo:
            return None
        # devolver el piso (clave) con máximo valor
        return max(conteo, key=conteo.get)
    except Exception as e:
        print(f"Error en piso_con_mas_ocupadas: {e}")
        return None
    finally:
        pass


# Calcula cuántas habitaciones vacías quedan en todo el hotel
def habitaciones_vacias(huespedes: List[Dict[str, str]]) -> int:
    """Cantidad de habitaciones vacías

    Pre: huespedes es la lista de huéspedes con habitaciones asignadas

    Post: devuelve el número de habitaciones desocupadas en todo el hotel

    """

    assert isinstance(huespedes, list), "Huespedes debe ser una lista."
    try:
        ocupadas = len([h for h in huespedes if "Piso" in h and "Habitacion" in h])
        total = PISOS * HABITACIONES_POR_PISO
        return total - ocupadas
    except Exception as e:
        print(f"Error en habitaciones_vacias: {e}")
        return PISOS * HABITACIONES_POR_PISO
    finally:
        pass


# Devuelve el piso con mayor cantidad de personas
def piso_con_mas_personas(huespedes: List[Dict[str, str]]) -> Optional[int]:
    """Piso con mayor número de personas alojadas

    Pre: huespedes contiene el campo 'Piso' y 'Ocupantes' por registro

    Post: devuelve el número de piso con mayor suma de ocupantes o None si no hay datos

    """

    assert isinstance(huespedes, list), "huespedes debe ser una lista."
    try:
        conteo = {}
        for h in huespedes:
            piso = h.get("Piso")
            try:
                ocup = int(h.get("Ocupantes", 0))
            except (TypeError, ValueError):
                ocup = 0
            if piso is None:
                continue
            conteo[piso] = conteo.get(piso, 0) + ocup
        if not conteo:
            return None
        return max(conteo, key=conteo.get)
    except Exception as e:
        print(f"Error en piso_con_mas_personas: {e}")
        return None
    finally:
        pass


# Muestra la próxima habitación que se desocupara según la fecha actual ingresada
def proxima_habitacion_desocupada(huespedes: List[Dict[str, str]]) -> None:
    """Próxima habitación en desocuparse

    Pre: huespedes tiene registros con 'FechaEgreso' y campos 'Piso','Habitacion'

    Post: pide la fecha actual al usuario y muestra la o las habitaciones que se desocuparán primero

    """

    assert isinstance(huespedes, list), "Huespedes debe ser una lista."
    try:
        fecha_actual_raw = input("Ingrese la fecha actual (DDMMAAAA): ").strip()
        try:
            fecha_actual = datetime.strptime(fecha_actual_raw, "%d%m%Y")
        except ValueError:
            print("Fecha actual con formato incorrecto.")
            return

        eventos = []
        for h in huespedes:
            fe_raw = h.get("FechaEgreso")
            if not fe_raw:
                continue
            try:
                fe = datetime.strptime(fe_raw, "%d%m%Y")
            except ValueError:
                continue
            if fe >= fecha_actual:
                eventos.append((fe, h))

        if not eventos:
            print("No hay habitaciones próximas a desocuparse.")
            return

        eventos.sort(key=lambda x: x[0])
        primer_fecha = eventos[0][0]
        próximos = [item[1] for item in eventos if item[0] == primer_fecha]

        print(f"\nPróxima fecha de desocupación: {primer_fecha.strftime('%d/%m/%Y')}")
        for h in próximos:
            print(
                f"- Piso {h.get('Piso')}, Habitación {h.get('Habitacion')}, DNI: {h.get('DNI')}"
            )

    except Exception as e:
        print(f"Error en proxima_habitacion_desocupada: {e}")
    finally:
        pass


# Muestra todos los huéspedes ordenados por DNI
def mostrar_todos(huespedes: List[Dict[str, str]]) -> None:
    """Mostrar listado completo de huéspedes

    Pre: huespedes es la lista con registros y campos de identificación y asignación

    Post: imprime por pantalla todos los huéspedes ordenados por DNI con sus datos principales

    """

    assert isinstance(huespedes, list), "Huespedes debe ser una lista."
    try:
        ordenados = sorted(huespedes, key=lambda r: int(r.get("DNI", 0)))
        print("\nListado de huéspedes (ordenado por DNI):")
        for h in ordenados:
            print(
                f"DNI: {h.get('DNI')}, Nombre: {h.get('ApellidoNombre')}, Piso: {h.get('Piso')}, "
                f"Habitación: {h.get('Habitacion')}, Ingreso: {h.get('FechaIngreso')}, "
                f"Egreso: {h.get('FechaEgreso')}, Ocupantes: {h.get('Ocupantes')}"
            )
    except Exception as e:
        print(f"Error en mostrar_todos: {e}")
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa nucleo

    Pre: no recibe parámetros

    Post: muestra los resultados de las funciones por pantalla

    """

    try:
        registrar_huespedes(ARCHIVO)
        huespedes = leer_huespedes(ARCHIVO)
        if not huespedes:
            print("No se encontraron huéspedes. Finalizando.")
            return

        huespedes = asignar_habitaciones(huespedes)

        piso_mas = piso_con_mas_ocupadas(huespedes)
        if piso_mas is None:
            print("No hay datos para determinar el piso con más ocupadas.")
        else:
            print(f"\na) Piso con más habitaciones ocupadas: {piso_mas}")

        vacias = habitaciones_vacias(huespedes)
        print(f"b) Habitaciones vacías en el hotel: {vacias}")

        piso_personas = piso_con_mas_personas(huespedes)
        if piso_personas is None:
            print("No hay datos para determinar el piso con más personas.")
        else:
            print(f"c) Piso con mayor cantidad de personas: {piso_personas}")

        proxima_habitacion_desocupada(huespedes)
        mostrar_todos(huespedes)

    except Exception as e:
        print(f"Error en main: {e}")
    finally:
        print("--- Programa finalizado ---")


if __name__ == "__main__":
    main()
