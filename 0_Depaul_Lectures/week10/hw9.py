class Stack(list):
    def push(self, item):
        list.append(self, item)
        # self.append(item)

    def __repr__(self):
        return f"Stack({list.__repr__(self)})"

    def __init__(self, iterable=[]):
        list.__init__(self, iterable)

    def __getitem__(self, index):
        return list.__getitem__(self, index)

    def pop(self):
        if not self.isEmpty():
            return list.pop(self, -1)
        else:
            raise IndexError("Cannot pop from an empty stack")

    def isEmpty(self):
        return len(self) == 0

    def len(self):
        # return len(self)
        return list.__len__(self)


# s = Stack()
# print(s)
# print(len( vars(s)))
# print(isinstance(s,list))

# s.push('apple')
# s.push('pear')
# s.push('kiwi')
# s.pop()

# print(s)
# print(s.isEmpty())
# print(s.pop())
# print(s.pop())
# print(s[0])
# print(s.__get)


def parenthesesMatch(parentheses_str):
    stack = Stack()
    matching_parentheses = {")": "(", "]": "[", "}": "{"}

    for char in parentheses_str:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.isEmpty():
                return False

            top = stack.pop()

            if matching_parentheses[char] != top:
                return False

    return stack.isEmpty()
    # return True


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("hw9TEST.py"))
