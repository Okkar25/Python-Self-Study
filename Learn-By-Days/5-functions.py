# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("Hello from a function")
  
# use the function name followed by parenthesis
# my_function()

# * Arguments

def greeting(first_name, last_name):
  print(f"Welcome {first_name} {last_name}!")

# greeting("Okkar","Aung")
# greeting("Saw","Yadana")

# Arguments are often shortened to args in Python documentation

# Parameters or Arguments?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# * By default, a function must be called with the correct number of arguments

# greeting("Okkar")

# * Asterisk
# fruits = ["apple","orange","grape","peach"] 
# [a,*b,c] = fruits

# print(a,b,c)

# ***** Arbitrary Arguments, *args
# function will receive a tuple of arguments, and can access the items accordingly
# Arbitrary Arguments are often shortened to *args in Python documentations

def my_kids(*kid):
    print(f"My youngest kid is", kid[1] )

# my_kids("John","Billy","Claire")


# * Keyword Arguments
#  order changes 
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# def my_children(child1, child2, child3):
#     print(f"My youngest child is", child3)

# my_children( child3="Claire",child2="John", child1="Billy")


# *** Arbitrary Keyword Arguments, **kwargs

def my_children(**child):
    # print(f"My youngest child is", child)
    print(f"My youngest child is", child["child1"])

# my_children( child3="Claire",child2="John", child1="Billy")


# * Default Parameter Value

def my_country(country = "Myanmar"):
    print(f"I live in", country)
    
# my_country("United States")


# * Passing a List as an Argument

def func_food(food):
    for x in food:
        print(x)

fruits = ["apple","orange","peach"]

# func_food(fruits)


# * Return Values

def my_function(x):
  return 5 * x

# print(my_function(10))

# * Pass

# def my_function(x):
#   pass


# ----------------------------------------------------------------------------------------------------


# position-only arguments => 3 , "name"
# keyword-only arguments => x=3, y=20, z="hello"


# * Positional-Only Arguments
# doesn't allow keyword arguments 
# a function can have ONLY positional arguments, or ONLY keyword arguments
# To specify that a function can have only positional arguments, add , / after the arguments

def my_function(x, /):
  print(x)

# my_function(3)
# my_function(x=3)



# * Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x, y):
  print(x + y)

# my_function(3)
# my_function(3,3)
# my_function(x=3)
# my_function(y=10,x=3)

# * Combine Positional-Only and Keyword-Only

def combine_func(a, b, /, *, c , d):
    print(a + b + c + d)

# combine_func(6, d=7,c=8, 5)
# combine_func(10,5, d=7,c=8)

# def combine_func(*, c , d, a, b, /): # error 
#     print(a + b + c + d)

def order_pizza(size, *toppings, **details):
    print(f"I want a {size}-sized pizza with the following toppings : ")
    for top in toppings:
        print(f"- {top}")
    
    print("\nDetails of the order : ")
    for k,v in details.items():
        print(f"- {k} : {v}")

# order_pizza("large", "cheese", "pepperoni", "sausage", delivery=True, tip=5)


# ----------------------------------------------------------------------------------------------------


# * Recursion 

# function calls itself.
# developer should be very careful with recursion as it can never terminates, or uses excess amounts of memory or processor power.


def recursion_func(k):
    if (k > 0):
        result = k + recursion_func(k - 1)
        print(result)
    else:
        result = 0
    return result

# print("Start here")
# recursion_func(5)



# ===============================================================================================




# 1. Factorial of a Number
# Problem:
# Write a recursive function to find the factorial of a given number.

# Solution:

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Output: 120
# Explanation:
# factorial(5) calls factorial(4), which calls factorial(3), and so on, until it reaches factorial(0) (the base case).
# Each call multiplies the result of the next call, and the product is returned.



# -----------------------------------------------------------------------------------------------



# 2. Fibonacci Sequence
# Problem:
# Write a recursive function to calculate the nth Fibonacci number. The Fibonacci sequence is defined as:

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
# Solution:

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Example usage
# print(fibonacci(6))  # Output: 8
# Explanation:
# The recursive function calls itself twice: once for n-1 and once for n-2, until it reaches the base cases (n = 0 or n = 1).
# fibonacci(6) computes the sum of fibonacci(5) and fibonacci(4) recursively.



# -----------------------------------------------------------------------------------------------



# 3. Sum of Digits
# Problem:
# Write a recursive function that takes a positive integer and returns the sum of its digits.

# Solution:

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_of_digits(n // 10)

# # Example usage
# print(sum_of_digits(1234))  # Output: 10
# Explanation:
# Each recursive call extracts the last digit (n % 10) and adds it to the result of the next call, which processes the remaining digits (n // 10).




# -----------------------------------------------------------------------------------------------




# 4. Power of a Number
# Problem:
# Write a recursive function to calculate x raised to the power of n.

# Solution:

# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n - 1)

# # Example usage
# print(power(2, 3))  # Output: 8
# Explanation:
# The base case is when n equals 0, returning 1 (since any number raised to the power of 0 is 1).
# The function multiplies x by power(x, n - 1) recursively.



# ---------------------------------------------------------------------------------------------------



# 5. Reverse a String
# Problem:
# Write a recursive function to reverse a string.

# Solution:

# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     else:
#         return s[-1] + reverse_string(s[:-1])

# # Example usage
# print(reverse_string("hello"))  # Output: "olleh"
# Explanation:
# The function recursively takes the last character of the string and appends it to the result of reversing the rest of the string.



# ---------------------------------------------------------------------------------------------------



# 6. Check if a String is a Palindrome
# Problem:
# Write a recursive function to check if a string is a palindrome.

# Solution:

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] == s[-1]:
#         return is_palindrome(s[1:-1])
#     else:
#         return False

# # Example usage
# print(is_palindrome("racecar"))  # Output: True
# Explanation:
# The function checks if the first and last characters of the string are equal. If they are, it continues checking the inner substring, recursively.
# The base case is when the length of the string is 0 or 1, in which case it is a palindrome.



# ---------------------------------------------------------------------------------------------------



# 7. Sum of an Array
# Problem:
# Write a recursive function to find the sum of all elements in an array.

# Solution:

# def sum_of_array(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sum_of_array(arr[1:])

# # Example usage
# print(sum_of_array([1, 2, 3, 4, 5]))  # Output: 15
# Explanation:
# The function takes the first element (arr[0]) and adds it to the result of the recursive call on the rest of the array (arr[1:]).
# The base case is when the array is empty, returning 0.



# ---------------------------------------------------------------------------------------------------



# 8. Find Maximum in a List
# Problem:
# Write a recursive function to find the maximum element in a list.

# Solution:

# def find_max(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         max_of_rest = find_max(arr[1:])
#         return max(arr[0], max_of_rest)

# # Example usage
# print(find_max([1, 5, 3, 9, 2]))  # Output: 9
# Explanation:
# The base case is when the list has one element, returning that element.
# The function compares the first element (arr[0]) with the maximum of the rest of the list, found recursively.



# ---------------------------------------------------------------------------------------------------



# 9. Count Occurrences of a Number in a List
# Problem:
# Write a recursive function to count the number of occurrences of a number in a list.

# Solution:

# def count_occurrences(arr, target):
#     if len(arr) == 0:
#         return 0
#     else:
#         return (1 if arr[0] == target else 0) + count_occurrences(arr[1:], target)

# # Example usage
# print(count_occurrences([1, 2, 3, 2, 2, 4], 2))  # Output: 3
# Explanation:
# The function checks if the first element equals the target. If so, it adds 1 to the count from the recursive call on the rest of the list.
# These problems cover different use cases for recursion and help in understanding how recursive functions break down problems into smaller sub-problems.
