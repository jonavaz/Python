### Module ###

import my_module

my_module.sumValue(5,3,1)
my_module.printValue("Hola Python!")

from my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola Python!")

import math
print(math.pi)
print(math.pow(2,8))

from math import pi

print(pi)

from math import pi as PI_VALUE

print(PI_VALUE)