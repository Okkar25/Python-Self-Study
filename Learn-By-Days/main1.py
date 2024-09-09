# operators 
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# + - * / // % ** 

# Assignment operators
# =  +=  -=  *=  /=  //=  %=  **=  

# Comparison operators
# ==  !=  >  <  >=  <=  

# Logical operators
#  and  or  not 

# Identity operators
# is  / is not

fruits1 = ["peach", "orange", "grape"]
fruits2 = ["peach", "orange", "grape"]

fruits3 = fruits1
fruits3.append("water melon")

# print(fruits1 == fruits2)
# print(fruits1 == fruits3)

# print(fruits1 is fruits2)
# print(fruits1 is fruits3)

# print(fruits1)
# print(fruits3)

# Modifications That Change the Object ********

# 1 
# Reassigning a Variable:
fruits = ["apple", "banana"]
fruits = ["cherry", "date"]

# 2 
# Creating a New List from an Existing One
fruits = ["apple", "banana"]
new_fruits = fruits[:]
# print(new_fruits)

# 3
# Using List Comprehensions
fruits = ["apple", "banana"]
new_fruits = [fruit.upper() for fruit in fruits]
# print(new_fruits is fruits)

# 4
# Using Functions that Return New Lists
fruits = ["apple", "banana"]
new_fruits = list(map(str.upper, fruits))
# print(new_fruits)


# Membership Operators

x = ["One", "Two", "Three"]
# print("Six" not in x)
# print("One" in x)


# Operator Precedence

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
# print((6 + 3) - (6 + 3))


# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions
# print(100 + 5 * 3)


# https://www.w3schools.com/python/python_operators.asp


# If two operators have the same precedence, the expression is evaluated from left to right.
# print(5 + 4 - 7 + 3)



#  -----------------------------------------------------------------------------------------------------



# list set tuple 
# collection type


# list []   = mutable, most flexible, accepts duplicates
# Tuple ()  = immutable, faster, accepts duplicates
# Set {}    = mutable ( add / remove ), unchangeable ( no update ), unordered, NO duplicates, best for membership testing


fruits = ["peach", "banana", "grape","coconut","guava"]
fruits[0]
# fruits[3] = "mango" # mutable
# fruits[5] # out of range

# fruits[3] = "melon"
fruits.append("melon")
fruits.append("melon")
fruits.append("melon")
fruits.remove("banana")
fruits.pop(1)
fruits.clear()
# print(fruits[3])

# print(fruits)


# for fruit in fruits:
#     print(fruit, end="-")


fruits1 = ("peach", "banana", "grape","coconut","guava") # cannot be changed 


# fruits1[0] = "strawberry" # does not support

# fruits1.append("blueberry")
# fruits1.remove("grape")
# fruits1.pop(1)
# fruits1.clear()


# sets - unordered / no indexing / arbitrary iteration  
# unordered => cannot access elements by their position or index
# No Repetition => Sets automatically handle duplicates.


fruits2 = {"apple1", "apple2", "apple3","apple4","apple5", "apple5","apple5"}


# fruits2[2] = "mango"
fruits2.add("mango")
fruits2.add("mango")
fruits2.add("blueberry")
# fruits2.remove("mango")
# fruits2.pop()
# fruits2.clear()

print(fruits2)

# for fruit in fruits2:
#     print(fruit, end=" ")

# searched_fruit = input("Insert a fruit to search : ")

# if searched_fruit in fruits2:
#     print(f"{searched_fruit} was found")
# else:
#     print(f"{searched_fruit} was not found")
        

# ******** when to use *********
# Uniqueness Enforcement            - when you need to ensure that all elements are unique
# Membership Testing                - checking if an element exists in the collection
# Set Operations                    - union / intersection 
# Removing Duplicates from a List   - can use a set to remove duplicates from a list and then convert it back to a list


# set_a = {10,20,30,40}
# set_b = {50,20,60,40, 70}

# print(set_a & set_b) # intersection 
# print(set_a | set_b) # union 


allowed_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3","192.168.1.3"]
filtered_ips = list(set(allowed_ips))
# print(allowed_ips)
# print(filtered_ips)


# ................................................................................



# Membership Testing in Lists
# How It Works: When you use the in keyword to check if an element is in a list, Python searches through the list from the beginning to the end until it finds the element or reaches the end of the list.

# Time Complexity:

# O(n): The time complexity for membership testing in a list is """"Linear""""" (O(n)), where n is the number of elements in the list. This is because, in the worst case, Python may need to check every element in the list before determining if the element is present or not.

my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("3 is in the list.")


# Membership Testing in Sets
# How It Works: Sets use a hash table to store elements, so when you check if an element is in a set, Python can directly compute the hash and check if it exists, rather than searching through all elements.

# Time Complexity:

# O(1): The average time complexity for membership testing in a set is constant time (O(1)). This makes sets much faster for membership testing, especially as the size of the collection grows.

my_set = {1, 2, 3, 4, 5}

if 3 in my_set:
    print("3 is in the set.")
    
    
# When to Use a List for Membership Testing

# Small Collections: If the list is small, the performance difference between a list and a set for membership testing might not be significant.
# Order Matters: If you need to maintain the order of elements and still want to perform membership testing, you might choose a list despite the performance trade-off.
# Duplicates Allowed: If you need to allow duplicates in your collection, a list is necessary because sets do not allow duplicate elements.


# When to Prefer a Set for Membership Testing

# Large Collections: As the size of your collection grows, using a set for membership testing becomes increasingly efficient.
# Uniqueness: When you need to enforce that all elements are unique, sets are ideal.
# Frequent Membership Tests: If your program frequently checks if elements are in a collection, using a set will improve performance.


# Example Comparing List and Set for Membership Testing

import time
# Large list and set
# operator 
large_list = list(range(1000000))
large_set = set(large_list)

print(large_list)

# Membership test for an element
start = time.time() # return current time
999999 in large_list
end = time.time()
print("List test time:", end - start)

start = time.time()
999999 in large_set
end = time.time()
print("Set test time:", end - start)



# --------------------------------------------------------------------------------------------


# Korea Problem

# items = {"Cola": 3, "Pepsi": 5, "Bubble Tea": 2}
# continue_adding = True
# secret_word = "Skywalker"
# print("Initial Items : ", items)

# def AddInventory(dict, name, num):
#     if name in dict:
#         dict[name] += num
#         print(items)
#     else:
#         dict[name] = num
#         print(items)


# while continue_adding:
#     item_name = input("Enter your item : ")
    
#     if item_name == secret_word:
#         print("Your updated items is : ", items)
#         break
        
#     item_qty = int(input("Enter item quantity : "))
#     AddInventory(items, item_name, item_qty)
# else:
#     print(items)










