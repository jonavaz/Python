### Lambdas ###

sum_two_value = lambda first_value, second_value: first_value + second_value
print(sum_two_value(2, 4))

multiply_value = lambda first_value, second_value: first_value * second_value - 3
print(multiply_value(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(3)(2, 4))

def sum_values_and_lambda(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_values_and_lambda(3)(2, 4))


my_lambda = lambda first_value, second_value: sum_values_and_lambda(3)(first_value, second_value)

print(my_lambda(2, 4))