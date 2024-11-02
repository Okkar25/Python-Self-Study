# sets

x = 10

# print(vars())

vars()["y"] = 100

# print(vars())

# y is not defined yet
# print(y * 2)


# LEGB

#  1. Local function: x
#  2. Enclosing function: (don't worry about this for now)
#  3. Global/Module: y
#  4. Builtins:  print, abs

x = 2
y = 3


def f():
    # global x
    x = 99
    print(x, y)
    print(vars())


# f()

# print(abs(-100))

abs(-5)


def g(x):
    return 0


abs = g
# print(abs(-5))


# print(vars())

# print(abs(-23))

vars().pop("abs")

# print(vars())

# print(abs(-23))


# * import

import math
from math import pi
from math import *

# print(math.pi)
# print(pi)


# * 3 types of functions/methods

# functions are not associated with a specific type: abs, max, len - do not have calling objects

# methods are functions defined inside a class : list.append, str.upper


# 1. function/methods that modifies/sets something

# list.append, list.sort
# print

# 2. function/method that returns/gets something

# abs, max, len
# str.upper
# sorted

# 3. function methods that modifies/sets and returns/gets:

# list.pop
# input
# .upper()

# print(input("Enter something: "))

# ans = input("Enter something: ")
# print(ans)

s = "apple"
b = "banana"

# print(s.upper())

x = b.upper()
# print(x)


# * Point class

# Object oriented (OO) programming

#  A class is a description/pattern for creating objects.  Each object possesses:
# data/attributes - the underlying data representing the object
# methods - code that is used to access/manipulate the attributes

# Object: An instance of a class. For example, my_car is an object (instance) of the Car class.
# Attributes of an object: You access an object’s attributes using dot notation, e.g., my_car.color.
# Methods of an object: You invoke methods using dot notation, e.g., my_car.start().


class Car:
    # The __init__ method initializes the attributes when an object is created
    def __init__(self, make, model, year, color):
        self.make = make  # Attribute for the car's make
        self.model = model  # Attribute for the car's model
        self.year = year  # Attribute for the car's year
        self.color = color  # Attribute for the car's color

    # Method to start the car
    def start(self):
        print(f"{self.color} {self.make} {self.model} is starting...")

    # Method to stop the car
    def stop(self):
        print(f"{self.color} {self.make} {self.model} is stopping...")


# Creating an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2020, "Red")

# Accessing the object's attributes
# print(my_car.make)   # Output: Toyota
# print(my_car.year)   # Output: 2020

# Calling methods on the object
# my_car.start()       # Output: Red Toyota Corolla is starting...
# my_car.stop()        # Output: Red Toyota Corolla is stopping...


# v1 - all methods are explicit
# v2 - adds magic/dunder methods that are called automatically


# Point Class - Version 1 (Explicit Methods)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Method to move the point to a new location
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # Method to return the coordinates as a string
    def display(self):
        return f"Point({self.x}, {self.y})"

    # Method to add two points explicitly
    def add(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)


# Example usage (v1):
p1 = Point(2, 3)
p2 = Point(4, 5)

# Moving p1 to a new location
p1.move(10, 15)

# Display points explicitly
# print(p1.display())  # Output: Point(10, 15)
# print(p2.display())  # Output: Point(4, 5)

# Adding points explicitly
# p3 = p1.add(p2)
# print(p3.display())  # Output: Point(14, 20)


# --------------------------------------------------------------------------------------------------------------------


# Point Class - Version 2 (With Magic Methods)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Automatically called when printing the object or using repr()
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Automatically called when adding two Point objects using the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Automatically called when using str() or printing the object
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Optional: You can add more dunder methods for subtraction, equality, etc.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


# Example usage (v2):
p1 = Point(2, 3)
p2 = Point(4, 5)

# Automatically uses __repr__() when printing the object
# print(p1)  # Output: (2, 3)
# print(p2)  # Output: (4, 5)

# Adding two points using the + operator (calls __add__())
p3 = p1 + p2
# print(p3)  # Output: (6, 8)

# Checking equality (calls __eq__())
p4 = Point(2, 3)
# print(p1 == p4)  # Output: True (because they have the same coordinates)

p4 = p2 - p1
# print(p4)


# * sleight of hand

# bound method call - object to the left
# lst.append(5) - the call is bound to the object
# unbound method call - class /type to the left
# list.append(lst,5) - the class list is to the left, the objects is passed as an argument


# 1.  Bound Method


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


# Create an instance of Point
p1 = Point(2, 3)

# Call the move method on the instance (Bound method)
p1.move(5, 6)  # This is a bound method call
# print(p1.x, p1.y)  # Output: 5 6


# 2. Unbound Method


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


# Unbound method - accessed directly from the class
p1 = Point(2, 3)
Point.move(
    p1, 10, 12
)  # Calling move as an unbound method, passing the instance explicitly

# print(p1.x, p1.y)  # Output: 10 12


# obj.method( arg1, arg2, ...)           # bound
# MyClass.method( obj, arg1, arg2, ...)  # unbound


num_lst = [1, 2, 3, 4, 5]
num_lst.append(10)

list.append(num_lst, 100)

# print(num_lst)

s = "hello"
# print(s.upper())

# print(str.upper(s))

#  >>> p = Point() # constructor
#  >>> p.setx( 4 )
#  >>> p.sety( 7.1 )
#  >>> p.get()
#  (4, 7.1)
#  >>> p.move(1,1) # relative move
#  >>> p.get()
#  (5, 8.1)


# Function-based approach

# Initial balance
balance = 0


def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: ${amount}")


def get_balance():
    return f"Current balance: ${balance}"


# Usage
# deposit(100)
# print(get_balance())


# OOP approach


class Account:
    def __init__(self):
        self.balance = 0  # Initial balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def get_balance(self):
        return f"Current balance: ${self.balance}"


# Usage
account = Account()
# account.deposit(100)
# print(account.get_balance())


# ----------------------------------------------------------------------------------------


# * Point - version 1


class Point:
    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get_coord(self):
        return (self.x, self.y)
        # if hasattr(self, "x") and hasattr(self, "y"):
        #     return (self.x, self.y)
        # else:
        #     return "One or Both of the coordinates are missing"

    def move(self, deltax, deltay):
        self.x = self.x + deltax
        self.y = self.y + deltay
        # self.x += deltax
        # self.y += deltay


p = Point()
# print(p.get_coord())
p.setx(5)
# p.sety(10)
# p.move(15, 10)
# print(p.get_coord())

# print(vars(p))


# * Point - version 2 - magic/dunder methods

# magic/dunder ("double underline") methods
# Note that these methods must be named correctly as they will be called automatically only if the name is typed exactly as required

#  __init__ /constructor

# method responsible for initializing objects
# called automatically when a Point object is constructed

# p = Point() calls Point.__init__(p)
# p = Point(2,3) calls Point.__init__(p,2,3)


def __init__(self, x=0, y=0):
    self.x = x
    self.y = y


# __repr__


def __repr__(self):
    return f"Point({self.x}, {self.y})"


# __eq__
# called automatically when two objects are compared

# p==q calls Point.__eq__(p,q)


def __eq__(self, other):
    # if self.x == other.x and self.y == other.y:
    #     return True
    # else:
    #     return False

    return self.x == other.x and self.y == other.y


# Point Class - Version 2 (With Magic Methods)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Automatically called when printing the object or using repr()
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Automatically called when adding two Point objects using the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Automatically called when using str() or printing the object
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Optional: You can add more dunder methods for subtraction, equality, etc.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


# Example usage (v2):
p1 = Point(2, 3)
p2 = Point(4, 5)

# Automatically uses __repr__() when printing the object
# print(p1)  # Output: (2, 3)
# print(p2)  # Output: (4, 5)

# Adding two points using the + operator (calls __add__())
p3 = p1 + p2
# print(p3)  # Output: (6, 8)

# Checking equality (calls __eq__())
p4 = Point(2, 3)
# print(p1 == p4)  # Output: True (because they have the same coordinates)

p4 = p2 - p1
# print(p4)



#  magic/dunder methods

#  +    =>                 __add__
#  <    =>                 __it__
#  <=   =                  __le__
# obj[index]               __getitem__
# obj[index]=value         __setitem__


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.height <= other.height


p1 = Person("John", 36, 200)
p2 = Person("Smith", 40, 200)
# print(p1 < p2)
# print(p1 <= p2 )


class Squares:
    def __init__(self, max_num):
        self.max_num = max_num

    def __getitem__(self, index):
        if index < 0 or index >= self.max_num:
            raise IndexError("Index out of range")
        return index**2


# Example usage
squares = Squares(10)
# print(squares[3])  # Output: 9 (since 3^2 = 9)
# print(squares[5])  # Output: 25 (since 5^2 = 25)


class CustomList:
    def __init__(self, size):
        self.data = [0] * size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise ValueError("Only integer values are allowed")
        self.data[index] = value


# Example usage
custom_list = CustomList(6)
# custom_list[5] = 10
# print(custom_list[5])  # Output: 10

# try:
#     custom_list[2] = "hello"  # Raises ValueError
# except ValueError as e:
#     print(e)  # Output: Only integer values are allowed


# ------------------------------------------------------------------------------------------


# * movePointAround - a Point client

# it is not indented in the module, it exists at the same level of indentation as Point
# it needs the Point class, in order to work.
# But, the Point class does not need the client.

# movePointAround is a Point CLIENT
# uses services of Point class
# but is NOT part of (inside) the Point class


def movePointAround():
    x, y = eval(input("Enter a point: "))
    pt = Point(x, y)

    while True:
        ans = input("Move it how? ")
        if ans == "":
            break
        else:
            dx, dy = eval(ans)
            pt.move(dx, dy)
            print(pt)

    # dont convert to a str
    return pt


# * A client function is a standalone function that uses (or "calls") methods of a specific class to perform actions or calculations, without being part of the class itself.

# * It's essentially a function that depends on the services provided by a class but is written outside that class.

# Client functions make it easier to separate what a class does (its core functionality)


# Point class (defines core functionality)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Client function (uses Point's methods but is not part of the class)
def movePointAround():
    x, y = eval(input("Enter a point (e.g., 3,4): "))
    pt = Point(x, y)
    print(f"Your current point is {x,y}")

    while True:
        ans = input("Move it how? (Enter dx,dy or press Enter to quit): ")

        if ans == "":
            break
        else:
            dx, dy = eval(ans)
            pt.move(dx, dy)
            print(pt)  # Uses Point's __repr__ method to print its current position


# movePointAround()


# * eval and tuple assignment

# The above client makes use of eval and tuple assignment.  IDLE notes:

# >>> ans = "1,1\n"
# >>> ans
# '1,1\n'
# >>> eval(ans) # produces tuple
# (1, 1)
# >>> # tuple assignment
# >>> x,y = (3,4)
# >>> x
# 3
# >>> y
# 4
# >>> ans
# '1,1\n'
# >>> x,y = eval(ans)
# >>> x,y
# (1, 1)
# >>>


# * == vs. is

#  == - compares the attributes/contents of the objects, do they have the same value?
#  is - compares memory location of objects, do two names actually refer to the same object in
# memory?

lst = [1, 2]
lst2 = [1, 2]

lst == lst2  # True
lst is lst2  # False

# print(id(lst), id(lst2)) # (2440175090824, 2440175089096)

lst3 = [1, 2]
lst4 = lst3

lst == lst2  # True
lst is lst2  # True

id(lst), id(lst2) #(2440177339144, 2440177339144)
