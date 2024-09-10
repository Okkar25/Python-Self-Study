# Python Classes and Objects

# Python is an object oriented programming language
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# * Create a Class

class MyClass:
    x = 5  # property

# * Create Object - JS instantiation
p1 = MyClass()
# print(p1.x)


# *** The __init__() Function - constructor 

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       
    def __str__(self):
        return f"Person : {self.name}, Age : {self.age}"
       
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    

p1 = Person("Okkar", 23)

# print(p1) # main object 

# print(p1.__str__()) 
# print(p1.__repr__()) 

# print(repr(p1))
# print(str(p1))

# print(p1.name)
# print(p1.age)


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def __str__(self):
        return f"This is a {self.brand} car in {self.color} color"
    
    def __repr__(self):
        return f"This is a {self.color} {self.brand} car"
    
car1 = Car("Toyota", "Black")
# print(car1)
# print(car1.__repr__())
# print(car1.__str__())
# print(repr(car1))
# print(str(car1))


# The __init__() function is called automatically every time the class is being used to create a new object.


# * The __str__() Function

# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
#   def __str__(self):
#     return f"{self.name}({self.age})"

p1 = Person("John", 36)

# without __str__ function <__main__.Person object at 0x0000026A8FDDDCA0>
# print(p1) 


# * Object Methods

# Objects can also contain methods. Methods in objects are functions that belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # getter function
    # @property # ** decorators 
    def get_age(self):
        return self.age
    
    # setter function
    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be less than 0") 
        
        self.age = new_age
        
    def greeting(self):
        return f"Greeting. My name is {self.name}"

p1 = Person("Okkar", 23)
# print(p1.age)         # property 
# print(p1.greeting())  # method

# * property is accessed without parenthesis ()
# * method is accessed with parenthesis ()

# print(p1.get_age()) # getter 
# p1.set_age(50)
# print(p1.get_age()) # setter  

# print(p1.get_age)


# * The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# * It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Student:
    def __init__(mysillyobject, major, year, GPA):
        mysillyobject.major = major
        mysillyobject.year = year
        mysillyobject.__GPA = GPA # private value 
    
    def get_GPA(self):
        return f"My overall GPA is {self.__GPA}"
    
    # @property
    def get_major(hello):
        return f"My major is {hello.major}"    
    
st1 = Student("Computer Science", "Sophomore", 3.5)
# print(st1.get_major())
# print(st1.year)
# print(st1.__GPA)
# print(st1.get_GPA())


# * Modify Object Properties

st1.year = "Third Year"
# print(st1.year)


# * Delete Object Properties
# You can delete properties on objects by using the del keyword

# del st1.year
# print(st1.year)


# * Delete Objects

# del st1
# print(st1)


# * The pass Statement

# class Person:
#     pass 

