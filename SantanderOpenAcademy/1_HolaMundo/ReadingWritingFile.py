# -----------------------------------------------------------------------------------------------------------
# Escribir archivo
file = open("data.txt", "w")
file.write("Hello, world!")
file.close()

# -----------------------------------------------------------------------------------------------------------
# Leer 1 archivo
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# -----------------------------------------------------------------------------------------------------------
# Leer 2 archivo
with open("data.txt", "r") as file:
    content = file.read()
    print(content)