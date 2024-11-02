class Pizza:
    def __init__(self, size="M", toppings=set()):
        self.size = size
        self.toppings = toppings

    def __repr__(self):
        # return f"Pizza('{self.size}',{self.toppings})"
        sorted_toppings = sorted(self.toppings)
        # return f"{sorted_toppings}"
        # return f"Pizza('{self.size}', {{{ ", ".join(str(topping) for topping in sorted_toppings) }}}"

        if not self.toppings:
            return f"Pizza('{self.size}',{self.toppings})"
        else:
            return f"Pizza('{self.size}',{{{ ", ".join(repr(topping) for topping in sorted_toppings) }}})"

    def setSize(self, new_size):
        self.size = new_size

    def getSize(self):
        return self.size

    def addTopping(self, topping):
        self.toppings.add(topping)

    def removeTopping(self, topping):
        self.toppings.remove(topping)

    def price(self):
        prices = {"S": 6.25, "M": 9.95, "L": 12.95}

        # total = 0
        # total += prices.get(self.size)

        total = prices.get(self.size, 0)

        if self.size == "S":
            total += len(self.toppings) * 0.7
        elif self.size == "M":
            total += len(self.toppings) * 1.45
        else:
            total += len(self.toppings) * 1.85

        return total

    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.size == other.size and len(self.toppings) == len(other.toppings)
        else:
            return False


# pie = Pizza()
# pie.setSize("L")
# pie.addTopping("pepperoni")
# pie.addTopping("anchovies")
# pie.addTopping("mushrooms")
# pie.removeTopping("mushrooms")

# print(pie)
# print(pie.price())
# pie2 = Pizza("L", {"mushrooms", "pepperoni"})
# print(pie2)
# print(pie == pie2)


def orderPizza():
    print("Welcome to Python Pizza!")

    size = input("What size pizza would you like (S,M,L): ")

    p = Pizza()
    p.setSize(size)

    while True:
        topping = input("Type topping to add (or Enter to quit): ")

        if topping != "":
            p.addTopping(topping)
        else:
            break

    print("Thanks for ordering!")
    print(f"Your pizza costs ${p.price()}")
    print(p)


# p = orderPizza()


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("hw8TEST.py"))
