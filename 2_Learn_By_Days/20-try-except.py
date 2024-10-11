# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:


# x = 10
# try: 
#     print(x)
# except:
#     print("Error occurs")

# print(x) # error 


# * Many Exceptions

# try:
#     print(x)
# except NameError:
#     print("Variable cannot be found")
# except:
#     print("Something else went wrong")


# * Else

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# * Finally

# The finally block, if specified, will be executed regardless if the try block raises an error or not.


# try:
# #   print(x)
#   print("x")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# finally:
#   print("The 'try except' is finished")



# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  


# * Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

x = -1

# if x < 0:
#     raise Exception("Error occurs")


# * You can define what kind of error to raise, and the text to print to the user.

x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")


# -----------------------------------------------------------------------------------------------


# Types of Errors 


# 1. TypeError
# Trying to add a string to an integer
# x = "hello" + 5  # TypeError: can only concatenate str (not "int") to str
# print(x)


# 2. NameError
# print(my_var)  # NameError: name 'my_var' is not defined


# 3. ValueError
x = int("100")
x = int("abc")
# print(x)


# 4. IndexError
lst = [1, 2, 3]
print(lst[5])  # IndexError: list index out of range


# 5. KeyError
my_dict = {"a": 1, "b": 2}
# print(my_dict["c"])  # KeyError: 'c'


# 6. AttributeError
x = 10
x.append(5)  # AttributeError: 'int' object has no attribute 'append'


# 7. ZeroDivisionError
print(10 / 0)  # ZeroDivisionError: division by zero


# 8. FileNotFoundError
open('non_existent_file.txt')  # FileNotFoundError: [Errno 2] No such file or directory


# 9. ImportError
# import non_existent_module  # ImportError: No module named 'non_existent_module'


# 10. IndentationError
# def my_func():
# print("hello")  # IndentationError: expected an indented block


# 11. SyntaxError
# if True # SyntaxError: invalid syntax (missing colon)


# 12. RuntimeError
# raise RuntimeError("Something went wrong")  # RuntimeError: Something went wrong


# 13. MemoryError
# Occurs when an operation runs out of memory. This is rare but can happen in memory-intensive applications.


# 14. OverflowError
# Raised when the result of an arithmetic operation is too large to be expressed within the allowed range.
import math
print(math.exp(1000)) # e^1000  # OverflowError: math range error


# 15. StopIteration
# Occurs when the next() function reaches the end of an iterator, such as a for-loop, and no more elements are available.

# 16. FileExistsError
# x mode 

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")



# * https://www.w3schools.com/python/python_ref_exceptions.asp



# try:
#     print(x)
# except Exception as e:
#     print(f"Error occurs : {type(e).__name__}")

# try:
#     # x = 10
#     print(x)
# except NameError:
#     print("This is a Name Error.")
# except IndentationError:
#     print("This is a Indentation Error.")

# try:
#     # x = -10
#     # print(x / 0)
#     # print(x)

#     # if x < 0:
#     #     raise ValueError("Value cannot be negative.")
#     x = 10

#     if type(x) is not str:
#         raise TypeError("Only str value allowed")

# except ValueError as v:
#     print("Error :", v)

# except NameError as e:
#     print("Something wrong with name not existing")

# except ZeroDivisionError as z:
#     print("Cannot be divided by zero")

# except Exception as error:
#     print(error)

# else:
#     print("There is no error.")

# finally:
#     print("Completed")


# * custom exception

class JustNotCoolError(Exception):
    pass


try:
    # raise Exception("I'm a custom exception.")
    raise JustNotCoolError("This isn't just cool, mann.")
    

except ValueError as v:
    print("Error :", v)

except NameError as e:
    print("Something wrong with name not existing")

except ZeroDivisionError as z:
    print("Cannot be divided by zero")

except Exception as error:
    print(error)

else:
    print("There is no error.")

finally:
    print("Completed")
