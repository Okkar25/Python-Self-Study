# Python Modules

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# * Use a Module
# Now we can use the module we just created, by using the import statement
# * When using a function from a module, use the syntax: module_name.function_name

import my_modules

# my_modules.full_name("Okkar", "Aung")

location = my_modules.person1["country"]
# print(location)


# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# * Re-naming a Module
# * You can create an alias when you import a module, by using the "as" keyword:

import my_modules as mm

# info = f"{mm.person1["name"]} is {mm.person1["age"]} years old and he is {"single" if mm.person1["RS_status"] else "in a relationship"}"

# info = f"{mm.person1["name"]} is {mm.person1["RS_status"] and "single"}"

info = f"{mm.person1["name"]} is {mm.person1["age"]} {"years" if mm.person1["age"] > 1 else "year"} old."

# print(info)


# * Built-in Modules

# Import and use the platform module

import platform

sys = platform.system()
# print(sys)


# * Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function

import platform

func_in_platform = dir(platform)
# print(func_in_platform)


# * The dir() function can be used on all modules, also the ones you create yourself.

import my_modules as mx 
x = dir(mx)
# print(x)



# * Import From Module
# You can choose to import only parts from a module, by using the "from" keyword

# import my_modules
from my_modules import person1

my_country = person1["country"]
# print(my_country)

# print(my_modules.full_name("John", "Wick"))

from my_modules import two_sums as sums_of_two

# print(sums_of_two(10,5))

# * Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

