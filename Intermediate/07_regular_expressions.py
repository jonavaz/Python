### Regular expressions ###

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(start)
print(end)
print(my_string[start:end])
#print(match.)

match = re.match("Esta no es la lección", my_other_string)
#if not(None == match): # Otra forma de comprobar que no es none
#if None is not match: # Otra forma de comprobar que no es none
if None != match:
    print(match)
    start, end = match.span()
    print(start)
    print(end)
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# Search
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)
#start, end = findall.span()

# Split
# Busca un patrón que nosotros le pasemos y retorna una lista separada por el patrón
split = re.split(":", my_string)
print(split)

# Sub

sub = re.sub("lección|Lección", "LECCIÓN", my_string, re.I)
print(sub)

sub = re.sub("[l|L]ección", "LECCIÓN", my_string, re.I)
print(sub)

sub = re.sub("Expresiones Regulares", "RegEx", my_string, re.I)
print(sub)

# Patterns
print("****** PATTERNS ******")

# La letra r al inicio indica que es una expresion regular
my_pattern = r"[lL]ección"
findall = re.findall(my_pattern, my_string)
print(findall)

my_pattern = r"[lL]ección|Expresiones"
findall = re.findall(my_pattern, my_string)
print(findall)

my_pattern = r"[a-z]"
findall = re.findall(my_pattern, my_string)
print(findall)

my_pattern = r"[0-9]"
search = re.search(my_pattern, my_string)
findall = re.findall(my_pattern, my_string)
print(findall)
print(search)

my_pattern = r"[\d]"
findall = re.findall(my_pattern, my_string)
print(findall)

my_pattern = r"[\D]"
findall = re.findall(my_pattern, my_string)
print(findall)

my_pattern = r"[l].*"
findall = re.findall(my_pattern, my_string)
print(findall)

# email validation regular expresion 
email = "jonavaz@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+[a-zA-Z]$"
match = re.match(pattern,email)
print(match)
search = re.search(pattern,email)
print(search)
findall = re.findall(pattern, email)
print(findall)

email = "jonavaz@gmail"
findall = re.findall(pattern, email)
print(findall)

email = "jonavaz@gmail."
findall = re.findall(pattern, email)
print(findall)

email = "jonavaz@gmail.9"
findall = re.findall(pattern, email)
print(findall)

email = "jonavazgmail."
findall = re.findall(pattern, email)
print(findall)

email = "jonavaz@gmail.com.mx"
findall = re.findall(pattern, email)
print(findall)