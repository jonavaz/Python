### File Handling ###

import os

# .txt file
#txt_file = open("./my_file.txt")
txt_file = open("Intermediate/my_file.txt", "w+") # Leer y escribir
txt_file.write("Mi nombre es Jonathan\nMi apellido es Vazquez\n34 años\nY mi lenguaje preferido es Python")
#txt_file.read()
print(txt_file.read())
print(txt_file.read(10))

print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readlines())

# Iterar por todas las líneas del archivo
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta C")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/my_file.txt")