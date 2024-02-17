######## calling custom module math_operations

'''import math_operations

a = math_operations.add(15, 20)
b = math_operations.subtract(15, 20)
c = math_operations.multi(15, 20)
d = math_operations.divide(15, 20)

print("addition of a and b is ", a)
print("subtraction of a and b is ", b)
print("multiplication of a and b ", c)
print("division of a and b ", d)
'''

#### import all functions from a module

from math_operations import *

a = add(10,20)
b = subtract(10, 20)
c = multi(10, 20)
d = divide(10,20)
e = power(2, 4)

print("addtion of a and b is ", a)
print("subtraction of a and b is ", b)
print("multiplication of a and b is ", c)
print("division of a and b is ", d)
print("power of b of a is ", e)