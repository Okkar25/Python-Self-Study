# Python provides a variety of decorators that are commonly used in object-oriented programming (OOP) and functional programming to enhance the functionality of functions, methods, or classes. Here's a list of some useful and frequently used decorators:

# 1. @staticmethod
# Used to define a method that belongs to the class but does not operate on an instance or modify class-level state.
# It does not receive an implicit first argument (self or cls).
# Example:


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Usage:
print(MathOperations.add(5, 10))  # 15

# 2. @classmethod
# Similar to @staticmethod, but it receives the class as its first argument (cls), making it useful for methods that need to work with class-level data.
# Example:


class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Usage:
obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # 2


# 3. @property
# We already discussed this one. It allows defining getter, setter, and deleter for class attributes in a more elegant way.
# Recap:


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Usage:
person = Person("Okkar")
print(person.name)  # Okkar
person.name = "Aung"
print(person.name)  # Aung


# 4. @functools.lru_cache
# This decorator from the functools module is used to cache the result of a function based on its arguments. It's useful for functions that are called multiple times with the same arguments, such as in recursive functions.
# Example:


import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Usage:
print(fibonacci(30))  # 832040 (calculated efficiently with caching)


# 5. @functools.wraps
# This decorator is used to preserve the metadata (such as function name and docstring) of the original function when a decorator wraps another function.
# Example:


import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This is a simple function to say hello."""
    print("Hello!")

# Usage:
say_hello()
print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)   # This is a simple function to say hello.



# 6. @dataclass
# The @dataclass decorator is used to automatically generate special methods (like __init__(), __repr__(), etc.) for classes that are primarily used to store data. It comes from the dataclasses module.
# Example:


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Usage:
p = Point(5, 10)
print(p)  # Point(x=5, y=10)



# 7. @abstractmethod (from abc module)
# Used to define an abstract method that must be implemented in a subclass. It's part of defining abstract base classes (ABCs) in Python.
# Example:


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

# Usage:
dog = Dog()
print(dog.sound())  # Woof

# Note: You can't instantiate the Animal class directly since it has an abstract method.
# animal = Animal()  # Raises TypeError



# 8. @contextmanager (from contextlib module)
# A decorator used to create a context manager without needing to define a full class with __enter__() and __exit__() methods.
# Example:


from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    file = open(path, mode)
    try:
        yield file
    finally:
        file.close()

# Usage:
with open_file("test.txt", "w") as f:
    f.write("Hello, World!")
    
    
# 9. @synchronized (custom decorator for thread safety)
# In multithreading, you might want to make a function thread-safe. You can create a custom decorator like @synchronized.
# Example:


import threading

def synchronized(lock):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return inner
    return wrapper

lock = threading.Lock()

class Counter:
    def __init__(self):
        self.count = 0
    
    @synchronized(lock)
    def increment(self):
        self.count += 1

# Usage:
counter = Counter()


# 10. Custom Decorators
# You can also create your own decorators to suit your needs. For instance, you could log the execution of a function or check certain preconditions before a function is called.
# Example:


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_execution
def say_hello():
    print("Hello!")

# Usage:
say_hello()