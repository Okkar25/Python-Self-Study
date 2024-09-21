# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
# print(txt)


# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.1f} dollars"
txt = f"The price is {price:.2f} dollars"
txt = f"The price is {price:.0f} dollars"
# print(txt)


txt = f"The total cost is ${10 * 300}"
# print(txt)


price = 59
tax = 0.25
txt = f"The price is ${price + (price * tax)}"
# print(txt)


# If .... Else ..... short hand property

price = 49
txt = f"It is {"Expensive!" if price > 50 else "Cheap!"}"
# print(txt)


fruit = "apples"
txt = f"I love {fruit.upper()}"
# print(txt)


def sum(a, b):
    return a + b

txt = f"The result is {sum(10, 20)}"
# print(txt)


# More Modifiers
# Use a comma as a thousand separator:

price = 59000
txt = f"The price is {price:,} dollars"
txt = f"The price is {price:_} dollars"
# print(txt)


#Use "%" to convert the number into a percentage format:

txt = f"You scored {0.25:%}"
# print(txt)

#Or, without any decimals:

txt = f"You scored {0.25:.0%}"
# print(txt)

# https://www.w3schools.com/python/python_string_formatting.asp



# * String format()

price = 49
txt = "The price is {} dollars"
txt = "The price is {:.2f} dollars"
# print(txt.format(price))


# Multiple Values

quantity = 3
item_no = 567
price = 49

order = "I want {} pieces of item number {} for {:.2f} dollars."
# print(order.format(quantity, item_no, price))


# Index Numbers

order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(order.format(quantity, item_no, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))


# Named Indexes
my_order = "I have a {phone}, it has a {model} chip."
# print(my_order.format(model="A18", phone="iPhone 16"))



