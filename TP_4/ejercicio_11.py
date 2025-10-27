from typing import List, Tuple


# Cuenta apariciones de subcadena como subsecuencia en cadena
def contar_subsecuencias(
    cadena: str, subcadena: str
) -> Tuple[int, List[Tuple[int, int]]]:
    """Contar subsecuencias

    Pre: cadena y subcadena son strings, subcadena no está vacía

    Post: devuelve (cantidad, lista_de_intervalos) donde cada intervalo
          es (índice_primer_caracter_coincidente, índice_último_caracter_coincidente)

    """

    assert isinstance(cadena, str), "cadena debe ser str"
    assert isinstance(subcadena, str), "subcadena debe ser str"
    assert subcadena != "", "subcadena no puede ser vacía"

    try:
        c = cadena.lower()
        s = subcadena.lower()
        cantidad = 0
        intervalos: List[Tuple[int, int]] = []

        # Intentamos iniciar la subsecuencia desde cada posición i de la cadena
        for i in range(len(c)):
            j = 0
            k = i
            start_index = None  # Guardamos el índice de la primera letra que coincide

            while k < len(c) and j < len(s):
                if c[k] == s[j]:
                    if start_index is None:
                        start_index = k
                    j += 1
                k += 1

            # Si j alcanzó la longitud de s, encontramos una subsecuencia
            if j == len(s) and start_index is not None:
                cantidad += 1
                intervalos.append((start_index, k - 1))

        return cantidad, intervalos

    except Exception as e:
        print("Ocurrió un error en contar_subsecuencias:", e)
        return 0, []
    finally:
        pass


# Recibe la cadena y los intervalos y devuelve la cadena con segmentos resaltados
def resaltar_intervalos(cadena: str, intervalos: List[Tuple[int, int]]) -> str:
    """Resaltar intervalos

    Pre: cadena es str y intervalos es una lista de tuplas válidas

    Post: devuelve la cadena original con segmentos envueltos en corchetes

    """

    assert isinstance(cadena, str), "cadena debe ser str"
    assert isinstance(intervalos, list), "intervalos debe ser lista de tuplas"

    try:
        n = len(cadena)
        if n == 0 or not intervalos:
            return cadena

        # Unir intervalos solapados/adyacentes
        sorted_intervals = sorted(intervalos, key=lambda x: x[0])
        merged: List[Tuple[int, int]] = []
        for s, e in sorted_intervals:
            if s < 0:
                s = 0
            if e >= n:
                e = n - 1
            if not merged:
                merged.append((s, e))
            else:
                last_s, last_e = merged[-1]
                if s <= last_e + 1:  # Si solapan o son adyacentes -> unir
                    merged[-1] = (last_s, max(last_e, e))
                else:
                    merged.append((s, e))

        # Construir la cadena con corchetes en los segmentos marcados
        resultado_chars: List[str] = []
        marker = [False] * n
        for s, e in merged:
            for idx in range(s, e + 1):
                marker[idx] = True

        i = 0
        while i < n:
            if marker[i] and (i == 0 or not marker[i - 1]):
                resultado_chars.append("[")
            resultado_chars.append(cadena[i])
            if marker[i] and (i == n - 1 or not marker[i + 1]):
                resultado_chars.append("]")
            i += 1

        return "".join(resultado_chars)

    except Exception as e:
        print("Ocurrió un error en resaltar_intervalos:", e)
        return cadena
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: muestra por pantalla la cantidad de coincidencias y la cadena con coincidencias resaltadas

    """

    texto = (
        "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría "
        "todo de algodón, que no lleva huesos. Sólo los espejos de azabache de "
        "sus ojos son duros cual dos escarabajos de cristal negro."
    )
    sub = "UADE"

    print("Texto original:\n", texto, "\n")
    try:
        cantidad, intervalos = contar_subsecuencias(texto, sub)
        print(f"Subcadena buscada: '{sub}'")
        print("Cantidad encontrada:", cantidad)
        resaltado = resaltar_intervalos(texto, intervalos)
        print("\nCoincidencias resaltadas:\n", resaltado)
    except AssertionError as ae:
        print("Error de aserción:", ae)
    except Exception as e:
        print("Error inesperado en main:", e)
    finally:
        pass


if __name__ == "__main__":
    main()
