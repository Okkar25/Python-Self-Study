# lambda

# print((lambda x, y: x + y)(20, 30))


def func_builder(x):
    return lambda num: num + x


add_ten = func_builder(10)
add_twenty = func_builder(20)

# print(add_ten(20), add_twenty(20))

num = [10, 20, 30, 40, 50]

add_five = list(map(lambda x: x + 5, num))
# print(add_five)

person = {"name": "Okkar Aung", "age": 23, "RS": False, "graduated": False}

# for key in person.items():
# print(f"{key[0]} : {key[1]}")
# print(key)

# for key, value in person.items():
#     print(f"{key} : {value}")

# new_person = dict(
#     map(
#         lambda item: (item[0], 50) if item[0] == "age" else item,
#         person.items(),
#     )
# )

# new_person = dict(
#     map(
#         lambda item: (item[0], True) if item[0] == "graduated" else item,
#         person.items(),
#     )
# )
# print(new_person)

new_person = map(
    lambda item: "my_name" if item == "name" else item,
    person.keys(),
)
# for x in new_person:
#     print(x)

new_person = list(
    map(
        lambda item: "my_name" if item == "name" else item,
        person.keys(),
    )
)
# print(new_person)


num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# even_num = [num for num in num_list if num % 20 == 0]

# even_num = list(
#     filter(lambda x: x != "X", map(lambda x: x if x % 20 == 0 else "X", num_list))
# )

# even_num = list(
#     filter(lambda x: x % 20 == 0 , num_list)
# )

even_num = list(map(lambda x: x if x % 20 == 0 else "X", num_list))


even_num = list(filter(lambda x: x % 30 == 0, num_list))

even_num = list(map(lambda x: "Here" if x % 50 == 0 else x, num_list))

num_seventy = [num for num in num_list if num == 70]
# print(num_seventy)


num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(max(num_list))

max_num = 0
# for i in range(len(num_list) - 1):
#     if num_list[i + 1] > num_list[i]:
#         max_num = num_list[i + 1]

for i in range(1, len(num_list)):
    if num_list[i] > num_list[i - 1]:
        max_num = num_list[i]

# print(max_num)

import functools

# sum_num = functools.reduce(lambda x, y: x + y, num_list)
max_num1 = functools.reduce(lambda x, y: x if x > y else y, num_list)

# print(max_num1)
import operator

sum_num = functools.reduce(operator.add, num_list)
# print(sum_num)

# accumulate()

import itertools

accumulator = list(itertools.accumulate(num_list, lambda x, y: x + y))
# print(accumulator)

from functools import reduce

sum_total = reduce(lambda x, y: x + y, num_list, 50)

sum_total = sum(num_list, 50)
# print(sum_total)


# * sum, max => built-in , customized func , reduce

str_list = ["Okkar Aung", "John Wick", "Jason Bourne", "Sarah Conner"]

# error if there is no zero initial value
char_count = reduce(lambda x, y: x + len(y), str_list, 0)  # accumulator / current
# print(char_count)
