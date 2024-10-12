### Error Types ###

# SyntaxError
#print "Hola comunidad!" # Remover comentario para el error
print ("!Hola comunidad!")

# NameError
language = "Spanish" # Remover comentario para el error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Remover comentario para el error

# ModuleNotFoundError
#import maths # Descomentar para error
import math

# AttributeError
#print(math.PI) # Descomentar para error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Jonathan", "Apellido":"Vazquez", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para error
print(my_dict["Apellido"])

# TypeError
#print(my_list["0"]) # Descomentar para error
print(my_list[4])

# ImportError
#from math import PI # Descomentar para error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años") # Descomentar para error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para error
print(4/2)