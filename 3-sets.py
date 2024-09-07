#  A set is a collection which is unordered, unchangeable*, and unindexed
# Set items are unchangeable, but you can remove items and add new items
# Set items are unordered, unchangeable, and do not allow duplicate values.

my_set = {"apple", "banana", "cherry"}
dupli_set = {"apple", "banana", "cherry", "apple", "cherry"}

# print(dupli_set)

# * values True and 1 are considered the same value in sets, and are treated as duplicates

this_set = {"apple", "banana", "cherry", True, 1, 2}
# print(this_set)

# * values False and 0 are considered the same value in sets, and are treated as duplicates

this_set1 = {"apple", "banana", "cherry", False, 1, 2, 0}
# print(this_set1)

# len(this_set)
# type(this_set)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


# *** The set() Constructor 

is_set = set(["apple", "banana", "cherry"]) # casting
is_set1 = set(("apple", "banana", "cherry")) # constructor # the double round-brackets

# print(is_set1)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# * Access Items
# You cannot access items in a set by referring to an index or a key

this_fruit_set = {"apple", "banana", "cherry","peach"}

# for x in this_set:
#   print(x)

# print("banana" in this_fruit_set)
# print("banana" not in this_fruit_set)


# * Add Items / Change Items
# Once a set is created, you cannot change its items, but you can add new items.


# this_fruit_set.add("water melon")
# print(this_fruit_set)


# * Update Items => adding two sets 

new_fruits = {"melon", "strawberry", "guava"}
# new_fruits.update(this_fruit_set)

# new_fruits.add(this_fruit_set)  # error 
# x = new_fruits + this_fruit_set # error

# print(new_fruits)


# * Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object

my_list = ["kiwi", "orange"]

new_fruits.update(my_list) 
# print(new_fruits)


# ----------------------------------------------------------------------------------------------

# ***** Remove Items
# To remove an item in a set, use the remove(), or the discard() method

fruit_set = {"apple", "banana", "cherry"}
# fruit_set.remove("cherry")

# * If the item to remove does not exist, remove() will raise an error
# fruit_set.remove("peach")

# * If the item to remove does not exist, discard() will NOT raise an error.
# fruit_set.discard("cherry")
# fruit_set.discard("peach")

# print(fruit_set)


# * pop()

# pop_item = fruit_set.pop()
# print(fruit_set, pop_item)

# * clear()

# fruit_set.clear()
# print(fruit_set) # set()

# * del keyword 

# del fruit_set
# print(fruit_set)


# ***** Loop sets 

# for fruit in fruit_set:
#     print(fruit)


# ----------------------------------------------------------------------------------------------


# ******** Join Sets

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# *** union() => | operator 

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)


# * Join Multiple Sets

# All the joining methods and operators can be used to join multiple sets
# add more sets in the parentheses, separated by commas

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# my_set = set1.union(set2,set3,set4)
# my_set = set1 | set2 | set3 | set4

# print(my_set)


# * Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# z = x | y # error 
# print(z)

# | operator  =>  join sets with sets
# union()     =>  join sets with other data types 


# * update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# print(set1)

# set1.update(set2)
# print(set1)

# * Both union() and update() will exclude any duplicate items



# -------------------------------------------------------------------------------------------



# **** Intersection

# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set2 = ("google", "microsoft", "apple")

# set3 = set1.intersection(set2)
# set3 = set1 & set2 
# print(set3)

# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.


# * intersection_update()

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)
# print(set1)

# * The values True and 1 are considered the same value. The same goes for False and 0.

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1 & set2 
# set3 = set1.intersection(set2) 
# print(set3)

# set1.intersection_update(set2)
# print(set1)


# ------------------------------------------------------------------------------------------------


# ***** Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)
# set3 = set2.difference(set1)
# print(set3)


# * you can use - operator instead of the difference() method

# set3 = set1 - set2
# set3 = set2 - set1
# print(set3)

# * The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method


# * difference_update()

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)
# set2.difference_update(set1)
# print(set2)



# **** Symmetric Differences

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# *** you can use ^ operator instead of the symmetric_difference() 


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
# print(set3)

# * The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.


# * symmetric_difference_update()

# set1.symmetric_difference_update(set2)
# set2.symmetric_difference_update(set1)
# print(set2)



# -----------------------------------------------------------------------------------------------------



# *** Set Methods 

# add()	 
# clear()
# copy()	 	
# difference()	-	
# difference_update()	-=	
# discard()	 	
# intersection()	&	
# intersection_update()	&=	

# isdisjoint()	 	             Return True if no items in set x is present in set y:
# issubset()	                 Return True if all items in set x are present in set y

# issuperset()	                 

# pop()	 
# remove()	 
# symmetric_difference()	^	
# symmetric_difference_update()	^=	
# union()	|	
# update()	|=	


# https://www.w3schools.com/python/python_sets_methods.asp



# Problem 8: Count Unique Words in a Sentence
# Problem:
# Given a sentence, count how many unique words there are.

# python
# Copy code

# # Solution
def count_unique_words(sentence):
    words = sentence.split()
    return len(set(words))

# Example usage
sentence = "the cat is in the hat the cat"
result = count_unique_words(sentence)
print(result)  # Output: 5


# Problem 10: Check if a Set is Empty
# Problem:
# Check if a set is empty or not.

# python
# Copy code
# Solution
def is_empty(s):
    return len(s) == 0

# Example usage
s = set()
result = is_empty(s)
print(result)  # Output: True