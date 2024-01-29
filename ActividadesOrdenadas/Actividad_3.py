# Ejercicio 3:

Frutas = ["manzana", "platano", "fresa"]
print("Segundo ítem:", Frutas[1])

if "patata" not in Frutas:
    print("Patata no es una fruta")

Frutas[0] = "kiwi"
Frutas.append("naranja")
Frutas.insert(2, "limón")
Frutas.remove("fresa")

print("Ítems de la lista:")
for fruta in Frutas:
    print(fruta)
