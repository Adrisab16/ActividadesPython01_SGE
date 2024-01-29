# Ejercicio 17:

def calculadora():
    num1 = float(input("Ingrese el primer operando: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo operando: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División por cero.")
            return

    print(f"La operación es: {num1} {operador} {num2}")
    print(f"El resultado es: {resultado}")

calculadora()
