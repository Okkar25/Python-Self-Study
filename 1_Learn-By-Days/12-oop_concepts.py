# polymorphism 

# Polymorphism allows objects of different classes to be treated as objects of a common base class. It also means using the same method or operator in different ways for different objects.

class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

# print(animal_speak(dog))
# print(animal_speak(cat))


