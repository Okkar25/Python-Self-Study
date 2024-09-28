# Accumulation

# 1 setting up a collection to iterate
numbers = [1, 2, 3, 4, 5]

# 2 Initialize accumulator
total_num = 0

# 3 Iterate over the collection and accumulate
for num in numbers:
    total_num += num
    
# 4 Return or print the final sum
# print("Total sum:", total)


# -------------------------------------------------------------------


def oddEven(list):
    for num in list:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

# oddEven( [22,33,44] )

def total(list):
    sum = 0
    for num in list:
        sum += num
    
    print(sum)
    # print(vars())

# total( [3,12,6,22] )


# -------------------------------------------------------------------


# * <op>= shorthand
# * <var> <op>= <expr>

x = 7
x = x + 3
x += 5
# print(x)

# i++ => not exist in Python ( only in Java, JS, C, C++)


# -------------------------------------------------------------------


# * counting

def countNegs(list):
    count_neg = 0
    
    for num in list:
        if num < 0:
            count_neg += 1
        
    print(count_neg)

# countNegs( [2,-55,-23,44,2] )


# -------------------------------------------------------------------


# * collecting

def negatives(list):
    neg_list = []
    
    for num in list:
        if num < 0:
            neg_list.append(num)
            
    print(neg_list)

# negatives( [2,-55,-23,44,2] )


# * accumulate a string

def stripPunct(str):
    for punctuation in ".,!?;:":
        str = str.replace(punctuation, "")
    print(str)
    
def stripPunct(str):
    new_str = ""
    for char in str:
        if char not in ".,!?;:":
            new_str += char
    print(new_str)

# stripPunct( "How, are, you?!." )


# * Search

# wrong
def hasVowel( s ):
    for char in s:
        if char in 'aeiou': # found vowel
            return True
        else:
            return False

def hasVowel(str):
    for char in str:
        if char in "aeiouAEIOU":
            return True
        
    return False

# print(hasVowel("hello how are you?"))


# * Indexed Iteration

# for i in range(len(str_value)):
#     print( i, str_value[i] )

fruit = 'peach'
 
# for i in range(len(fruit)):
#     print(i, fruit[i])


# * indexed accumulator

def vowelIndices(str):
    index_vowels = []
    
    for i in range(len(str)):
        if str[i] in "aeiouAEIOU":
            index_vowels.append(i)
    
    print(index_vowels)

# vowelIndices( 'hello, how are you?' )


# * indexed search

def firstVowel(str):
    for char in str:
        if char in "aeiouAEIOU":
            return 1
    
    return -1

def firstVowel(str):
    for i in range(len(str)):
        if str[i] in "aeiouAEIOU":
            return 1
    
    return -1
    
# print(firstVowel('hello, how are you?'))
# print(firstVowel('myth'))


# -------------------------------------------------------------------------------------


def words_with_no_vowels(str):
    no_vowel_words = []
    
    str_list = str.split(" ")
    
    for word in str_list:
        has_vowel = False
        
        for char in word:
            if char in "aeiouAEIOU":
                has_vowel = True
                break
        
        if not has_vowel:
            no_vowel_words.append(word)    
       
    return no_vowel_words


def words_with_no_vowels(str):
    no_vowel_words = []
    
    str_list = str.split(" ")
    
    for word in str_list:
        if all(char not in "aeiouAEIOU" for char in word):
            no_vowel_words.append(word)
            
    return no_vowel_words

sentence = "This is a test sentence with some words like fly by myth and try"
result = words_with_no_vowels(sentence)
# print("Words with no vowels:", result)


# ----------------------------------------------------------------------------------------


# Nested loops or 2d / nested iteration
# for # outer loop
# for # inner loop

# nested list

lst = [
['apple','pear','kiwi'],
['pizza','hamburger','sandwich'],
['cola','pepsi','beverage','wine']]

# print(lst[2])
# print(lst[2][3])
# print(lst[2][3][1])

# for row in lst:
#     print( row )

# for row in lst:
#     for item in row:
#         print( item )

# for row in lst:
#     for item in row:
#         print( item, end=' ')  
#     print() # # Print a new line after each row


# * 2d search


lst = [
['apple','pear','kiwi'],
['pizza','msg','salt'],
['cereal','chips','velveeta','cookies']]


def contains(fruit, list):
    for row in list:
        for item in row:
            if fruit == item:
                return True
    return False

# print(contains( 'kiwi', lst ))
# print(contains( 'Kiwi', lst ))
# print(contains( 'mustard', lst ))
# print(contains( 'cookies', lst ))


# * 2d, accumulator

def pairsThatAdd(search, first_list, second_list):
    
    pairs = []
    
    for num1 in first_list:
        for num2 in second_list:
            if num1 + num2 == search:
                pairs.append((num1, num2))
    
    return pairs

# print(pairsThatAdd( 5, [1,2,3], [4,1,2]))


# --------------------------------------------------------------------------------------


# * 2d, indexed accumulator


treasureMap =\
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~====X==============~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~======================~~~~~~~~~~~~~~~~~~
~~~~~~~~=========================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~==========X=========X=======~~~~~~~~~~~~~~~
~~~~~~~~~=========================~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~===================~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~=======================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~========================~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~=======X==========X==~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~====================~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~==================~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~=================~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def getTreasure(tmap):
    ''' return list of (row,col) locations
of all treasure (X) on tmap'''

    treasure_locations = []
    
    # tmap = tmap.split("\n")
    tmap = tmap.split()
    
    for row in range(len(tmap)):
        for col in range(len(tmap[row])):
            if tmap[row][col] == 'X':
                treasure_locations.append((row,col))
                
    return treasure_locations

# print(getTreasure( treasureMap ))


# --------------------------------------------------------------------------------------


# * indexed, search

# def isSorted(num_list):
#     sorted_list = sorted(num_list, key=lambda x : x)
#     if sorted_list == num_list:
#        return True
#     return False

def isSorted(num_list):
    # search for decreasing pair of numbers

    for i in range(len(num_list) - 1): 
        if num_list[i] > num_list[i + 1]:
            return False

    return True

# print(isSorted( [2,3,4,5,9,9,9,9,10,12] ))
# print( isSorted( [2,3,4,5,9,8,9,9,10,12] ))

