# hw9TEST.py

>>> from hw9 import *


##### Stack #####            

>>> s = Stack()
>>> len( vars(s)) # really inheriting? failure on this test means Stack is probably not properly inheriting
0
>>> isinstance(s,list)  # inheriting?
True

>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s.push('pear')
>>> s.push('kiwi')
>>> s
Stack(['apple', 'pear', 'kiwi'])
>>> top = s.pop()
>>> top
'kiwi'
>>> s
Stack(['apple', 'pear'])
>>> len(s)
2
>>> s.isEmpty()
False
>>> s.pop()
'pear'
>>> s.pop()
'apple'
>>> s.isEmpty()
True
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s[0]
'apple'
>>> 

if you receive an error on s2 then you are probably not calling the list
constructor init.


>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s2 = Stack()
>>> s2.push('pear')
>>> s2  # if this fails - see the TEST file for explanation
Stack(['pear'])


check that the Stack is really inheriting from list

>>> s = Stack()
>>> isinstance(s, list)
True
>>> len( vars(s) )==0
True

##### parenthesesMatch #####


>>> parenthesesMatch('(){}[]')
True
>>> parenthesesMatch('{[()]}')
True
>>> parenthesesMatch('((())){[()]}')
True
>>> parenthesesMatch('(}')
False
>>> parenthesesMatch(')(][') # right number, but out of order
False
>>> parenthesesMatch('([)]') # right number, but out of order
False
>>> parenthesesMatch('({])')
False
>>> parenthesesMatch('((())')
False
>>> parenthesesMatch('(()))')
False
