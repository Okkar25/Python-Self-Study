# one of collection data types 
# A tuple is a collection which is ordered and unchangeable

this_tuple = ("apple", "banana", "cherry")
# print(this_tuple)

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value

this_tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
# print(this_tuple1)

# len() 
# print(len(this_tuple1))

# ***** Create Tuple With One Item *****
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

tuple_one_item = ("apple" )   # string 
tuple_one_item1 = ("apple", )  # tuple

# print(type(tuple_one_item1), tuple_one_item1)
# print(type(tuple_one_item), tuple_one_item)


# A tuple with strings, integers and boolean values:

tuple_all_data = ("abc", 34, True, 40, "male")


# The tuple() Constructor

list1 = ["apple", "banana", "cherry"]
set = { 34, 5, 90, 68, 12,  23, 10, 222 }


tuple_list = tuple(list1)

# print(tuple_list, type(tuple_list))


# Python Collections (Arrays)

# * Set items are unchangeable, but you can remove and/or add items whenever you like.

# * number set shows like ordered but it is not 
# * because it is small values 

set1 = { "apple", "banana", "cherry", "grape", "peach" }
set2 = { 34, 5, 90, 68, 12,  23, 10, 222 }
set3 = { 34, 5, "banana", 68, True,  23, 10, "peach", False }

# print(set, type(set))

set3.add("strawberry")
set3.remove(10)
# print(set3)


# ==============================================================================================


# Access Tuples 

this_fruits = ("apple", "banana", "cherry")

# print(this_fruits[2])
# print(this_fruits[-2])

this_fruits1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# range of indexes
# print(this_fruits1[2:5])
# print(this_fruits1[:4])
# print(this_fruits1[2:])
# print(this_fruits1[-4:-1])
# print(this_fruits1[-4:])


# if "melon" in this_fruits1:
#     print("Yes it exists")
# else:
#     print("No it does not exist")


# new_fruits = [ "Yes it exists" if fruit == "kiwi" else "No it doesn't exist" for fruit in this_fruits1 ]
# new_fruits = [ "Yes it exists" for fruit in this_fruits1 if fruit == "kiwi"]

# print(new_fruits)


# *** Update Tuples 
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. ***** But there are some workarounds.

x = ("apple", "banana", "cherry")

# x[0] = "guava"
# print(x[0])

# print("first value", x)

# y = list(x)
# y[0] = "guava"
# x = tuple(y)

# print("second value", y)
# print("third value", x)


#  Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.


# y = list(x)
# y.append("water melon")
# x = tuple(y)

# print(x)


# * Add tuple to a tuple

# y = ("strawberry", )
# x += y

# print(x)

# * Remove Items

# y = list(x)
# y.remove("banana")
# x = tuple(y)

# print(x)


# **** del => keyword 

# y = list(x)
# y.clear()
# x = tuple(y)
# print(x)

# del x 
# print(x)


# =============================================================================================


# **** Unpacking a Tuple


# When we create a tuple, we normally assign values to it. This is called "packing" a tuple

fruits_pack = ("apple", "banana", "cherry", "melon", "mango")


# extract the values back into variables. This is called "unpacking

(a, b, c, d, e) = fruits_pack  # unpacking 

# print(a,b,c, d, e)

# **** The number of variables must match the number of values in the tuple
# *** if not, you must use an asterisk to collect the remaining values as a list.


# ** Using Asterisk => *

# (a, b, *c) = fruits_pack

(a, *b, c) = fruits_pack

# print(a, b, c)

# * Loop 

empty_tuple = ()
empty_list = list(empty_tuple)

# for fruit in fruits_pack:
#     empty_list.append(fruit)
#     empty_tuple = tuple(empty_list)
# print("items in empty tuple", empty_tuple)


# for index in range(len(fruits_pack)):
#     print(index, fruits_pack[index])


# index = 0

# while index < len(fruits_pack):
#     print(fruits_pack[index])
#     index += 1


# ** Join Tuple 

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# list1 = list(tuple1)
# list1.append(tuple2)
# print(tuple(list1))

# multiply tuple
# result = tuple1 * 2
# print(result)


# Tuple Methods 
# count()
# index()

num_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# print(num_tuple.count(8))
# print(num_tuple.index(8))

