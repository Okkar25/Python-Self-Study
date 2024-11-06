# Inheritance is a programming mechanism that allows us to customize/modify an existing class instead
# of building from scratch.

# inherited   =>   sub     =>   child class
# base        =>   super   =>   parent class

# * An object of the subclass is also an instance of, and has the methods of, the super class.

# A sub class has 4 types of methods:
#  0. inherited - Don't write, use super method
#  1. overridden - replace super's method
#  2. added - new method
#  3. extended - modify super's method


class SuperClass:
    def greet(self):
        print("Hello from SuperClass")


class SubClass(SuperClass):
    def greet(self):  # Override
        print("Hello from SubClass")


class SubClass(SuperClass):
    def new_method(self):  # Added
        print("This is a new method in SubClass")


class SubClass(SuperClass):
    def greet(self):  # Extended
        super().greet()  # Call the original method
        print("and also from SubClass")  # Extend functionality


# * Queue_inherit

# implement the
# Queue class using inheritance instead of composition
#  self does not have any attributes
#  mantra ( repetition ): the list is self
#  do not mix inheritance and composition
#  watch out for circular definitions that cause infinite recursion


# * Circular Definitions in Class Methods


class CircularQueue:
    def enqueue(self, item):
        self.enqueue(item)  # Unintentional self-call, causes infinite recursion


# Circular Definitions and Inheritance

# In the context of inheritance, circular definitions can happen if a method in a subclass calls a method from the superclass, which somehow indirectly calls back into the subclass's method, forming an unending cycle.


class Parent:
    def action(self):
        return self.do_action()


class Child(Parent):
    def do_action(self):
        return self.action()  # Calls Parent's action, causing a loop


# voiding Circular Definitions

# Avoiding Circular Definitions in Class Methods by Using a Clear Method Structure


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0


# Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
# print(q.dequeue())  # Output: 1


# Example of Circular Dependency Between Superclass and Subclass Methods


class Parent:
    def action(self):
        print("Action in Parent")
        self.extra_action()  # Calls the subclass method

    def extra_action(self):
        print("Extra action in Parent")  # Default implementation


class Child(Parent):
    def action(self):
        print("Action in Child")
        super().action()  # Calls Parent's action

    def extra_action(self):
        print("Extra action in Child")
        self.action()  # Calls Child's action, causing a loop


# Avoiding Circular Dependency


class Parent:
    def action(self):
        print("Action in Parent")
        self.extra_action()  # Calls the subclass's extra_action if it exists

    def extra_action(self):
        print("Extra action in Parent")  # Default implementation


class Child(Parent):
    def action(self):
        print("Action in Child")  # Override without calling super().action()
        self.extra_action()  # Explicit call without super() loop

    def extra_action(self):
        print("Extra action in Child")


c = Child()
p = Parent()
# c.action()
# p.action()


# Queue_inherit

# implement the
# Queue class using inheritance instead of composition
# self does not have any attributes
# mantra: the list is
# self
# do not mix inheritance and composition
# watch out for circular definitions that cause infinite recursion


class CuttingError:
    pass


class Queue(list):
    # EXTENDED method
    def __repr__(self):
        return f"Queue({list.__repr__(self)})"
        # return f"Queue({super().__repr__()})"
        # return f"Queue({self})"  # circular definitions

    # ADDED methods
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    # q[1] = 'Sally' -> Queue.__setitem__(q,1,'Sally')

    def __setitem__(self, index, item):
        # raise CuttingError('no cutting, you bad code!')
        self[index] = item  #  leading to infinite recursion => Queue.__setitem__
        list.__setitem__(self, index, item)
        super().__setitem__(index, item)

    # inherit:
    # __getitem__,__eq__, __len__

    # EXTEND
    def __add__(self, other):
        return Queue(list.__add__(self, other))
        # return Queue(super().__add__(other))
        # dont do this - CIRCULAR
        # return Queue( self + other )


# note: circular definitions
# Be careful about circular definitions.  They will cause infinite recursion:


class Queue(list):
    # circular, causes infinite recursion
    def __repr__(self):
        return f"Queue({self})"


# To execute either return statement:

#  self must be converted to a str
#  this calls __repr__ !
#  which __repr__ ?
#  self is a Queue
#  this calls Queue.__repr__ !
#  method calls itself
#  circular definition/infinite recursion
#  produces: "Queue(Queue(Queue(Queue(Queue(...))))"


# CuttingError
# custom exception


class CuttingError(Exception):
    pass

