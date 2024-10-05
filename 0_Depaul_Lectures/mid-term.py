# Problem 1 : numCapitalized

# Write a function numCapitalized that accepts a sentence consisting of words and spaces (no
# punctuation) and returns the number of words in the sentence that are capitalized.
# Note that this is NOT the total number of capitals in the string. Sample usage:


def numCapitalized(sentence):
    word_list = sentence.split(" ")
    count = 0

    for word in word_list:
        if word[0].isupper():
            count += 1

    return count


# print(numCapitalized('This sentence has one such'))
# print(numCapitalized('This sentence has ONE more'))
# print( numCapitalized('ALL THESE ARE'))
# print( numCapitalized('ALL THESE ARE')==3)


# -----------------------------------------------------------------------------------------


# PRoblem 2 : gct

# Implement a function gct according to these guidelines:
# The function accepts a single positive integer which represents a number of tablespoons of a
# liquid.
# You may assume that this number is always between 0 and 25599 (inclusive of both).
# The function returns a formatted str containing an equivalent number of gallons, cups and
# tablespoons. The answer should use as many gallons, then cups as possible. For example
# gct(312) would return '01g,03c,08t' as 312 tablespoons is equivalent to 1 gallon, 3 cups,
# and 8 tablespoons.
# Each of the output quantities (gallons, cups, tablespoons) should occupy two digits.
# If the values have less than two digits, they should be padded with leading zeroes. I.e., 2
# cups is represented by '02c' .
# If you look things up, cite them (same goes for all problems)

# * 1 gallon = 16 cups
# * 1 cup = 16 tablespoons


def gct(t):
    # conversion factors
    # 1 gallon = 16 cups
    # 1 cup = 16 tablespoons

    tablespoons_per_gallon = 256
    tablespoons_per_cup = 16

    # calculate the number of gallons
    gallons = t // tablespoons_per_gallon
    tablespoons_remaining = t % tablespoons_per_gallon

    # calculate the number of cups
    cups = tablespoons_remaining // tablespoons_per_cup
    tablespoons_remaining = tablespoons_remaining % tablespoons_per_cup

    tablespoons = tablespoons_remaining

    # return f"{gallons:02}g, {cups:02}c, {tablespoons:02}t"

    result = "{:02}g, {:02}c, {:02}t"
    # return result.format(gallons, cups, tablespoons)

    return (
        f"{str(gallons).zfill(2)}g, {str(cups).zfill(2)}c, {str(tablespoons).zfill(2)}t"
    )


# print(gct(312))
# print(gct(777))
# print(gct(25599))
# print(gct(25599) == '99g, 15c, 15t')


# ---------------------------------------------------------------------------------------------


def priceTShirt(size, slogan):
    # S => 12 / M => 15 / L => 18 ( dollar )
    # lower => 25 / upper => 30 / punctuation => 20 / " " \n => 0 ( cents )
    total = 0

    if size == "S":
        total += 12
    elif size == "M":
        total += 15
    else:
        total += 18

    slogan_list = slogan.split(" ")

    for word in slogan_list:
        for char in word:
            if char in ".,!'\"?:":
                total += 0.2
            elif char.isupper():
                total += 0.3
            elif char.islower():
                total += 0.25
            # elif char == "\n" or char == " ":
            #     total += 0

    return total


def priceTShirt(size, slogan):
    base_prices = {"S": 12, "M": 15, "L": 18}

    price = base_prices.get(size, 0)

    for char in slogan:
        if char.isupper():
            price += 0.30
        elif char.islower():
            price += 0.25
        elif char in ".,!'\"?:":
            price += 0.20

    # price = f"{price:.2f}"
    # return float(price)

    return round(price, 2)


# print(priceTShirt('S',"Vote!"))
# print(priceTShirt('L',"Madam, \nI'm Adam"))
# print(priceTShirt('L',"Taco cat!"))
# print(priceTShirt("M","A man, a plan, a canal: Panama."))
# print(priceTShirt("M","   \n\n\n   ") == 15 )


# ---------------------------------------------------------------------------------------------


# * alterCase


def alterCase(str):
    result = ""

    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i].upper()
        else:
            result += str[i].lower()

    return result


# print(alterCase('apple'))
# print(alterCase('ABRACADABRA'))
# print(alterCase('Mississippi'))
# print(alterCase('apPLE'))
# print(alterCase('apPLE')=='ApPlE')


# ---------------------------------------------------------------------------------------------


# * piggyBank (25 points)

# Implement a function piggyBank that represents a piggy bank and determines its value. Details:
# accepts a single argument, a list of coins.
# 'Q','D','N','P' are the valid values for coins and represent quarter, dime, nickel and
# penny, respectively. Each should be valued at their standard US value in whole cents.
# (Assume they will be supplied in upper case.)
# any other value, for example the the Canadian Quarter 'CQ' , should be accepted, but
# should not add to the value of the bank
# the value of the bank should be returned in whole cents

# 1 Quarter = 25 cents
# 1 Dime = 10 cents
# 1 Nickel = 5 cents
# 1 Penny = 1 cent


def piggyBank(coins):
    currency = {"Q": 25, "D": 10, "N": 5, "P": 1}

    total_cents = 0

    for coin in coins:
        if coin == "Q":
            total_cents += currency[coin]
        elif coin == "D":
            total_cents += currency[coin]
        elif coin == "N":
            total_cents += currency[coin]
        elif coin == "P":
            total_cents += currency[coin]
        else:
            total_cents += 0

    return total_cents


# print(piggyBank(['Q','D','P'] ))
# print(piggyBank(['D', 'P', 'P', 'N', 'D', 'D', 'Q']))
# print(piggyBank(['D', 'P', 'P', 'N', 'D', 'D', 'CQ']))
# print(piggyBank(['D', 'X', 'P', 'R', 'D', 'D', 'CQ']))
# print(piggyBank( ['D', 'P', 'P', 'N', 'D', 'D', 'CQ']) == 37)


# ---------------------------------------------------------------------------------------------


# * odds (25 points)

# Write a function odds that returns the odd numbers contained in a 2-dimensional list of
# numbers. Details:
# accepts a single argument, a 2-dimensional list of positive integers
# returns a (1-dimensional) list containing the odd numbers from the input list


def odds(TwoDlist):
    odd_list = []

    for list in TwoDlist:
        for num in list:
            if num % 2 == 1:
                odd_list.append(num)
    return odd_list


# print(odds( [[1,2,3],[4,5,6]] ))
# print(odds( [[1,2,3],[4,5,6], [12,14], [13,15]] ))
# print(odds( [[1,2,3],[4,5,6], [3,5], [13,15]] ))
# print(odds( [ [2,4],[4,6,10] ] ))
# print(odds( [[1,2,3],[4,5,6], [12,14], [13,15]] ) == [1, 3, 5, 13, 15])


# --------------------------------------------------------------------------------------------


# * findWordOfLength (25 points)

# Write a function findWordOfLength that locates the first word in a sentence that has the given
# length. Details:
# accepts two arguments:
# 1. the desired word length
# 2. a sentence ( str )
# returns the location (index) of the first word in the sentence that has the desired length
# for this problem, the first word has location/index 0, the second index 1, and so forth ...
# (Python style counting/indexing)
# the punctuation characters ".,;!?" should not be included in any word's length
# -1 is returned if no word of the desired length is found


def findWordOfLength(length, sentence):
    # str = ""
    # for char in sentence:
    #     if char not in ".,;!?":
    #         str += char

    for punctuation in ".,;!?":
        sentence = sentence.replace(punctuation, "")

    word_list = sentence.split(" ")

    for i in range(len(word_list)):
        if len(word_list[i]) == length:
            return i

    return -1


# print(findWordOfLength(4,"Able was I ere I saw Elba."))
# print( findWordOfLength(1,"Able was I ere I saw Elba."))
# print(findWordOfLength(6,"Able was I, ere I saw Elba."))
# print(findWordOfLength(7,"Hey Anna, would you prefer to ride in a kayak or a racecar?"))
# print(findWordOfLength(8,"Hey Anna, would you prefer to ride in a kayak or a racecar?"))
# print(findWordOfLength(4,"What???!!!"))
# print(findWordOfLength(5,"Hey Anna, would you prefer to ride in a kayak or a racecar?") == 2)


# ---------------------------------------------------------------------------------------------------


# * taller (25 points)

# Write a function taller that determines the taller of the heights of two people. Details:
# accepts two height arguments
# each height is a str in a set format, e.g., "6ft2in" , "4ft11in" , or "5ft0in" .
# the first number is a single digit/character, i.e., 0,1,2..,9 , representing the number of
# feet
# followed by 'ft'
# the second is a number in 0,1,2,..,11 representing the number of inches (this will be
# either 1 or 2 characters)
# followed by 'in'
# e.g., "6ft2in" means 6 feet and 2 inches.
# returns the taller of the two input strs


def taller(first_height, second_height):
    dimensions = []
    num = ""
    first = 0
    second = 0

    # calculating First height in inches
    for char in first_height:
        if char.isdigit():
            num += char  # Build the number
        else:
            if num:  # If we reached a non-digit and num is not empty
                dimensions.append(int(num))  # Convert to integer and add to the list
                num = ""  # Reset num for the next potential number

    for i in range(len(dimensions)):
        if i == 0:
            first += dimensions[i] * 12
        elif i == 1:
            first += dimensions[i]

    # cleaning dimension list for second height calculation
    dimensions = []

    # calculating Second height in inches
    for char in second_height:
        if char.isdigit():
            num += char
        else:
            if num:
                dimensions.append(int(num))
                num = ""

    for i in range(len(dimensions)):
        if i == 0:
            second += dimensions[i] * 12
        elif i == 1:
            second += dimensions[i]

    # comparing two height which is higher
    if first > second:
        return first_height
    else:
        return second_height


# =======================================================================


def taller(first_height, second_height):

    ft_in = []
    first = 0
    second = 0

    # filtering out digits for first height
    remove_ft = first_height.split("ft")
    remove_in = remove_ft[1].split("in")

    for list in [remove_ft, remove_in]:
        for num in list:
            if num.isdigit():
                ft_in.append(eval(num))

    # calculating first height in inches
    for i in range(len(ft_in)):
        if i == 0:
            first += ft_in[i] * 12
        elif i == 1:
            first += ft_in[i]

    # cleaning up ft_in to calculate second height
    ft_in = []

    # filtering out digits for first height
    remove_ft = second_height.split("ft")
    remove_in = remove_ft[1].split("in")

    for list in [remove_ft, remove_in]:
        for num in list:
            if num.isdigit():
                ft_in.append(eval(num))

    # calculating second height in inches
    for i in range(len(ft_in)):
        if i == 0:
            second += ft_in[i] * 12
        elif i == 1:
            second += ft_in[i]

    if first > second:
        return first_height
    else:
        return second_height


# print(taller("6ft2in","4ft11in"))
# print(taller("5ft2in","5ft11in"))
# print(taller("6ft2in","4ft11in"))
# print(taller("5ft2in","4ft11in"))
# print(taller("4ft2in","4ft11in"))
# print(taller("5ft9in","5ft11in"))
# print(taller("5ft9in","5ft11in") == '5ft11in')


# =======================================================================


def taller(height1, height2):
    # Helper function to convert height from "XftYin" to total inches
    def height_in_inches(height):
        # Find the position of 'ft' and 'in'
        ft_index = height.index("ft")
        in_index = height.index("in")

        # Extract the feet and inches part
        feet = int(height[:ft_index])  # Everything before 'ft' is the feet
        inches = int(
            height[ft_index + 2 : in_index]
        )  # Everything between 'ft' and 'in' is the inches

        # Convert the total height into inches
        return feet * 12 + inches

    # Compare the two heights in inches
    if height_in_inches(height1) > height_in_inches(height2):
        return height1
    else:
        return height2


# Example test cases
print(taller("6ft2in", "4ft11in"))  # Output: '6ft2in'
print(taller("5ft2in", "5ft11in"))  # Output: '5ft11in'
print(taller("10ft11in", "6ft2in"))  # Output: '10ft11in'
print(taller("10ft11in", "10ft10in"))  # Output: '10ft11in'
