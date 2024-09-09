# list

# List items are ordered, changeable, and allow duplicate values.

this_list = ["apple", "banana", "cherry"]
len(this_list)

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]


# The list() Constructor

this_list1 = list(("apple", "banana", "cherry"))
# print(list()) # empty list 


# collection data types

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. add / remove
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


this_list2 = ["apple", "banana", "cherry"]
# print(this_list2[1])
# print(this_list2[-1])

this_list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(this_list3[2:5]) # slice
# print(this_list3[:4])
# print(this_list3[3:])
# print(this_list3[-4:-1])

# if "apple" in this_list3:
#   print("Yes, 'apple' is in the fruits list")

# changeable 
this_list2[1] = "Peach"
# print(this_list2)

# Change a Range of Item Values
# slice method 

this_list3[2:4] = ["grape", "watermelon"]
# print(this_list3)

# insert more items than you replace
this_list2[1:2] = ["orange", "strawberry"]
# print(this_list2)

# insert less items than you replace
new_list = ["apple", "banana", "cherry", "peach"]
# new_list[1:3] = ["watermelon"]
# print(new_list)


# ** .insert() => does not replace existing elements 

# new_list.append("super melon")
# new_list.remove("banana")
# new_list.pop(2)
# new_list.insert(1, "super melon")
# print(new_list)


# ****** Popular list methods *********
# .slice()
# .insert()
# .append()
# .remove()
# .pop()
# .clear()
# .extend() / .concat() js  => can also combine lists / tuples / sets


list_a = [1,2,3,4]
list_b = [5,6,7,8]
list_c = (10,20,30,40) # tuples
list_d = {100,200,300,400} # sets

# combined_list = list_a + list_b
# extended_list = list_a.extend(list_b)
# list_a.extend(list_b)
list_a.extend(list_c)

# print(list_a)

# first occurrence
this_list4 = ["apple", "banana", "cherry", "banana", "kiwi"]
# this_list4.remove("banana")
# print(this_list4)

# pop() => index --> specify / no index --> last item 



# ***** del keyword ***** completely delete list to undefined 

# del this_list4[3]
# del this_list4 
# print(this_list4)

# this_list4.clear()
# print(this_list4)

# index looping 
this_list5 = ["apple", "banana", "cherry"]
# for i in range(len(this_list5)):
#   print(this_list5[i])


# i = 0
# while i < len(this_list5):
#     print(this_list5[i])
#     i += 1


# ******** List Comprehension ( shorthand property )

# [print(x) for x in this_list5]

# [ print(x.upper()) for x in this_list5 ]

# d = [ x.upper() for x in this_list5]
# print(d)  


# ---------------------------------------------------------------------------------------------


new_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_fruits_list = []

for fruit in new_fruits:
    if "e" in fruit:
        new_fruits_list.append(fruit)
        
# print(new_fruits_list)



new_fruits_list = [fruit for fruit in new_fruits if "a" in fruit]
# print(new_fruits_list)

non_apple_fruits_list = [fruit for fruit in new_fruits if fruit != "apple"]
# print(non_apple_fruits_list)


# ******* Syntax ************

# new_list = [expression for item in iterable if condition == True]

old_fruits_list = [fruit for fruit in new_fruits if "a" not in fruit and "i" not in fruit]
# print(old_fruits_list)



# Iterable ( list / tuple / set / range )


# new_arr = [x for x in range(10)]
new_arr = [x for x in range(10) if x < 5]
# print(new_arr)


# The expression is the current item in the iteration, but it is also the outcome
# can be manipulated before it ends up like a list item in the new list:

new_arr1 = [x.upper() for x in new_fruits]
new_arr1 = [ "hello" for x in new_fruits]
# print(new_arr1)



# ***** important 

fresh_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# fresh_fruits_list = [fruit for fruit in fresh_fruits if fruit != "banana"]
# fresh_fruits_list = [fruit if fruit != "banana" else "dragon fruit" for fruit in fresh_fruits]
fresh_fruits_list = ["dragon fruit" if fruit == "banana" else fruit for fruit in fresh_fruits]
# print(fresh_fruits_list)


# "Return the item if it is not banana, if it is banana return orange".


languages = ["JavaScript","Python","Java","PHP","Go","Ruby"]

# new_language_list = [lang for lang in languages if "o" in lang]
# new_language_list = [lang for lang in languages if lang.lower() != "python"]
# new_language_list = ["C++" if lang == "Python" else lang for lang in languages]
# new_language_list = [lang if lang != "Python" else "Assembly" for lang in languages]
new_language_list = [lang for lang in languages for char in "aeiou"]
# print(new_language_list)



# ------------------------------------------------------------------------------------------



# output the item which has no vowels from the list


# languages = ["JavaScript","Python","Java","PHP","Go","Ruby"]
# vowels = "aeiou"

# for lang in languages:
#     has_vowel = False
    
#     for char in vowels:
#         if char in lang.lower():
#             has_vowel = True
#             break # Exit the inner loop once a vowel is found
        
#     if not has_vowel:
#         print(lang)


# ===============================================================================


# count the number of vowels in each item in list 

# languages = ["JavaScript","Python","Java","PHP", "C++", "SQL", "Go","Ruby"]
# vowels = "aeiou"

# count_list = {}

# for lang in languages:
#     count_list[lang] = 0
    
#     for char in lang:
#         if char in vowels:
#             count_list[lang] += 1
            
# print(count_list)


# ===============================================================================


# name = "Okkar Aung"
# vowels = "aeiou"
# count = 0              
# for char in name:
#     if char.lower() in vowels:
#         count += 1
# print(count)



# ---------------------------------------------------------------------------------------------



# *** sorting 

sort_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# sort_list = [34, 5, 78, 12, 90]

# sort_list.sort()
# sort_list.sort(reverse = True)

# sort_list = [100, 50, 65, 82, 23]
# sort_list.sort(reverse = True)

# print(sort_list)


# *** Customize Sort Function ***  Argument => key = function

def close_to_50(n):
    return abs(n - 50)

# sort_arr = [100, 50, 65, 82, 23, 12]

# sort_arr.sort(key = close_to_50)

# print(sort_arr)

 # *** case-sensitive  
 
sort_list1 = ["banana", "Orange", "Kiwi","Apple", "cherry"]
# sort_list1.sort()
# sort_list1.sort(key=str.lower)

# print(sort_list1)


names = ["Alice", "BOB", "Charlie"]

# lowercase_names = [name.lower() for name in names]
# lowercase_names = list(map(str.lower, names))

# print(lowercase_names)


# reverse the order of a list, regardless of the alphabet

sort_list1.reverse()
# print(sort_list1)


# ============================================================================================



# ******** copy list


ori_list = ["banana", "Orange", "Kiwi","Apple", "cherry"]

# copy_list = ori_list.copy()
# copy_list = list(ori_list)
copy_list = ori_list[:]

# print(copy_list is ori_list)
# print(copy_list)


# ****** join list 


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list3 = list1 + list2

# for x in list2:
#     list1.append(x)
    
# list1.extend(list2)

list3 = list1[:] + list2[:]

# print(list3)


# [:] creates a shallow copy of the entire list by including all elements.
# [::] also creates a shallow copy of the entire list, with the default step being 1.


list_ori = [1, 2, 3, 4, 5]

copy1 = list_ori[:]
copy2 = list_ori[::]

# print(copy1)  # Output: [1, 2, 3, 4, 5]
# print(copy2)  # Output: [1, 2, 3, 4, 5]



#  *****  list methods  ******

# append()     =>    Adds an element at the end of the list
# clear()      =>    Removes all the elements from the list
# copy()       =>    Returns a copy of the list
# count()      =>    Returns the number of elements with the specified value

# extend()     =>    Add the elements of a list (or any iterable), to the end of the current list
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# index()      =>    Returns the index of the first element with the specified value
# insert()     =>    Adds an element at the specified position
# pop()        =>    Removes the element at the specified position
# remove()     =>    Removes the item with the specified value
# reverse()    =>    Reverses the order of the list
# sort()       =>    Sorts the list



fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# print(fruits)


a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

# print(a[3][2])

# fruits.clear()
# print(fruits)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1, 9]
x = points.count(9)
# print(x)


fruits = ['grape', 'apple', 'Cherry', 'banana', 'Peach']
cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)
# list.extend(iterable)

points = (1, 4, 2, 9, 7, 8, 9, 3, 1, 9)
# points[0] = 100

# fruits.extend(points)

# y = fruits.index("cherry")
# print(y)

# fruits.insert(1, "grape")

# fruits.pop(3)

# fruits.remove("cherry")

# fruits.append(points)
# for x in points:
#     fruits.append(x)
# fruits.extend(points)
    
# fruits.reverse()

# fruits.sort(reverse=True)
# fruits.sort() # case sensitive
# fruits.sort(key=str.lower)

# print(fruits)


num_list = [50, 40, 23, 19, 100, 68, 72]
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def nearest_to_50(n):
    return abs(n - 50)

def show_length(n):
    return len(n)
    
# num_list.sort(key=nearest_to_50)

# cars.sort(key=show_length)


cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def sort_year(e):
    return e["year"]

# cars.sort(key=sort_year)
# cars.sort(key=sort_year, reverse=True)

print(cars)



