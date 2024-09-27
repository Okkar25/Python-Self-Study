x = 20
y = 30
z = x + y

# print(vars())

# file = open("demofile.txt", "r")
# content = file.read()
# file.close()


# with open("demofile.txt", "r") as file:
#     content = file.read()
    # print(content)

# print(content)
# print(content.count("i"))
# print(content.lower().count("h"))


# with open("demofile.txt", "r") as file:
    # content = file.read()
    
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    
    # content = file.readlines()
    # print(content)
    # for line in content:
    #     print(line)


# file = open("demofile.txt", "w+")
# file.write(str(10000))
# file.write("This is testing1")

# file = open("demofile.txt", "r")
# file.seek(0,0)
# content = file.read()
# print(content)

# file.close()

# txt = open("demofile.txt").read()
# print(txt)


# def numChars1(filename):
#     file = open(filename, "r")
#     content = file.read()
#     file.close()
#     return len(content)

# def numChars2(filename):
#     return len(open(filename).read())

# def numChars3(filename):
#     with open(filename, "r") as file:
#         return len(file.read())

# print(numChars3('out.txt'))


# import csv 

# def load_data(filename):
#     data = []
    
#     with open(filename) as csvfile:
#         person_data = csv.reader(csvfile, delimiter=",")
#         next(person_data)
        
#         for row in person_data:
#             data.append(row)
        
#         return data
    
# new = load_data("data.csv")

# for row in new:
#     print(row)


# import csv 

# with open("names.csv", mode="w") as csvfile:
#     fieldnames = ["id", "name", "email"]
    
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow({"id":1, "name": "Okkar Aung", "email":"okkaraung2323@gmail.com"})
#     writer.writerow({"id":2, "name": "Alex Mason", "email":"alexmason6453@gmail.com"})
#     writer.writerow({"id":3, "name": "Bobby Hudson", "email":"bobbyhudson9821@gmail.com"})
    
    
# import csv 

# data = [
#     {"id":1, "name": "Okkar Aung", "email":"okkaraung2323@gmail.com"},
#     {"id":2, "name": "Alex Mason", "email":"alexmason6453@gmail.com"},
#     {"id":3, "name": "Bobby Hudson", "email":"bobbyhudson9821@gmail.com"}
# ]

# with open("employee.csv", mode="w") as csvfile:
#     fieldnames = data[0].keys()
    
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     # for row in data:
#     #     writer.writerow(row)
    
#     writer.writerows(data)
    

animal = 'Huskies'
# print(" ".join(animal.upper()) )


# list = ["apple", "banana", "mango", "peach", "apple", "orange", "mango"]

# duplicate = {}

# for fruit in list:
#     if fruit in duplicate:
#         duplicate[fruit] += 1
#     else:
#         duplicate[fruit] = 1

# for fruit in duplicate:
#     print(f"{fruit.upper()} {duplicate[fruit]}")

# for fruit in duplicate:
#     if duplicate[fruit] == 2:
#         print(fruit)
       
        
txt = "Hello! I am John. May I have a packet of chips, dipped in cheese ?"

for punctuation in "!.,?":
    txt = txt.replace(punctuation, "")

# handling errors 

# print(eval("pear"))
# print(eval("'pear'"))
# print(eval("'hello'"))

def f():
    x = 7
    ans = input("Enter an expression: ")
    print("Your expression is", eval(ans))
    
# f()


# 1. Using vars() with a class object
# When you use vars() on an instance of a class, it returns the instance's attributes in the form of a dictionary.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p = Person("Okkar", 23)

# print(p.__dict__)
# print(vars(p))


# 2. Using vars() without arguments
# If vars() is called without any arguments, it returns the local variables in the current scope.


x = 10
y = 20
z = x + y

# print(vars())

# 3. Modifying attributes using vars()
# Since vars() returns a mutable dictionary, you can modify object attributes using it.

# print(p.name)

vars(p)["name"] = "Novak"

# print(p.name)


# 4. Using vars() with modules
# You can also use vars() to inspect the attributes of a module.

import math
from pprint import pprint
# print(vars(math))
# print(dir(math))
# pprint(vars(math))

import calendar
yy = 2024
mm = 9
# print(calendar.month(yy,mm, 3, 1))
