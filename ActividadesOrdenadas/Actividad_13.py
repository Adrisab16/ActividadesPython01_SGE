# Ejercicio 13:

def mas_larga(lista):
    return max(lista, key=len)

palabras = ["manzana", "platano", "fresa", "kiwi"]
print("Palabra más larga:", mas_larga(palabras))
