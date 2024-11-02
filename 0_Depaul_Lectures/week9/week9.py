# Container classes

# "Review": assignment and copies

lst = [2, 3, 4]
lst1 = lst

lst2 = lst[:]
lst3 = list(lst)

lst == lst1
lst is lst1

lst == lst2
lst is lst2

lst == lst3
lst is lst3

# * Queue - composition

# enqueue objects to the back and dequeue objects from the front
# This implementation will use composition, another implementation using inheritance.

# before writing a method, decide how it should function.  Should it:
#  modify/set
#  return/get
#  both


class Queue:
    # def __init__(self, lst=[]):
    #     self.q = list(lst)

    def __init__(self, lst=[]):  # runs once
        # body runs every time!
        # fix: call constructor in body
        self.q = lst  # <====== the final version has self.q = list(lst)

    def __repr__(self):
        return f"Queue({self.q})"

    def enqueue(self, item):  # set / modify
        self.q.append(item)

    def dequeue(self):  # modify and return
        return self.q.pop(0)
        # return self.q.pop(-1)

    # q[1] -> Queue.__getitem__(1)

    def __getitem__(self, index):
        return self.q[index]

    # len(q) => Queue.__len__(q)
    def __len__(self):
        return len(self.q)

    def __eq__(self, other):
        return self.q == other.q

    def __add__(self, other):
        return Queue(self.q + other.q)


q1 = Queue()
q2 = Queue()

q1.enqueue(2)
q2.enqueue("apple")

# q1.dequeue()

# print(q1)
# print(q2)

# print(q1 == q2)
# print(q1.q is q2.q)  # True
# print(q1 is q2) # False


a = [1, 2, 3]
b = a
# b = a[:]
# b = list(a)

b.append(10)

# print(a)
# print(b)

# print(a == b)
# print(a is b)

# a = [1, 2, 3]; b = a: a is b is True because b is an alias for a, referencing the same list object.
# q1 = Queue(); q2 = Queue(): q1 is q2 is False because each Queue() call creates a new, unique object in memory.


# Sets

my_set = set()

# Add elements
my_set.add("apple")
my_set.add("banana")

# Check if an element exists
# print("apple" in my_set)  # Output: True

# Hashing example
# print(hash("apple"))

#  to create a set:
#  {item, item, item, ...}
#  set() - empty set

#  modifying sets:
#  add(item) - adds, but not duplicates
#  remove(item) - removes or error if not there
#  discard(item) - removes, does not cause error if not there
#  update(iterable) - iterated add
#  union, intersection

# operators:
#  in, not in - containment/iteration, super fast
#  & - intersection
#  | - union

s = {2, 99, 3, 4, 6}
# s.add([10, 20])
s.add((10, 20))
# print(s)

# * In sets, the items are hashable (constant) so lists cannot be added only tuples (constant too)

# * sets require their elements to be hashable (which means they cannot change), mutable objects like lists cannot be added to sets.

# s[2] # 'set' object is not subscriptable


# * creating an empty set (important)
# empty set
s = set()

# empty dict
d = {}

s = {}
# s.add(5)
# print(s)


x = set([1, 2, 3, 2, 2, 2, 2, 2, 5, 6, 1, 1])
# print(x)
y = set("abracadabra")


# * set() constructor expects an iterable as its argument, such as a list, tuple, string, or another set.
# int is not iterable
# set( 5 )

my_set = {1, 2, 3}

my_set.add(4)
# my_set.add([5,6,7]) # not hashable
# my_set.add((5,6,7))
my_set.update([5, 6, 7])
my_set.update((8, 9, 10))

# print(my_set)

intersect = {2, 3, 4, 5, 6} & {3, 5, 7, 9}

union = {2, 3, 4, 5, 6} | {3, 5, 7, 9}


# * inheritance

# inherited=sub=child class
# base=super=parent class

# An object of the subclass is also an instance of, and has the methods of, the super class.

# A sub class has 4 types of methods:
#  0. inherited - Don't write, use super method
#  1. overridden - replace super's method
#  2. added - new method
#  3. extended - modify super's method

lst = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# v1 - simplest example, NO NEW functionality
# class MyList(list):  # subclass/inherit from list
#     pass


# m = MyList()
# m.append(1)
# m.append(2)
# m.append(4)
# m.append(7)

# m.pop()
# m[1]

# print(m)
# print(type(m))
# print(isinstance(m, MyList))
# print(isinstance(m, list))


# Here is our version of MyList , it
# removes the spacing displayed between items
# adds an apply method
# inheritance: self IS a list INSTANCE


class MyList(list):
    # INHERIT: append, pop, ...

    # OVERRIDE repr
    def __repr__(self):
        # accumulate a str (without spaces)
        ans = "["
        for item in self:
            ans += repr(item) + ","
        return ans[:-1] + "]"  # remove the trailing comma [1,2,3,]

    # ADDED method
    def apply(self, function):
        for i in range(len(self)):
            self[i] = function(self[i])

def add_ten(num):
    return num + 10


m = MyList([1, 2, 3, 4, 5])
m.append(10)
# print(m)

m.apply(add_ten)

print(m)

