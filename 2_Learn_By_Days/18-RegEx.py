# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.


import re as regex 

txt = "It is raining in Paris today"
x = regex.search("^It.*today$", txt)

# * returns a match object if a match is found
# print(x)
# print(bool(x))

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# The dot (.) matches any single character except a newline (\n).


# Examples:
# Regex pattern: a.b

# The dot (.) will match any single character between a and b.
# String: "acb" → Match (because there's a single character between a and b)
# String: "a*b" → Match (the * is treated as a single character)
# String: "ab" → No match (there is no character between a and b)
# String: "aXXb" → No match (because . only matches one character)

# regex pattern: ab*c

# The b* means "zero or more b characters".
# String: "ac" → Match (zero bs)
# String: "abc" → Match (one b)
# String: "abbc" → Match (two bs)
# String: "abbbc" → Match (three bs)
# Regex pattern: a.*c

# The .* means "zero or more of any characters".
# String: "ac" → Match (zero characters between a and c)
# String: "abc" → Match (one character between a and c)
# String: "aXYZc" → Match (multiple characters between a and c)
# String: "a123c" → Match (numbers between a and c)


# * RegEx Functions

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

import re 

txt = "I want visa my US visa approved visa"
x = re.findall("visa", txt)
# x = re.findall("UK", txt) # Return an empty list if no match was found
# print(x)

# x = re.split("\s", txt)
# x = re.split("\s", txt, 3)
# x = re.split("\\s", txt, 3)
# x = re.split(r"\s", txt, 3)
# x = re.split("\s", txt, 5)
# print(x)

# x = re.sub("\s", "-", txt)
x = re.sub("visa", "pizza", txt, 2)
# print(x)


# ----------------------------------------------------------------------------------------------


# * Metacharacters

# []	A set of characters	                                                          "[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)	  "\d"	
# .  	Any character (except newline character)	                                  "he..o"	
# ^	    Starts with                                                                   "^hello"	
# $	    Ends with                                                                     "planet$"	
# *	    Zero or more occurrences                                                      "he.*o"	
# +	    One or more occurrences                                                       "he.+o"	
# ?	    Zero or one occurrences                                                       "he.?o"      
# {}	Exactly the specified number of occurrences                                   "he.{2}o"	
# |	    Either or                                                                     "falls|stays"	
# ()	Capture and group

import re 

txt = "The rain in the Paris"
x = re.findall("[a-h]", txt)
# print(x)


txt1 = "That will be 59 dollars"
# x1 = re.findall("\d", txt1)
# print(x1)


txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
# print(x)


txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
# print(bool(x))
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")


txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")


txt = "helhjgdhfdgdfglo planet"
txt = "heo planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
# print(x)


txt = "heo planet"
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
# print(x)


txt = "hello planet"
# txt = "helo planet"
# txt = "heo planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
x = re.findall("he.?o", txt)
# print(x)


txt = "hello herro planet"
#Search for a sequence that starts with "he", followed exactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
# print(x)

#Check if the string contains either "falls" or "stays":
txt = "The rain in Spain falls mainly in the plain! stays"
x = re.findall("falls|stays", txt)
# print(x)


# ************* escape characters confusing ******************

# https://www.w3schools.com/python/gloss_python_escape_characters.asp



# -------------------------------------------------------------------------------------------------


# * Special Sequences

import re 

txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall(r"\AThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


#Check if "ain" is present at the beginning or end of a WORD:
txt = "The rain in ain Spain"
# x = re.findall(r"\bain", txt)
# x = re.findall(r"ain\b", txt)
# x = re.findall(r"\bain\b", txt)
# print(x)


#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
# x = re.findall(r"ain\b", txt)
# print(x)


#Check if the string contains any digits (numbers from 0-9):
txt = "The rain 10 in ain Spain 13"
x = re.findall(r"\d", txt)
# print(x)


#Return a match at every no-digit character:
txt = "The hello rain 10 in ain Spain 13"
x = re.findall(r"\D", txt)
# print(x)


txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall(r"\s", txt)
# print(x)


#Return a match at every NON white-space character:
x = re.findall(r"\S", txt)
# print(x)


txt = "The rain 100 in happy_world Spain 59"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall(r"\w", txt)
# print(x)


#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
txt = "The rain # $ in ? Spain!"
x = re.findall(r"\W", txt)
# print(x)


#Check if the string ends with "Spain":
txt = "The rain # $ in ? Spain"
x = re.findall(r"Spain\Z", txt)
# print(x)


# -------------------------------------------------------------------------------------------------


# *** Sets

txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
# print(x)


#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
# print(x)


#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
# print(x)


txt = "The rain 23 in Spain 190"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
# x = re.findall("[0-9]", txt)
# print(x)


#Check if the string has any two-digit numbers, from 00 to 59:
txt = "The rain 23 in Spain 190"
txt = "8 times 29 before 11:45 AM 68"
x = re.findall("[0-5][0-9]", txt) # first digit [0-5] last digit [0-9]
# print(x)


#Check if the string has any characters from a to z lower case, and A to Z upper case:
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
# print(x)


txt = "8 times + before 11:45 AM +"
#Check if the string has any + characters:
x = re.findall("[+]", txt)
# print(x)


# ----------------------------------------------------------------------------------------------

# * \s => white space 

import re

txt = "The rain in Spain"
x = re.search(r"\s", txt)
# print("The first white-space character is located in position:", x.start()) 


txt = "The rain in Spain"
x = txt.replace("Spain", "Paris")
# x = re.sub("\s", "-", txt, 2)
x = re.sub("Spain", "Paris", txt)
# print(x)


# ----------------------------------------------------------------------------------------------


# ** Match Object

import re 

txt = "The foolish fox jumps into the water to its reflection"
# x = re.findall("to", txt)
x = re.search("to", txt)
# print(x)


# * The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


import re

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)
# x = re.search(r"\bS\w", txt)
# print(x.span())


# x = re.search(r"\bS\w+", txt)
# x = re.search(r"\bS\w+", txt)
# print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:
x = re.search(r"\bS\w+", txt)
# print(x.group())


#* If there is no match, the value None will be returned, instead of the Match Object.


email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'



import re

# Regex pattern for email validation
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Test emails
emails = ["test@example.com", "user.name+alias@domain.co.uk", "invalid-email@", "123@invalid_domain.com"]

for email in emails:
    if re.match(email_pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is an invalid email address.")
