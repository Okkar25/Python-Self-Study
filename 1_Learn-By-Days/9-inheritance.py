# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# * Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
   
    def get_name(self):
        return f"My name is {self.fname} {self.lname}" 
    
    def __repr__(self):
        return f"{{ first_name : {self.fname}, last_name : {self.lname} }}"
        
    
p1 = Person("Okkar", "Aung")
# print(p1)
# print(p1.get_name())
# print(p1.fname)


# * Create a Child Class

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# class Student(Person):
#     pass 

# Now the Student class has the same properties and methods as the Person class.
# st = Student("John", "Wick")
# print(st.get_name())


# * Add the __init__() Function

# The __init__() function is called automatically every time the class is being used to create a new object.
# * When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
# * To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class Student(Person):
#     def __init__(self, fname, lname, major):
#         super().__init__(fname, lname)
#         self.major = major


# class Student(Person):
#     def __init__(self, fname, lname, major):
#         Person.__init__(self, fname, lname)
#         self.major = major
        
# st1 = Student("John", "Wick", "Computer Science")
# print(st1.major)


# * Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
    def __init__(self, fname, lname, major, year):
        super().__init__(fname, lname)
        self.major = major
        self.graduation_year = year
        
    def get_major(self):
        return f"Welcome {self.fname} {self.lname}! You get accepted into our {self.major} department of class {self.graduation_year}"
        
st1 = Student("John", "Wick", "Computer Science", 2028)
# print(st1.graduation_year)


# * Add Methods
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

class Student(Person):
    def __init__(self, fname, lname, major, year):
        super().__init__(fname, lname)
        self.major = major
        self.graduation_year = year
        
    def welcome(self):
        return f"Welcome {self.fname} {self.lname}! You get accepted into our {self.major} department of class {self.graduation_year}"
     
     # override parent method 
    def get_name(self):
        return f"You name is now {self.fname} Bobby {self.lname}"
        
st1 = Student("John", "Wick", "Computer Science", 2028)
# print(st1.welcome())
# print(st1.get_name())

