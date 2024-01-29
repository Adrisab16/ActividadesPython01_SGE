# Ejercicio 8:

suma_impares = 0

for num in range(51):
    if num % 2 != 0:
        print(num)
        suma_impares += num

print("Suma de los números impares:", suma_impares)
