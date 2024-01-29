# Ejercicio 14:

cadena = input("Ingrese una cadena: ")
mayusculas = sum(1 for letra in cadena if letra.isupper())
print("Número de letras mayúsculas:", mayusculas)
