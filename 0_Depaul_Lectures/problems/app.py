#  5.27 Write function letter2number() that takes as input a letter grade (A, B, C, D, F,
#  possibly with a- or +) and returns the corresponding number grade. The numeric values
#  for A, B, C, D, and F are 4, 3, 2, 1, 0. A + increases the number grade value by 0.3 and a
# decreases it by 0.3.
#  >>> letter2number('A-')
#  3.7
#  >>> letter2number('B+')
#  3.3
#  >>> letter2number('D')
#  1.0


def letter2number(str):

    char = str[0]
    sign = str[1]
    total = 0

    char_values = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

    total += float(char_values.get(char, 0))

    if len(str) > 1:
        sign = str[1]

        if sign == "+":
            total += 0.3
        else:
            total -= 0.3

    return total


# print(letter2number("A-"))
# print(letter2number("B+"))
# print(letter2number("D"))


# 5.28 Write function geometric() that takes a list of integers as input and returns True if
#  the integers in the list form a geometric sequence. A sequence a0, a1, a2, a3, a4,...,an 2,
#  an 1 isageometric sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3,...,an 1/an 2 are
#  all equal.
#  >>> geometric([2, 4, 8, 16, 32, 64, 128, 256])
#  True
#  >>> geometric([2, 4, 6, 8])
#  False


def geometric(lst):
    
    # Calculate the common ratio
    ratio = lst[1] / lst[0]
    
    for i in range(len(lst) - 1):
        if lst[i + 1] / lst[i] != ratio:
            return False
    
    return True


print(geometric([2, 4, 8, 16, 32, 64, 128, 256])) 
print(geometric([2, 4, 6, 8]))                    
