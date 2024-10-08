print('Hola mundo!')
"""
# -----------------------------------------------------------------------------------------------------------
edad = 20

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 60:
    print("Eres un adulto.")
elif edad > 15:
    print("Mayor de 15 años.")
elif edad == 60:
    print("¡Feliz 60 cumpleaños!")
else:
        print("Eres adulto mayor.")
# -----------------------------------------------------------------------------------------------------------
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

contador = 0
while contador < 5:

    print(contador)
    contador += 1
# -----------------------------------------------------------------------------------------------------------
print("Número del 1 al 5 multiplicados por 2 con bucle for")
for numero in range(1, 6):
     print(numero*2)

print("Número del 1 al 5 multiplicados por 2 con bucle while")
contador=1
while contador <= 5:
     print(contador*2)
     contador += 1
# -----------------------------------------------------------------------------------------------------------
print("Número del 0 al 4 con bucle while y break")
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("Operador modulo con bucle for y continue")
for i in range(10):
     if 0 == (i % 2):
          continue
     print(i)

# -----------------------------------------------------------------------------------------------------------
# Lista de comprensión
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 1]
print(cuadrados)  # Imprime [4, 16]
# -----------------------------------------------------------------------------------------------------------
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]
print(frutas[0])  # Imprime "uva"
# -----------------------------------------------------------------------------------------------------------
#Diccionarios
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

# -----------------------------------------------------------------------------------------------------------
# Conjuntos o set
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5, 6}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}
interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}
diferencia1 = conjunto1 - conjunto2
print(diferencia1)  # Imprime {1, 2}
diferencia2 = conjunto2 - conjunto1
print(diferencia2)  # Imprime {4, 5, 6}
diferencia3 = conjunto2 - conjunto2
print(diferencia3)  # Imprime {4, 5, 6}
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}
print(diferencia2|diferencia1)  # Imprime {1, 2, 4, 5}

frutas = {"manzana", "banana", "naranja"}
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.clear()
print(frutas)  # Imprime set()

# -----------------------------------------------------------------------------------------------------------
# Función Lambda
square = lambda x: x ** 2
print(square(5))  # Prints 25

# -----------------------------------------------------------------------------------------------------------
# Argumento variables
def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(variable_sum(1, 2, 3))  # Prints 6
print(variable_sum(4, 5, 6, 7))  # Prints 22

# -----------------------------------------------------------------------------------------------------------
# Errores en Python
list = [1, 2, 3]
print(list[-4])  # Index 3 is out of range
"""
# -----------------------------------------------------------------------------------------------------------
# Try, Except and Finally
try:
    # Code that may generate an exception
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")

try:
    # Code that may generate an exception
    file = open("file.txt", "r")
    # Perform operations with the file
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Clousing file.")
    file.close()  # Always close the file, even if an exception occurs