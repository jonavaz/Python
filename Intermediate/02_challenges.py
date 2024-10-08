### Challenges ###

"""
 EL FAMOSO "FIZZ BUZZ":
 
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

def is_3_multiply(number):
    auxB = False
    aux = number%3
    if(0 == aux):
        auxB = True
    else:
        auxB = False
    return auxB

def is_5_multiply(number):
    auxB = False
    aux = number%5
    if(0 == aux):
        auxB = True
    else:
        auxB = False
    return auxB

def is_3_and_5_multiply(number):
    aux35 = False
    aux3 = is_3_multiply(number)
    aux5 = is_5_multiply(number)

    if((True == aux3) and (True == aux5)):
        aux35 = True
    else:
        aux35 = False
    return aux35

def fizzbuzz():
    my_list = list(range(1,101))
    print(my_list)

    for i in my_list:
        multy35 = is_3_and_5_multiply(i)
        multy3 = is_3_multiply(i)
        multy5 = is_5_multiply(i)
        if(True == multy35):
            print("Fizzbuzz")
        elif(True == multy3):
            print("Fizz")
        elif(True == multy5):
            print("Buzz")
        else:
            print("%d" %i)

fizzbuzz()

"""
¿ES UN ANAGRAMA?

 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
 """
def is_anagram(word_one, word_two):
    isAnagram = False
    if word_one.lower() == word_two.lower():
        isAnagram = False
    elif sorted(word_one.lower()) == sorted(word_two.lower()):
        isAnagram = True
    else:
        isAnagram = False
        #print("No deberia de entrar aqui")

    return isAnagram

def isYesOrNo(aux):
    if(True == aux):
        res = "Si"
    else:
        res = "No"   
    return res 

aux = is_anagram("altisonancia", "Nacionalista")
res = isYesOrNo(aux)

print("Son anagramas? %s" %res)

"""
LA SUCESIÓN DE FIBONACCI

 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
"""

def Fibonacci():
    count = 0
    prev = 0
    next = 1
    while count < 50:
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        count += 1
    
Fibonacci()

"""
ES UN NÚMERO PRIMO

 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_odd(number):
    isNotOdd = False
    if 2 <= number:
        for index in range(2,number):
            if 0 == number % index:
                isNotOdd = True
                break
    else:
        isNotOdd = True

    return isNotOdd

def printIsOdd():
    count = 1
    while 101 > count:
        aux = is_odd(count)
        if False == aux:
            print("El número %d es primo" %count)
        count += 1

printIsOdd()