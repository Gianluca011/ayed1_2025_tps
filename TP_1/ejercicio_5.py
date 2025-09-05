# Función lambda para saber si un número es oblongo
# Un número es oblongo si se puede expresar como k*(k+1) para algún k natural
es_oblongo = lambda n: any(n == k * (k + 1) for k in range(1, n))

# Función lambda para saber si un número es triangular
# Un número es triangular si puede expresarse como la suma de los primeros k naturales: k*(k+1)/2
es_triangular = lambda n: any(n == k * (k + 1) // 2 for k in range(1, n))

# Ejemplo
numeros = [6, 10, 15, 21]

print("")
print("Calculadora de oblongos y triangulares")
print("")
for num in numeros:
    print(f"Número: {num}")
    print(f"Es oblongo? {es_oblongo(num)}")
    print(f"Es triangular? {es_triangular(num)}")
    print("---")