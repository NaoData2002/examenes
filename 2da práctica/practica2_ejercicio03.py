def ingresar_datos():
    while True:
        try:
            dato1 = int(input("Ingrese el primer dato: "))
            dato2 = int(input("Ingrese el segundo dato: "))
            return dato1, dato2
        except ValueError:
            print("Error: Ingrese solo valores numéricos. Intente nuevamente.")


def dividir_datos(dato1, dato2):
    while True:
        try:
            resultado = dato1 / dato2
            return resultado
        except ZeroDivisionError:
            print("Error: División entre cero. Intente nuevamente.")


def evaluar_suma(dato1, dato2):
    while True:
        try:
            resultado = dato1 + dato2
            if resultado < 10 or resultado > 20:
                raise ValueError("Error: La suma no cumple con el rango esperado (10-20).")
            return resultado
        except ValueError as e:
            print(e)
            print("Intente nuevamente.")


# Ingresar los datos
dato1, dato2 = ingresar_datos()

# Realizar la división
try:
    division = dividir_datos(dato1, dato2)
    print("Resultado de la división:", division)
except ZeroDivisionError as e:
    print(e)

# Evaluar la suma
try:
    suma = evaluar_suma(dato1, dato2)
    print("Resultado de la suma:", suma)
except ValueError as e:
<<<<<<< HEAD
    print(e)
=======
    print(e)
>>>>>>> origin/main
