# Python Iterators

# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

# * Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.


fruits = ["apple","orange", "grape", "peach"]


iter_fruits = iter(fruits)
# print(next(iter_fruits))
# print(next(iter_fruits))
# print(next(iter_fruits))
# print(next(iter_fruits))

# * Even strings are iterable objects, and can return an iterator

# str = "instrument"
# iter_str = iter(str)
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))
# print(next(iter_str))


# * Looping Through an Iterator

tuple = ("apple","orange", "grape", "peach")
# for i in str:
#     print(i)


# * The for loop actually creates an iterator object and executes the next() method for each loop



# --------------------------------------------------------------------------------------------------



# **** Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# __init__() allows you to do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence

# Example
# * Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

# invoked automatically  =>  __iter__() / __next__()
# Double Underscore Method => dunder method



# class MyIterable:
#     def __iter__(self):
#         return iter([1, 2, 3])

# obj = MyIterable()
# for item in obj:  # __iter__() is called automatically
#     print(item)


# =========================================================================================


class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        y = self.x
        self.x += 1
        return y
    
    def __repr__(self):
        return f"This is __repr__() {self.x} automatically invoked"
    
    def __str__(self):
        return f"This is __str__() {self.x} automatically invoked"
    
my_obj = MyNumbers() # instantiation # object created
my_iter = iter(my_obj) # iterator object created

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# print(my_obj.__str__())
# print(my_obj.__repr__())

# print(str(my_obj))
# print(repr(my_obj))
# print(my_obj)


class MyNumbers: 
    def __iter__(self):
        self.start = 1
        return self 
    
    def __next__(self):
        next_seq = self.start
        self.start += 1
        return next_seq
    
my_class = MyNumbers()
my_iter = iter(my_class) # iterator 

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))



# =========================================================================================



# * StopIteration

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times


class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x <= 10:
            y = self.x
            self.x += 1
            return y
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

# print(next(my_iter))

# for i in my_iter:
#     print(i)
    