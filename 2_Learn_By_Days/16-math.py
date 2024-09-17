# Python Math

# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Built-in Math Functions

# * The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(23, 56, 12, 78)
y = max(23, 56, 12, 78)
# print(f"max is {y} and min is {x}")


# * The abs() function returns the absolute (positive) value of the specified number:
z = abs(-7.25)
# print(z)


# * The pow(x, y) function returns the value of x to the power of y (xy).
p = pow(2,3)
p = 2 ** 3
p = 2 * 2 * 2
# print(p)


# * The Math Module

# Python has also a built-in module called math, which extends the list of mathematical functions.
# When you have imported the math module, you can start using methods and constants of the module.

import math as mt

x = mt.sqrt(64)
# print(x)
# print(f"{x:.0f}")

import math

larger_val = math.ceil(1.01)
smaller_val = math.floor(1.25)
# print(larger_val, smaller_val)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:


# The math.pi constant, returns the value of PI (3.14...):

import math 

pi = math.pi
# print(pi, f"{pi:.3f}")



