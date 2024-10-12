### File Handling ###

import os

# .txt file
#txt_file = open("./my_file.txt")
txt_file = open("Intermediate/my_file.txt", "w+") # Leer y escribir con r+
txt_file.write("Mi nombre es Jonathan\nMi apellido es Vazquez\n34 años\nY mi lenguaje preferido es Python")

txt_file.seek(0)
#txt_file.read()
print(txt_file.read(10))

print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readline())

# Iterar por todas las líneas del archivo
for line in txt_file.readlines():
    print(line)

#txt_file.write("\nAunque tambien me gusta C")
print(txt_file.readline())

txt_file.close()
 
#os.remove("Intermediate/my_file.txt")

# .json file
print("FIN DE ARCHIVOS DE TEXTO\n")

import json
print("INICIO DE ARCHIVOS JSON")

json_file = open("Intermediate/my_file.json", "w+") # Leer y escribir
json_test = {"name":"Jonathan",
             "surname":"Vázquez",
             "age":34,
             "languages":["Python", "C", "C++"],
             "website":"www.//moure.dev"}

json.dump(json_test, json_file, indent = 2) # indent sirve para poner cada key con su valor en una nueva línea y con el valor de espacios de indent al inicio de cada línea
json_file.seek(0)

for line in json_file.readlines():
    print(line)

json_file.seek(0)
json_dict = json.load(json_file)
print(json_dict)
print(type(json_dict))
print(json_dict["languages"])

json_file.close()

# *.csv files
import csv

csv_file = open("Intermediate/my_file.csv", "w+") # Leer y escribir

csv_test = ["Jonathan", "Vázquez", 34, ["Python", "C", "C++"], "www.//moure.dev"]
csv_test2 = ["Axel", "Montoya", 25, "COBOL", "www.//axl2858.com"]

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languages", "website"])
csv_writer.writerow(csv_test)
csv_writer.writerow(csv_test2)
csv_file.seek(0)

for line in csv_file.readlines():
    print(line)

csv_file.close()
# *.xlsx files
#import xlrd # Se debe de instalar el modulo

# *.xml files
import xml