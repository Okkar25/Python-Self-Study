class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        self.strs = strs

        if not self.strs:
            return ""

        prefix = self.strs[0]

        for string in self.strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix


solution = Solution()
longest_common_prefix = solution.longestCommonPrefix(["flow", "flower", "flight"])
# print(longest_common_prefix)


# print("flower".startswith("flow"))


# ---------------------------------------------------------------------------------------------------


coordinate_map = {(1, 2): "Point A", (3, 4): "Point B", (5, 6): "Point C"}

# Accessing values using tuple keys
# print(coordinate_map[(1, 2)])  # Output: "Point A"
# print(coordinate_map[(5, 6)])  # Output: "Point C"


# Tuple (first_name, last_name) as dictionary keys
people_ages = {("John", "Doe"): 29, ("Jane", "Smith"): 34, ("Alice", "Johnson"): 25}

# Accessing data using tuple keys
# print(people_ages[("John", "Doe")])  # Output: 29
# print(people_ages[("Jane", "Smith")])  # Output: 34


# Tuple (product_id, store_id) as dictionary keys
product_prices = {
    (101, 1): 9.99,  # product_id 101 in store 1
    (101, 2): 10.99,  # product_id 101 in store 2
    (202, 1): 15.49,  # product_id 202 in store 1
}

# Accessing price using composite key
# print(product_prices[(101, 1)])  # Output: 9.99
# print(product_prices[(202, 1)])  # Output: 15.49


x, y, z = 1, 2, 3

# print(x)  # Output: 1
# print(y)  # Output: 2
# print(z)  # Output: 3


coordinates = (10, 20, 30)

x, y, z = coordinates

# print(x)  # Output: 10
# print(y)  # Output: 20
# print(z)  # Output: 30


# unpacking
a = 5
b = 10

a, b = b, a  # Swaps the values of a and b

# print(a)  # Output: 10
# print(b)  # Output: 5


# Partial unpacking
x, *y, z = 1, 2, 3, 4, 5

# print(x)  # Output: 1
# print(y)  # Output: [2, 3, 4]
# print(z)  # Output: 5


# Unpacking nested tuples

person = ("Alice", (30, "Engineer"))

name, (age, job) = person

# print(name)  # Output: Alice
# print(age)  # Output: 30
# print(job)  # Output: Engineer


# tuple unpacking or tuple assignment
# even though you don't see the parentheses, Python implicitly handles this as a tuple
# When you write x, y = y, x, Python first creates a tuple of the values on the right-hand side (y, x). This is called tuple packing
x, y = y, x


# List comprehensions

# [expression for item in iterable if condition]
# a one line accumulator

squares = []
for i in range(11):
    squares.append(i * i)

[i * i for i in range(11)]

[i * i for i in range(11) if i % 3 != 0]

# for p1 in "RPS":
#     for p2 in "RPS":
#         print(p1, p2)

x = [(p1, p2) for p1 in "RPS" for p2 in "RPS"]
# print(x)


(i * i for i in range(11))
[i * i for i in range(11)]

# for i in (i * i for i in range(11)):
#     print(i)

y = list((i * i for i in range(11)))
# print(y)


# Filter Words Starting with a Vowel
words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowel_words = [word for word in words if word[0].lower() in "aeiou"]
# print(vowel_words)

# Given a 2D matrix (a list of lists), flatten it into a 1D list using list comprehension.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [item for row in matrix for item in row]
# print(flatten)


# Create a list of the lengths of each word in a given list of words.

words = ["hello", "world", "python", "list", "comprehension"]
word_lengths = [len(word) for word in words]
# print(word_lengths)


# Given a list of strings, create a new list where each string is reversed.
words = ["hello", "world", "python", "list"]

reversed_words = [word[::-1] for word in words]
# print(reversed_words)


#  Given a string with both letters and numbers, extract the digits into a list using list comprehension.
string = "a1b2c3d4e5"
digits = [int(char) for char in string if char.isdigit()]
# print(digits)


# Given two lists, generate their Cartesian product (all combinations of elements from both lists).

list1 = [1, 2, 3]
list2 = ["a", "b"]
cartesian_product = [(num, char) for num in list1 for char in list2]
# print(cartesian_product)


primes = [x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
# print(primes)


# * random


import random

# print(random.randint(10, 20))
# print(random.randrange(11))
# print(random.randrange(1, 21, 2))

fruits = ["apple", "banana", "cherry", "date"]
# print(random.choice(fruits))
# print(random.choices(fruits, k=2)) # allow duplicates

# Set the seed
# random.seed(20)

# Generate random numbers
# print(random.randint(1, 100))  # Always prints the same number with the same seed
# print(random.randint(1, 100))  # Will also print the same number with the same seed

# Random float between 10 and 20
random_float = random.uniform(10, 20)
# print(random_float)


my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # modify the original list
# print(my_list)

# sample / choices => new list
# sample => no duplicate / cannot exceed size
# choices => allow duplicates / can exceed size

# sampled_list = random.sample(my_list, 3)
sampled_list = random.choices(my_list, k=6)
# print(sampled_list)

# print([random.randint(0,3) for i in range(10) ])
# print([random.randint(1, 7) for i in range(10)])


# print([random.uniform(1, 5) for i in range(10)])

# print( random.choice( [1,'apple',3]))

# print(random.choices([1, 2, 3, 4, 5], k=3))
# print(random.choices([1, 2, 3, 4, 5]))
# print(random.choices("RPS"))
# print([ random.choice("HT") for i in range(20)])


# print(random.sample(range(10), 3))
# print(random.choices(range(10), k=3))

lst = list(range(10))
random.shuffle(lst)
# print(lst)

# TypeError: 'str' object does not support item assignment
# shuffle => can only be used on list (mutable)
# random.shuffle( 'abc' )
# random.shuffle((1, 2, 3))

# print([ random.choice("HT") for i in range(20)])

# seeding allows you to repeat
# random.seed(1)
# print([ random.choice("HT") for i in range(20)])


# random/dict examples


# import random

# def diceTotal():
#     pips = 0

#     die1 = random.randrange(1,7)
#     die2 = random.randrange(1,7)
#     pips += die1 + die2
#     print( die1, die2)

#     while die1==die2:
#         die1 = random.randrange(1,7)
#         die2 = random.randrange(1,7)
#         pips += die1 + die2
#         #print( die1, die2)
#     return pips


import random


def diceTotal():
    total_pips = 0

    while True:
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Add the pips from the two dice
        total_pips += die1 + die2
        print(f"Rolled: {die1}, {die2}")

        # Check if it's a double
        if die1 != die2:
            break  # If not a double, stop rolling

    return total_pips


# Example usage
# result = diceTotal()
# print(f"Total number of pips: {result}")

# print([diceTotal() for i in range(10)])


# Loop and a half pattern


def sumUserNums():
    total = 0
    ans = input("Enter a number: ")  # half
    while ans != "":
        total += eval(ans)
        # ans is either a '##' or ''
        ans = input("Enter a number: ")
    return total


# Infinite loop pattern


def sumUserNums():
    total = 0
    while True:
        # ans is either a '##' or ''
        ans = input("Enter a number: ")
        if ans == "":
            break  # stop the loop
        else:  # '##'
            total += eval(ans)
    return total


# games = [diceTotal() for i in range(50)]
# print(games)

# from Dictionaries import frequency
from collections import Counter

# print(games)
# print(Counter(games))
# print(dict(Counter(games)))


# games = [diceTotal() for i in range(50)]
# count_games = Counter(games)

# print(dict(count_games))

# sorted_games = dict(sorted(count_games.items()))
# print(sorted_games)


names = ["Zhask", "John", "Sarah"]
phones = [111, 222, 333]

data = zip(names, phones)
# print(dict(data))
# print(list(data))
# print(dict(list(data)))


# Korea Problem

items = {"Cola": 3, "Pepsi": 5, "Bubble Tea": 2}
continue_adding = True
secret_word = "Skywalker"
print("Initial Items : ", items)


def AddInventory(dict, name, num):
    if name in dict:
        dict[name] += num
        print(items)
    else:
        dict[name] = num
        print(items)


while continue_adding:
    item_name = input("Enter your item : ")

    if item_name == secret_word:
        print("Your updated items is : ", items)
        break

    item_qty = int(input("Enter item quantity : "))
    AddInventory(items, item_name, item_qty)
else:
    print(items)


# * encode

# >>> d = {'a':'k', 'b':'g'}
# >>> encode( 'bat', d )
# 'gkt'

d = {"a": "k", "b": "g"}


def encode(str, d):
    encoded_str = ""

    for char in str:
        if char in d:
            encoded_str += d[char]
        else:
            encoded_str += char
    # print(str)
    return encoded_str


# print(encode("bat", d))


# * substitution cipher

alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffle_alpha = list(alphabet)
random.shuffle(shuffle_alpha)
# print(shuffle_alpha)

alphabet = list(alphabet)

alphabet_pairs = list(zip(alphabet, shuffle_alpha))
alphabet_pairs = dict(zip(alphabet, shuffle_alpha))
# print(alphabet_pairs)

# print(encode("the quick red fox jumped over the lazy brown dog", alphabet_pairs))


# * decode


def encode(str, d):
    encoded_str = ""

    for char in str:
        if char in d:
            encoded_str += d[char]
        else:
            encoded_str += char
    # print(str)
    return encoded_str


msg = """
>>> aitmjx xwan
Xwl Flc mo Texwmc, qe Xai Tlxljn
Qlksxaosu an qlxxlj xwkc srue.
Lztuayax an qlxxlj xwkc aituayax.
Naitul an qlxxlj xwkc ymitulz.
Ymitulz an qlxxlj xwkc ymituaykxlh.
Oukx an qlxxlj xwkc clnxlh.
Ntkjnl an qlxxlj xwkc hlcnl.
Jlkhkqauaxe ymscxn.
Ntlyaku yknln kjlc'x ntlyaku lcmsrw xm qjlkb xwl jsuln.
Kuxwmsrw tjkyxaykuaxe qlkxn tsjaxe.
Ljjmjn nwmsuh cldlj tknn naulcxue.
Sculnn lztuayaxue naulcylh.
Ac xwl okyl mo kiqarsaxe, jlosnl xwl xlitxkxamc xm rslnn.
Xwljl nwmsuh ql mcl-- kch tjloljkque mcue mcl --mqdamsn vke xm hm ax.
Kuxwmsrw xwkx vke ike cmx ql mqdamsn kx oajnx sculnn ems'jl Hsxyw.
Cmv an qlxxlj xwkc cldlj.
Kuxwmsrw cldlj an moxlc qlxxlj xwkc *jarwx* cmv.
Ao xwl aitulilcxkxamc an wkjh xm lztukac, ax'n k qkh ahlk.
Ao xwl aitulilcxkxamc an lkne xm lztukac, ax ike ql k rmmh ahlk.
Ckilntkyln kjl mcl wmcbacr rjlkx ahlk -- ulx'n hm imjl mo xwmnl! """

code = {"O": "f"}

msg = msg.lower()
print(encode(msg, code))

# msg is written in English, certain letters are more frequent. We can use our previous work to compute
# frequencies:

# from Dictionaries import frequencies # or from ... import frequencies
# frequencies( msg )

# {'\n': 23, '>': 3, ' ': 126, 'A': 55, 'I': 17, 'T': 23, 'M': 44, 'J': 34, 'X': 81,
# 'W': 32, 'N': 47, 'L': 92, 'F': 1, 'C': 42, 'O': 12, 'E': 17, ',': 4, 'Q': 21, 'K':
# 53, 'S': 21, 'U': 33, 'R': 11, '.': 18, 'Z': 6, 'Y': 17, 'H': 17, "'": 4, 'B': 2,
# 'D': 5, '-': 6, 'V': 4, '*': 2, '!': 1}


