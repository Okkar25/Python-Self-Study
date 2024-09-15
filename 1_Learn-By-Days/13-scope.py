# * Local Scope

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def my_func():
#   global x
  x = 300
#   print(x)

my_func()

# print(x)

def outer_func():
    x = 1000
    
    def inner_func():
        print(x)
        
    inner_func()
    
# outer_func()


# * Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

y = 500

def my_func1():
    print(y)
    
# my_func1()

# print(y)


# * same variable name inside and outside of a function

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function)

z = 1000

def this_func():
    z = 10
    print(z)
    
# this_func()
# print(z)


# * Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

def my_func():
  global x
  x = 300

# my_func()
# print(x)


# * use the global keyword if you want to make a change to a global variable inside a function

u = 700

def global_func():
    global u
    u = 200
    print(u)
    
# global_func()

# print(u) # override global u variable values 


# * Nonlocal Keyword

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def outer_func():
    x = "hello"
    
    print("outer x value", x)
    
    def inner_func():
        nonlocal x
        x = "world"
        print("inner x value", x)
        
    inner_func()
    
    print("outer x value", x)
    
# outer_func()
