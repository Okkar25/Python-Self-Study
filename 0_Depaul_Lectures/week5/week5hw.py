def doubleVowel(str):
    vowels = "aeiouAEIOU"

    for i in range(len(str) - 1):
        if str[i] in vowels and str[i + 1] in vowels:
            return True
    return False


# ---------------------------------------------------------------------------------------------


def numPairs(target_num, list):
    pairs = []

    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i] + list[j] == target_num:
                pairs.append((list[i], list[j]))

    return len(pairs) // 2


# --------------------------------------------------------------------------------------------


def hideShow(input_str, masking_seq):
    result_str = ""

    for i in range(len(input_str)):
        for j in range(len(masking_seq)):
            if i == j and masking_seq[j] == str(1):
                result_str += input_str[i]
            elif i == j and masking_seq[j] == "0":
                result_str += "#"

    return result_str


# ---------------------------------------------------------------------------------------------


# def clean(input_str):
#     strip_str_index = []

#     for i in range(len(input_str)):
#         if input_str[i] != " " and input_str[i] != "\n" and input_str[i] != "\t":
#             strip_str_index.append(i)

#     # strip_str = str[strip_str_index[0] : strip_str_index[len(strip_str_index) - 1] + 1]
#     # strip_str = str[strip_str_index[0]:strip_str_index[-1]]
#     strip_str = input_str[strip_str_index[0] : strip_str_index[-1] + 1]
#     return strip_str


# ============================================================================================


# def clean(input_str):
#     strip_str_index = []

#     for i in range(len(input_str)):
#         # if input_str[i] not in [" ", "\n", "\t"]:
#         if input_str[i] not in (" ", "\n", "\t"):
#             strip_str_index.append(i)

#     strip_str = input_str[strip_str_index[0] : strip_str_index[-1] + 1]
#     return strip_str


# ============================================================================================


# def clean(s):
#     # Remove leading spaces
#     start = 0
#     while start < len(s) and s[start] in (' ', '\n', '\t'):
#         start += 1

#     # Remove trailing spaces
#     end = len(s) - 1
#     while end >= 0 and s[end] in (' ', '\n', '\t'):
#         end -= 1

#     # Return the cleaned string by slicing
#     return s[start:end+1] if start <= end else ''


# ============================================================================================


def clean(s):
    # Remove leading spaces
    start = 0
    while s[start] in (' ', '\n', '\t'):
        start += 1

    # Remove trailing spaces
    end = len(s) - 1
    while s[end] in (' ', '\n', '\t'):
        end -= 1

    # Return the cleaned string by slicing
    return s[start:end+1] 


# ---------------------------------------------------------------------------------------------


def sequence(num):

    seq = [num]

    while num > 1:
        if num % 2 == 0:
            num = num // 2
            seq.append(num)
        elif num % 2 == 1:
            num = num + 1
            seq.append(num)

    for digit in seq:
        print(digit)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile("week5hwTEST.py"))
