# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst

#     # Split the list into two halves
#     mid = len(lst) // 2
#     left_half = merge_sort(lst[:mid])
#     right_half = merge_sort(lst[mid:])

#     # Merge the sorted halves
#     return merge(left_half, right_half)

# def merge(left, right):
#     sorted_list = []
#     i = j = 0

#     # Merge two sorted halves
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_list.append(left[i])
#             i += 1
#         else:
#             sorted_list.append(right[j])
#             j += 1

#     # Append remaining elements
#     sorted_list.extend(left[i:])
#     sorted_list.extend(right[j:])

#     return sorted_list

# # Example usage:
# seq1 = [3, 1, 4, 1]
# seq2 = [5, 9, 2, 6]

# sorted_seq1 = merge_sort(seq1)
# sorted_seq2 = merge_sort(seq2)

# result = merge(sorted_seq1, sorted_seq2)
# print(result)


# ======================================================================================


# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         # Track if any swaps are made in this pass
#         swapped = False
#         # Traverse through the list, stopping earlier each pass
#         for j in range(0, n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 # Swap if the current element is greater than the next
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swapped = True
#         # If no swaps occurred in this pass, the list is sorted
#         if not swapped:
#             break
#     return lst


# ======================================================================================


def interleaved(seq1, seq2):
    result = []
    i, j = 0, 0

    # Traverse both sequences until one of them is exhausted
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            result.append(seq2[j])
            j += 1

    # Append remaining elements (if any) from seq1
    # while i < len(seq1):
    #     result.append(seq1[i])
    #     i += 1

    # Append remaining elements (if any) from seq2
    # while j < len(seq2):
    #     result.append(seq2[j])
    #     j += 1

    # second method
    result.extend(seq1[i:])
    result.extend(seq2[j:])

    return result


# print(interleaved([-7, -2, -1], [-4, 0, 4, 8]))


# --------------------------------------------------------------------------------------


def primeFac(n):
    factors = []

    # Start with 2, the smallest prime number
    divisor = 2

    while n > 1:
        # If n is divisible by the current divisor, it's a factor
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

        # Move to the next possible divisor
        divisor += 1

    return factors


# --------------------------------------------------------------------------------------


def piggyBank(list):
    currency = {"Q": 0, "D": 0, "N": 0, "P": 0}
    total = 0

    for value in list:
        if value not in currency:
            currency[value] = 1
        else:
            currency[value] += 1

    for value in list:
        if value == "Q":
            total += 25
        elif value == "D":
            total += 10
        elif value == "N":
            total += 5
        else:
            total += 1

    return (currency, total)


# print(piggyBank(["D", "P", "Q", "Q", "D", "P", "P"]))


# --------------------------------------------------------------------------------------


import random

# random.seed(1)


def roll_dice():
    first_die_num = random.randint(1, 6)
    second_die_num = random.randint(1, 6)

    return first_die_num + second_die_num


def craps():

    initial_roll = roll_dice()
    # print(initial_roll)

    if initial_roll in [7, 11]:
        return 1  # player wins
    elif initial_roll in [2, 3, 12]:
        return 0  # player loses

    while True:
        next_roll = roll_dice()

        if next_roll == initial_roll:
            return 1  # player wins
        elif next_roll == 7:
            return 0  # player loses


# print(craps())


# --------------------------------------------------------------------------------------


# random.seed(0)

def testCraps(n):
    result = [craps() for i in range(n)]
    times_of_winning = result.count(1)

    return times_of_winning / n


# print([(i,random.seed(i),testCraps(100*i)) for i in range(1,10)])


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("hw6TEST.py"))
