# indentation 

# num = 10
# if (num > 20):
#     print("number is greater than 20")
#     print("hello")
# else:
#     print("number is less than 20")
#     print("bye")


def calculate_total_sum(a,b):
    total_sum = a + b
    return total_sum

# result = calculate_total_sum(10,20)
# print(result)

# name = "Okkar Aung"
# name = 23

# data type
x = str(3)
y = int(4)
z = float(5)

# invalid
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# assign multiple values 
# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Peach"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "orange", "grape"]
# x,y,z = fruits

# print("x is " + x,"y is " + y, "z is " + z)
# print(f"x is {x}, y is {y}, z is {z}")

# x = 5
# y = "John"
# print(x + y) // error 
# print(x, y)


# global variable -------------------------------

# x = 10

def my_func():
    print(x)
# my_func()

def my_func1(): 
   global value
   value = 20
   
   global secret_value
   secret_value = 500
#    print(value)

# my_func1()

# print(secret_value)


global_value = 100

def global_func():
    global global_value  # overwrite global value 
    global_value = 900  # local variable 
    # print(global_value)

# global_func()

# print(global_value)

# list = (1,2,3,4,5)
# print(type(list))

# str = int("2")
# print(type(str))

# x = bytes(5)
# print(x)

# y = bytearray(5)
# print(y)

# z = memoryview(x)
# print(z)

# is_student = True

# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")
    
# friends = 9
# friends += 1

# friends = friends / 2
# friends = friends // 2

# friends /= 3

# remaining_friends = friends % 3

# print(remaining_friends)

my_age = str(23)
# print(my_age, type(my_age))

is_criminal = str(True) 
# print(is_criminal, type(is_criminal))

# fruit = int("banana") # invalid 
# print(fruit, type(fruit))

gpa = float(3.5)
# print(gpa)

# ------------------ input ----------------------

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# print(type(age))
# age += 1
# print(f"Hello {name}!")
# print(f"You are {age} years old.")



# ------------------ if --------------------



# age = int(input("Enter your age : "))
# has_ticket = True
# price = 10.00

# if age >= 65:
#     print("You are a senior citizen")
#     print(f"ticket price for a senior citizen is {price * 0.5}")
# elif age >= 20:
#     print("You are an adult")
#     print(f"ticket price for an adult is {price}")
# elif age > 10:
#     print("You are a teenager")
#     print(f"ticket price for an adult is {price * 0.75}")
# elif age == 0:
#     print("You are a new born")
# elif age < 0:
#     print("Please enter a valid age")
# elif age <= 10:
#     print("You are a child")
#     print(f"ticket price for an child is {price * 0.25}")


# if has_ticket:
#     print("You may enter, you have a ticket")
# else:
#     print("You cannot enter. Buy a ticket")




# --------------------------------------------------------------------------------------------------------------------




# balance = int(input("Enter your balance : "))

# if balance >= 500:
#     answer = input("Would you like to taste our Pizza ? Yes or No ? : ").strip().lower()
    
#     # print(answer, type(answer))
      
#     if answer == "yes":
#         balance -= 300
#         print("Enjoy the Pizza with large toppings.")
#         print(f"Your balance is : {balance}")
#     else:
#         # print ("Come back when you have money")
#         print(f"Your balance is : {balance}")
    
# elif balance >= 300:
    
#     answer = input("Would you like to taste our delicious snacks ? Yes or No ? : ").strip().lower()
    
#     if answer == "yes":
#         balance -= 200
#         print("Enjoy the snacks")
#         print(f"Your balance is : {balance}")
#     else:
#         print(f"Your balance is : {balance}")
        
# elif balance >= 200:
#     answer = input("Would you like our cold drinks ? Yes or No ? : ").strip().lower()
    
#     if answer == "yes":
#         balance -= 100
#         print("Enjoy the cold drinks")
#         print(f"Your balance is : {balance}")
#     else:
#         print(f"Your balance is : {balance}")
        
# else: 
#     print("Your are broke as f**k!")
    
    

    
# --------------------------------------------------------------------------------------------------------------------




# balance = int(input("Enter your balance: "))

# if balance >= 600:
#     answer = input("Would you like to taste our Pizza for $300? Yes or No? ").strip().lower()
    
#     if answer == "yes":
#         balance -= 300
#         print("Enjoy the Pizza with large toppings.")
#         print(f"Your balance is: {balance}")
        
#         # Check if balance is enough for snacks
#         if balance >= 400:
#             answer = input("Would you like to taste our delicious snacks for $200? Yes or No? ").strip().lower()
            
#             if answer == "yes":
#                 balance -= 200
#                 print("Enjoy the snacks.")
#                 print(f"Your balance is: {balance}")
                
#                 # Check if balance is enough for cold drinks
#                 if balance >= 200:
#                     answer = input("Would you like our cold drinks for $100? Yes or No? ").strip().lower()
                    
#                     if answer == "yes":
#                         balance -= 100
#                         print("Enjoy the cold drinks.")
#                         print(f"Your balance is: {balance}")
#                     else:
#                         print(f"Your balance is: {balance}")
#                 else:
#                     print(f"Your balance is: {balance}")
#             else:
#                 print(f"Your balance is: {balance}")
#         else:
#             print(f"Your balance is: {balance}")
#     else:
#             print(f"Your balance is: {balance}")
    
# elif balance >= 400:
#     answer = input("Would you like to taste our delicious snacks for $200? Yes or No? ").strip().lower()
    
#     if answer == "yes":
#         balance -= 200
#         print("Enjoy the snacks.")
#         print(f"Your balance is: {balance}")
        
#         # Check if balance is enough for cold drinks
#         if balance >= 200:
#             answer = input("Would you like our cold drinks for $100? Yes or No? ").strip().lower()
            
#             if answer == "yes":
#                 balance -= 100
#                 print("Enjoy the cold drinks.")
#                 print(f"Your balance is: {balance}")
#             else:
#                 print(f"Your balance is: {balance}")
#         else:
#             print(f"Your balance is: {balance}")
#     else:
#         print(f"Your balance is: {balance}")

# elif balance >= 200:
#     answer = input("Would you like our cold drinks for $100? Yes or No? ").strip().lower()
    
#     if answer == "yes":
#         balance -= 100
#         print("Enjoy the cold drinks.")
#         print(f"Your balance is: {balance}")
#     else:
#         print(f"Your balance is: {balance}")
        
# else:
#     print("You are so poor TwT!")


  
# --------------------------------------------------------------------------------------------------------------------



# casting

# x = list(("apple", "banana", "cherry"))

# print(x)
# print(type(x)) 

# y = dict(name="Okkar", age=23)
# print(y)

# z = set(("apple", "banana", "cherry"))
# print(z, type(z))

# u = frozenset(("apple", "banana", "cherry"))
# print(u, type(u))

# b = bool(-1)
# print(b, type(b))


# complex => a + bj

# complex_num = 7 + 3j
# print(complex_num.real, complex_num.imag) 



#-------------------------------------------------------------------------



import random # built-in modules

rand_num = random.randrange(1,10)

# print(rand_num)


frozen_list = frozenset([1,2,3,4,5])
# print(frozen_list, type(frozen_list))

frozen_tuple = frozenset((1,2,3,4,5))
# print(frozen_tuple, type(frozen_tuple))

frozen_set = frozenset({1,2,3,4,5})
# print(frozen_set, type(frozen_set))



#--------------------------------------------------------------------------------------



# ***** shorthand property *****

a = 20
b = 30

# if a > b: print("a is greater than b")
# print("a is greater than b") if a > b else print("a is less than b")
# print("A is greater") if a > b else print("a = b") if a == b else print("B is greater")
# if not a > b: print("hello") 
# if a > b: pass# shorthand property 


# logical operators ( or / and / not ) 

# temp = int(input("Enter today temperature : "))
# is_raining = input("Will it rain today? Yes or No ? : ").strip().lower()

# if is_raining == "yes":
#     is_raining = True
# else:
#     is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is postponed")
# else: 
#     print("The outdoor event will continue")


#=================================================================================


# temp = int(input("Enter today temperature : "))
# is_sunny = input("Will it be sunny today? Yes or No ? : ").strip().lower()

# if is_sunny == "yes":
#     is_sunny = True
# else:
#     is_sunny = False

# if temp >= 35 and is_sunny:
#     print("The weather is hot outside 🥵")
#     print("It is sunny 🌞")
    
# elif temp >= 28 and is_sunny:
#     print("The weather is warm outside 😎")
#     print("The weather is dull ⛅")
    
# # elif temp < 28 and temp > 0 and is_sunny:
# elif 28 > temp > 0 and is_sunny:
#     print("The weather is good outside 🌞")

# elif temp <= 0 and is_sunny:
#     print("The weather is cold outside 🥶")
#     print("It is snowing ❄️")
    
# else: 
#     print("It is not sunny today. 🌆")


#=================================================================================
    
    
    
# temp = 15
# is_sunny = False


# if temp >= 35 and is_sunny:
#     print("The weather is hot outside 🥵")
#     print("It is sunny ☀️")
    
# elif temp >= 28 and is_sunny:
#     print("The weather is warm outside 😎")
#     print("It is sunny ☀️")
    
# # elif temp < 28 and temp > 0 and is_sunny:
# elif 28 > temp > 0 and is_sunny:
#     print("The weather is good outside 🌞")
    
# elif temp <= 0 and is_sunny:
#     print("The weather is cold outside 🥶")
#     print("It is a bit sunny ⛅")
    
    
    
    
# elif temp >= 35 and not is_sunny:
#     print("The weather is hot outside 🥵")
#     print("It is Cloudy ⛅")
    
# elif temp >= 28 and not is_sunny:
#     print("The weather is warm outside 😎")
#     print("The weather is dull ☁️")
    
# # elif temp < 28 and temp > 0 and is_sunny:
# elif 28 > temp > 0 and not is_sunny:
#     print("The weather is cool outside 😷")
#     print("It is raining lightly 🌦️")
    
# elif temp <= 0 and not is_sunny:
#     print("The weather is cold outside 🥶")
#     print("There is no sunlight 🌨️")



# emoji 
# window => window + .
# mac    => ctrl + cmd + space



# --------------------------------------------------------------------------------------------------------



# ****** string methods *********


name = "Saw Yadana"
# print(name[0])

# for x in name:
#     print(x)
    
# print(len(name))

is_exist = "s" in name.lower()
# print(name.lower())

exist_value = "N"

# if exist_value in name.upper():
#     print("The value exists.")
# else:
#     print("Such value does not exist.")


txt = "The happy fox jumps into the water"
exist_value1 = "wolf"

# if exist_value1 not in txt:
#     print("true")
# else: 
#     print("false")

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#    print("No, 'expensive' is NOT present.") 


# string methods 
# slice

str = "Hello World"
sliced_value = str[2:7] # slice
# print(sliced_value)

slice_from_start = str[:7]
# print(slice_from_start)


sliced_to_end = str[8:]
# print(sliced_to_end)

sliced_negative = str[-8:-3]
# print(sliced_negative)

# modify
# .upper()
# .lower()
# .strip()
# .capitalize()
# .replace()
# .split()
# .join()

# .count()
# .find()
# .index()
# .isdigit()
# .isnumeric()
# .islower()
# .isupper()
# .swapcase()
# .zfill()


# https://www.geeksforgeeks.org/python-string-methods/

# https://www.w3schools.com/python/python_ref_string.asp



a = " I am Python user "
b = "I am Python user"
# print(a.strip())
# print(a.strip() == b)

x = a.replace("Python","JavaScript")

text = "My major is, computer science"
result = text.split(" ")
result = text.split(",")
# print(result)

# concatenation

value1 = "Py"
value2 = "thon"
value3 = value1 + " " + value2
# print(value3)

# format string / f-string / string literal 

# placeholder {:} modifier: .f .2f .3f 

price = float(100)
# print(f"My laptop costs ${price:.5f}")

# print(f"Sum of Two numbers is {20 + 40}")


# escape characters \


lyrics = "My favorite song is \"Ghost\" by Justin Bieber."
# print(lyrics)

# \n  -  new line 
# \\  -  backslash 
# \r  -  Carriage return
# \t  -  tab 
# \b  -  backspace 


txt = "Hello\rWorld!" # output hello => after that cursor moves back to hello => then print world 

txt = "Hello\tWorld!" # tab

txt = "Hello \bWorld!" # tab
# print(txt) 


# list = ["apple","orange","grape"]
# print("/".join(list))



# ----------------------------------------------------------------------------------------------------------------------------




# ****** while loop *********

# age = 0
# while age < 10: 
#     age += 1
#     print(age)
# print("final age", age)




# break / continue

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     i += 1
#     continue
#   i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         # break
#         continue
#         # pass
#     print(i)  
# print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
  
  
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# print("i is no longer less than 6")






# name = input("Enter your name : ")

# while name == "":
#      name = input("Enter your name : ")
     
# age = int(input("Enter your age : "))
     
# while age < 0 or age == "":
#      print("Age cannot be less than zero")
#      age = int(input("Enter your age : "))
     
# print(f"Hello {name}")
# print(f"You are {age} years old")


# def sum_of_natural_num(n):
#     num_sum = sum(range(1, n+1))
#     print(num_sum)

# sum_of_natural_num(10)


# ------------------------------------------------------------------------------------------------------------------------------------

# 1. Print Numbers from 1 to 10


# def print_num(start, end):

#     while start <= end:
#         print(start)
#         start += 1

# print_num(3,7)

# ===================================================


# 2 Write a Python program to find the sum of natural numbers up to a given number n.

# def sum_of_natural_num(start, n):
#     sum = 0
    
#     while start <= n:
#         sum += start 
#         start += 1
        
#     print(sum)

# sum_of_natural_num(4,7)

# new method 
# 3 4 5 6 7
# x = sum(range(3,7)) 
# print(x)


# ============================================

# 3. Guess the Number Game
# Problem: Write a Python program where the computer randomly selects a number between 1 and 100, and the user has to guess the number. The program should continue to prompt the user until they guess the correct number.


# import random
# number_to_guess = random.randint(1, 100)
# guess = None
# while guess != number_to_guess:
#     guess = int(input("Guess the number between 1 and 100: "))
#     if guess < number_to_guess:
#         print("Too low! Try again.")
#     elif guess > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You've guessed the correct number.")


# import random

# num_to_guess = random.randint(1,30)
# guess = None
# total_attempt = 0

# while guess != num_to_guess:
#     print(num_to_guess)
#     guess = int(input("Enter your guess number : "))
#     total_attempt += 1
    
#     if guess - num_to_guess >= 10:                                          #  17    5
#         print("Too high! Try to guess lower.") 
#     elif guess - num_to_guess >= 5:
#         print("Still high! Try to guess a bit lower.")
#     elif guess > num_to_guess:
#         print("You are close! Try a bit lower than that.")
        
#     elif num_to_guess - guess >= 10:                                        #  16    17
#         print("Too low! Try to guess higher.") 
#     elif num_to_guess - guess >= 5:
#         print("Still low! Try to guess a bit higher.")
#     elif guess < num_to_guess:
#         print("You are close! Try a bit higher than that.")
        
#     else: 
#         print("Congratulations! You have guessed the correct number.")

# print(f"Your total attempt is {total_attempt} {"time" if total_attempt == 1 else "times"}")      


# ============================================  


# 4. Factorial of a Number
# Problem: Write a Python program to calculate the factorial of a given number using a while loop.


# 5. Reverse a Number
# Problem: Write a Python program to reverse a given number using a while loop.

# 432856
# def reverse_number(num):
#     reverse = 0
    
#     while num > 0:
#        digit = num % 10
#        reverse = reverse * 10 + digit
#        num //= 10

#     print(f"Reversed number is: {reverse}")
    
# reverse_number(423765 )



# -------------------------------------------------------------------------------------------------------------------------------




# ************ for loop **************

# range() defaults to 0 as starting value
 

# for i in range(1,6, 2):
#     print(i)


# import time
# for i in range(10,0,-1):
#     time.sleep(1)
#     print(i)
# print("countdown completes")


# job = "Software Developer"
# for char in job:
#     print(char, end="-")


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     # break
#     continue
#   print(x)


# for i in range(6):
#     if i == 3: break 
#     print(i)
# else:
#     print("Finish!")


# ****** nested loop ********


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)


list1 = [23,5,6,34,678]
list2 = [21,51,6,678, 32]

# duplicate_num = 0

# for x in list1:
#     for y in list2:
#         if x == y:
#             duplicate_num += 1

# print(f"there are {duplicate_num} duplicate numbers in the lists.")



# set_1 = set(list1)
# set_2 = set(list2)

# duplicate_sets = set_1 & set_2
# duplicate_lists = list(duplicate_sets)

# # print(len(duplicate_lists), duplicate_lists)

# print(f"there are {len(duplicate_lists)} duplicate numbers in the lists.")



# for x in [0, 1, 2]:
#   pass



# ***** Problems ******


# 2: Sum of All Numbers in a List
# Problem: Given a list of numbers, write a for-loop to calculate the sum of all the numbers in the list.


# numbers = [1, 2, 3, 4, 5]
# total_sum = 0

# for num in numbers:
#     total_sum += num

# print("Sum of all numbers:", total_sum)



# ===========================================================================



# Problem 3: Factorial of a Number
# Problem: Write a for-loop to calculate the factorial of a given number.


# n = 5
# factorial = 1

# for i in range(1, n+1):
#     factorial *= i

# print("Factorial of", n, "is", factorial)



# ===========================================================================



# Problem 4: Print the Multiplication Table
# Problem: Write a for-loop that prints the multiplication table of a given number.



# n = 9

# for i in range(1,n+1):
#     print(f"{n} X {i} = {n * i}")



# ===========================================================================



# Problem 5: Find the Largest Number in a List
# Problem: Given a list of numbers, write a for-loop to find the largest number.



numbers = [10, 24, 45, 13, 99, 2, 38]

# largest_num = 0

# for i in range(len(numbers)):
#     if numbers[i] > largest_num:
#         largest_num = numbers[i]


# for i in numbers:
#     if i > largest_num:
#         largest_num = i
    

# print(f"Largest number is {largest_num}")



# ===========================================================================



# Problem 6: Count Vowels in a String
# Problem: Write a for-loop that counts the number of vowels in a given string.



text = "The foolish fox tried to catch the moon in the water reflection"
# vowels = "aeiou"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1
        
# print(f"Number of vowels in the text is {count}")



# ===========================================================================



#Problem 7: Reverse a List
# Problem: Write a for-loop to reverse a given list.



# my_list = [1, 2, 3, 4, 5]
# reversed_list = []

# for i in range(len(my_list) - 1, -1, -1):
#     reversed_list.append(my_list[i])
    
# print(f"Reversed List : {reversed_list}")



# ===========================================================================



# Problem 8: Count the Frequency of Elements in a List
# Problem: Write a for-loop to count the frequency of each element in a list.



# numbers = [1, 23, 5, 78, 23, 5, 34, 90, 5, 15, 34, 78, 34, 100, 34, 90 ]
# frequency = {}

# for i in numbers:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
        
# print(f"Frequency of elements : {frequency}")


# new = {
#     1 : 1,
#     23: 1,
#     5: 1,
#     78: 1
# }

# if 23 in new:
#     print("True")
    
# old = {}
# old["my_name"] = "Okkar"
# old[1] = 23
# old["23"] = 80

# print(old)



# ===========================================================================



# Problem 10: Print a Pyramid Pattern
# Problem: Write a for-loop to print a pyramid pattern of stars.

# n = 5

# for i in range(1,(n + 1)):
#     print( " " * (n - i) + "*" * (i * 2 - 1))
    
# for diamond
# for i in range((n-1), 0, -1):
#     print(" " * (n - i) + "*" * (i * 2 - 1))



# * docstring

def add(a, b):
    """
    This function takes two numbers as inputs and returns their sum.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

# Access the docstring
# print(add.__doc__)