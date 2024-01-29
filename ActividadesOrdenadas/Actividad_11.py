# Ejercicio 11:

def sumar_lista(lista):
    return sum(lista)

def multiplicar_lista(lista):
    result = 1
    for num in lista:
        result *= num
    return result

numeros = [1, 2, 3, 4]
print("Suma de la lista:", sumar_lista(numeros))
print("Multiplicación de la lista:", multiplicar_lista(numeros))
