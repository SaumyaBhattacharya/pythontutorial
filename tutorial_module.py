# Modules in Python

# Built-in modules in Python
import math
# from math import sqrt

print('Square root of 16: ', math.sqrt(16))
print('Value of pi: ', math.pi)
# print('Square root of 16: ', sqrt(16))




# User defined modules in python
import sample_module
# from sample_module import subtraction

print('Addition of two numbers using user defined module: ', sample_module.addition(4,2))
print('Addition of two numbers using user defined module: ', sample_module.subtraction(4,2))
# print('Addition of two numbers using user defined module: ', subtraction(4,2))




# aliasing in Modules - using 'as' keyword
import sample_module as module
from sample_module import addition as add

print('Addition of two numbers using user defined module: ', module.addition(10,2))
print('Addition of two numbers using user defined module: ', add(10,2))
