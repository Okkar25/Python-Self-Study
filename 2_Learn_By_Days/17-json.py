# Python JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate
# In Python, JSON is commonly used to represent data structures like dictionaries and lists in a format that can be transmitted or stored.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python Dict
# * in json => false / in dict => False

import json 

x = '{"name":"Okkar Aung", "age": 23, "RS": false, "occupation": "software developer"}'
# print(x, type(x))
js = json.loads(x)
# print(js, type(js))


# * Convert from Python to JSON

import json 

my_info = {"name":"Okkar Aung", "age": 23, "RS": False, "occupation": "software developer"}
to_json = json.dumps(my_info)
# print(to_json, type(to_json))


# * You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True)) # true
# print(json.dumps(False)) # false
# print(json.dumps(None)) # null


# * When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

import json 

py_dict = {
    "name": "Okkar Aung",
    "age": 23,
    "single": True,
    "married": False,
    "pets": None,
    "friends" : ("Saw Yadana", "Phone Myint Kyaw", "Na Na"),
    "phones": [
        {"model": "iPhone 11", "color": "black"},
        {"model": "iPhone SE", "color": "space grey"},
    ]
}

to_json = json.dumps(py_dict)
# print(to_json, type(to_json))

to_dict = json.loads(to_json)
# print(to_dict, type(to_dict))


# * Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

format_json = json.dumps(py_dict, indent=4)
# print(format_json)


# * separators

separate_json = json.dumps(py_dict, indent=4, separators=(". "," = "))
# print(separate_json)


# * Order the Result
# The json.dumps() method has parameters to order the keys in the result:


order_json = json.dumps(py_dict, indent=4, separators=(", "," = "), sort_keys=True)
# print(order_json)




