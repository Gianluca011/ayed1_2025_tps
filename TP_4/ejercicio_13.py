# Función auxiliar para convertir números menores a 1000
def convertir_menor_mil(n: int) -> str:
    """Convertir número menor a mil

    Pre: 0 menor o igual a n y menor que 1000

    Post: devuelve la representación en letras del número

    """

    unidades = [
        "",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    especiales = [
        "diez",
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    ]
    decenas = [
        "",
        "",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    centenas = [
        "",
        "ciento",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]

    if n == 0:
        return ""
    if n == 100:
        return "cien"

    c, d, u = n // 100, (n % 100) // 10, n % 10
    texto = centenas[c]

    if 10 <= n % 100 < 20:
        texto += " " + especiales[n % 100 - 10]
    else:
        if d > 0:
            texto += " " + decenas[d]
            if d == 2 and u > 0:
                texto = texto[:-1] + "i"  # veinte -> veinti
        if u > 0 and not (10 <= n % 100 < 20):
            texto += " y " + unidades[u] if d >= 3 else unidades[u]

    return texto.strip()


# Convierte un número entero a letras
def numero_a_letras(n: int) -> str:
    """Convertir número entero a letras

    Pre: 0 menor o igual que n y menor o igual que 1_000_000_000_000

    Post: devuelve el número en forma escrita en español

    """

    try:
        assert isinstance(n, int), "El número debe ser entero"
        assert 0 <= n <= 1_000_000_000_000, "Número fuera de rango"

        if n == 0:
            return "cero"
        if n == 1_000_000_000_000:
            return "un billón"

        partes = []
        grupos = ["", "mil", "millón", "mil millones"]
        grupo_millon = ["", "millón", "millones"]

        miles = []
        while n > 0:
            miles.append(n % 1000)
            n //= 1000

        for i, grupo in enumerate(miles):
            if grupo == 0:
                continue
            texto_grupo = convertir_menor_mil(grupo)
            if i == 1 and grupo == 1:
                partes.append("mil")
            elif i == 2:
                partes.append("un millón" if grupo == 1 else f"{texto_grupo} millones")
            elif i == 3:
                partes.append(f"{texto_grupo} mil millones")
            else:
                partes.append(texto_grupo)

        return " ".join(reversed(partes)).strip()

    except AssertionError as ae:
        return f"Error: {ae}"
    except Exception as e:
        return f"Error inesperado: {e}"
    finally:
        pass


# Programa para ejecutar la función
def main() -> None:
    """Programa núcleo

    Pre: no recibe parámetros

    Post: pide un número entero al usuario y muestra su versión en letras

    """

    try:
        numero = int(input("Ingrese un número entre 0 y 1 billón: "))
        resultado = numero_a_letras(numero)
        print("En letras:", resultado)
    except ValueError:
        print("Error: debe ingresar un número entero.")
    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
