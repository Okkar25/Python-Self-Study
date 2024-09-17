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
x = re.split("\s", txt, 3)
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

