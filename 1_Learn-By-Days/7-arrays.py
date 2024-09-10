# Python does not have built-in support for Arrays, but Python Lists can be used instead.

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

cars = ["Ford", "Volvo", "BMW"]

# An array can hold many values under a single name, and you can access the values by referring to an index number.


# *** Access the Elements of an Array

# x = cars[0]
# cars[0] = "Toyota"


# * The length of an array is always one more than the highest array index.


# for x in cars:
#   print(x)

# Adding Array Elements
cars.append("Honda")

# Removing Array Elements
# cars.pop(1)
# cars.remove("Volvo")


# * Array Methods

# append()   	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()    	Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()   	Adds an element at the specified position
# pop()     	Removes the element at the specified position
# remove()  	Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list


fruits = [ 'banana', 'cherry','apple']

# cars.extend(fruits)
# print(cars)

# fruits.insert(1, "orange")

# fruits.reverse()

# fruits.sort()
# print(fruits)

x = sorted(fruits)
x = sorted(fruits, key=lambda x : x[len(x) - 1])
# print(x)


