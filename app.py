saw = {
    "name": "Saw",
    "age": 23,
    "single": True,
    "married": False,
    "pets": None,
    "friends": ("Saw Yadana", "Phone Myint Kyaw", "Na Na"),
    "phones": [
        {"model": "iPhone 11", "color": "black"},
        {"model": "iPhone SE", "color": "space grey"},
    ],
}

# dict

a = [1, 2, 3]
# b = a  # aliasing
b = a[:]

# print(a == b)
# print(a is b)


# When two variables are aliases, any change made to the object through one variable will be reflected when accessed through the other variable

import random

# print(random.randrange("HT"))

lst = []
# lst.extend([2])

# list.extend(lst, [2])

# list.extend([2])

# print(lst)

# print(str.__add__("apple", "pear"))

# print(str(__add__, "apple", "pear" ))


# class MyList(list):
#     def append(self, item):
#         self.append(item)
    
#     def __setitem__(self, index, item):
#         self[index] = item

# def enqueue(self, item):
#     self.q.append(item)

class SomeList(list):
    def __init__(self, iterable=[]):
        self.lst = list(iterable)
    
s = SomeList([1,2])
s.append(3)
# print(len(s))

class Queue():
    def __init__(self, lst=[]):
        self.q = list(lst)
    
    def enqueue(self, item):
        self.q.append(item)
    
    def dequeue(self):
        return self.q.pop(0)

q = Queue([1,2,3])
q.enqueue(4)
item = q.dequeue()
# print(item, q)


class MyList(list):
    def append(self, item):
        self.append(item)
    
    def __setitem__(self, index, item):
        self[index] = item

