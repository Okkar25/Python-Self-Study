"""


>>> from hw8 import *


>>> pie = Pizza()
>>> pie
Pizza('M',set())
>>> pie.setSize('L')
>>> pie.getSize()
'L'
>>> pie.addTopping('pepperoni')
>>> pie.addTopping('anchovies')
>>> pie.addTopping('mushrooms')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.addTopping('pepperoni')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.removeTopping('anchovies')
>>> pie
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie.price()
16.65
>>> pie2 = Pizza('L',{'mushrooms','pepperoni'})
>>> pie2
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie==pie2
True



>>> orderPizza()
Welcome to Python Pizza!
What size pizza would you like (S,M,L): M
Type topping to add (or Enter to quit): mushroom
Type topping to add (or Enter to quit): onion
Type topping to add (or Enter to quit): garlic
Type topping to add (or Enter to quit): 
Thanks for ordering!
Your pizza costs $14.299999999999999
Pizza('M',{'mushroom', 'onion', 'garlic'})
>>> orderPizza()
Welcome to Python Pizza!
What size pizza would you like (S,M,L): L
Type topping to add (or Enter to quit): calamari
Type topping to add (or Enter to quit): garlic
Type topping to add (or Enter to quit): 
Thanks for ordering!
Your pizza costs $16.65
Pizza('L',{'garlic', 'calamari'})
>>> p=orderPizza()
Welcome to Python Pizza!
What size pizza would you like (S,M,L): S
Type topping to add (or Enter to quit): 
Thanks for ordering!
Your pizza costs $6.25
>>> p
Pizza('S',set())
>>>





"""
