# Ejercicio 16:

def calcular_letra_dni(dni):
    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) == 8 and dni.isdigit():
        numero_dni = int(dni)
        letra = tabla_letras[numero_dni % 23]
        print(f"La letra que corresponde al DNI introducido es: {letra} y el NIF completo es {dni}{letra}")
    else:
        print("Formato de DNI incorrecto")

dni_input = input("Introduce el DNI (formato: NNNNNNNN): ")
calcular_letra_dni(dni_input)
