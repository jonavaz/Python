### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5
"""
def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)
"""
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###
# Los closures retornan una funcion

def sum_ten(original_vale):
    def add(value):
        return value + 10 + original_vale
    return add

### sum_ten retorna la función add
add_closure = sum_ten(1)    
print(add_closure(5))

# Es como una ejecucion de una lambda, en donde el primer parametro es para sum_ten y el segundo
# es el parametro de la función dentro de sum_ten
sum_ten(5)(1)

# Mi ejercicio de closures
SUMAR = 1
RESTAR = 2
MULTIPLICAR = 3
DIVIDIR = 4

def math_operations(operator):
    if SUMAR == operator:
        def sumNumbers(first_value, second_value):
            return first_value + second_value
        return sumNumbers
    elif RESTAR == operator:
        def resNumbers(first_value, second_value):
            return first_value - second_value
        return resNumbers
    elif MULTIPLICAR == operator:
        def multNumbers(first_value, second_value):
            return first_value * second_value
        return multNumbers
    else:
        def divNumbers(first_value, second_value):
            return first_value / second_value
        return divNumbers

def f_(operator):
    # Si solo se mandar llamar math_operations(operator) sin return antes, 
    # La función f_ retorna un error de que la función no es llamable
    return math_operations(operator)

"""    
print(math_operations(SUMAR)(2,2))
print(math_operations(RESTAR)(2,2))
print(math_operations(MULTIPLICAR)(2,2))
print(math_operations(DIVIDIR)(2,2))
"""    

print(f_(SUMAR)(2,2))
print(f_(RESTAR)(2,2))
print(f_(MULTIPLICAR)(2,2))
print(f_(DIVIDIR)(2,2))
