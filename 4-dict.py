car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

person = {
   "name":"Okkar Aung",
   "age": 23,
   "age": 50, # overwrite 
   "RS": False,
}

# print(person)

# * key : value
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# * can be referred to by using the key nam

# print(person)
# print(len(person))

# * The values in dictionary items can be of any data type

car_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# ** dict constructor 

this_person = dict(name="John", age=23, country="United States")
# print(this_person)


# * Accessing Items

car_model = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(car_model["year"])

# * get() 

# print(car_model["year"])
# print(car_model.get("model"))

# * keys()

# print(car_model.keys())
# print(car_model.keys[2]) # error 
# print(car_model[car_model.keys[2]]) # error 

# * The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# keys_overview = car_model.keys()
# print("before change => ", keys_overview)

# car_model["color"] = "white"
# print("after change => ", keys_overview)


# * values()

car_model = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(car_model.values())

# values_overview = car_model.values()
# print("before change => ", values_overview)

# car_model["color"] = "white"
# print("after change  => ", values_overview)


# ***** items()

car_model = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(car_model.items())

# items_changes = car_model.items()
# print("before change => ", items_changes)

# car_model["year"] = 2020
# print("after change  => ", items_changes)


# * Check if Key Exists

# if "year" in car_model:
#     print("Yes, it exists")
# else:
#     print("Yes, it doesn't exist")


# * Change Values

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# this_dict["year"] = 2018


# * update()

# this_dict.update({"year": 2020})
# print(this_dict)


# * Adding Items

# this_dict["color"] = "red"

# this_dict.update({"factory":"Misubishi"})
# print(this_dict)


#  * Removing Items

# this_dict.pop("year")
# this_dict.popitem()

# del this_dict["model"]
# del this_dict
# this_dict.clear()

# print(this_dict)


# * Loop 

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "white"
}

# for item in this_dict:
#     print(item)
#     print(this_dict[item])


# for x in this_dict.keys():
#     print(x)
    
# for x in this_dict.values():
#     print(x)

# for x in this_dict.items():
#     print(x)


# * Copy a Dictionary

car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "white"
}

# my_dict = car_dict.copy()
# print(my_dict)

# my_dict = dict(car_dict)
# print(my_dict)


# * Nested Dict 

my_family = {
    "father": {
        "name": "Aung Aung",
         "age": 50,
         "occupation": "Seafarer"
    },
    "mother": {
        "name": "Aye Aye Thet",
         "age": 48,
         "occupation": "Clothes Maker"
    },
    "brother": {
        "name": "Thiha Aung",
         "age": 25,
         "occupation": "Office Employee"
    },
    "Me": {
        "name": "Okkar Aung",
         "age": 23,
         "occupation": "Web Developer"
    }
}

# print(my_family["Me"]["occupation"])

father = {
   "name": "Aung Aung",
   "age": 50,
   "occupation": "Seafarer"
}

mother = {
    "name": "Aye Aye Thet",
    "age": 48,
    "occupation": "Clothes Maker"
}

Me = {
    "name": "Okkar Aung",
    "age": 23,
    "occupation": "Web Developer"
}

my_family = {
    "father" : father,
    "mother": mother,
    "Me" : Me
}

# print(my_family["mother"]["occupation"])

my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# for x, obj in my_family.items():
#     # print(x, obj)
#     print(x)
    
#     for y in obj:
#         print(f"{y} : {obj[y]}")
        


# * Methods 

# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary



# keys = {"title","genre", "budget","director"}
# values = 0

# movie = dict.fromkeys(keys,values)
# print(movie)


# movie = {
#     "title" : "Mad Max",
#     "budget": "50M",
#     "director":"George Miller",
#     "rating": 7.5
# }

# movie.setdefault("rating", 8)
# print(movie)



# ---------------------------------------------------------------------------------------------



# Problem 1: Count Frequency of Words in a Sentence
# Problem:
# Given a sentence, count the frequency of each word using a dictionary.

# # Solution
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Example usage
sentence = "the cat in the hat the cat"
result = word_frequency(sentence)
# print(result)  # Output: {'the': 3, 'cat': 2, 'in': 1, 'hat': 1}


# --------------------------------------------------------------------------------------------


# Problem 2: Merge Two Dictionaries
# Problem:
# Given two dictionaries, merge them into one.

# Solution
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2} # **** merging dict 

# Example usage
dict1 = {'a': 1, 'b': 5}
dict2 = {'b': 3, 'c': 4}
result = merge_dictionaries(dict1, dict2)
# print(result)  # Output: {'a': 1, 'b': 3, 'c': 4}


# --------------------------------------------------------------------------------------------


# Problem 3: Check if a Key Exists in a Dictionary
# Problem:
# Given a dictionary and a key, check if the key exists in the dictionary.

# Solution
def check_key_exists(d, key):
    return key in d

# Example usage
d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
result = check_key_exists(d, key)
# print(result)  # Output: True


# --------------------------------------------------------------------------------------------


# Problem 4: Find the Maximum Value in a Dictionary
# Problem:
# Given a dictionary with numeric values, find the key with the highest value.

# Solution

# Example usage
d = {'a': 10, 'b': 50, 'c': 30}

result = max(d, key=d.get)
# print(result)  # Output: 'b'


# --------------------------------------------------------------------------------------------


# Problem 5: Invert a Dictionary (Swap Keys and Values)
# Problem:
# Given a dictionary, invert it so that keys become values and values become keys.

# Solution
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Example usage
d = {'a': 1, 'b': 2, 'c': 3}
result = invert_dictionary(d)
# print(result)  # Output: {1: 'a', 2: 'b', 3: 'c'}


# --------------------------------------------------------------------------------------------


# Problem 6: Remove a Key from a Dictionary using del keyword
# Problem:
# Remove a key from a dictionary if it exists.


# Solution
def remove_key(d, key):
    if key in d:
        del d[key]
    return d

# Example usage
d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
result = remove_key(d, key)
# print(result)  # Output: {'a': 1, 'c': 3}



# --------------------------------------------------------------------------------------------



# Problem 7: Count Occurrences of Characters in a String
# Problem:
# Given a string, count how many times each character appears using a dictionary.


str = "hello world"
# words = str.split(" ")
# joined_str = "".join(words)
joined_str = str.replace(" ", "")

char_occurrence = {}

for char in joined_str:
    if char in char_occurrence:
        char_occurrence[char] += 1
    else:
        char_occurrence[char] = 1

# print(char_occurrence)



# --------------------------------------------------------------------------------------------



# Problem 8: Filter Dictionary by Values
# Problem:
# Given a dictionary with numeric values, return a new dictionary containing only the entries with values greater than a given threshold.


d = {'a': 10, 'b': 5, 'c': 20}
threshold = 10

greater_than_10 = {k:v for k,v in d.items() if v > 10}
# print(greater_than_10)



# --------------------------------------------------------------------------------------------



# Problem 10: Sort a Dictionary by Its Values
# Problem:
# Given a dictionary, sort it by its values in ascending order and return the sorted dictionary.


d = {'a': 3, 'b': 1, 'c': 2}
result = dict(sorted(d.items(), key=lambda item: item[1]))

# print(dict(d.items()))
# print(d.items())
# print(result)