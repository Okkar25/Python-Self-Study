# Python Polymorphism

# The word "polymorphism" means "many forms"
# In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# * Function Polymorphism

# An example of a Python function that can be used on different objects is the len() function.

x = "Hello World!"
my_tuple = ("apple", "banana", "cherry")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(len(my_tuple))
# print(len(x))
# print(len(car))


# * Class Polymorphism

# In polymorphism we can have multiple classes with the same method name.

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def travel(self):
        return "Fly!"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def travel(self):
        return "Drive!"
        
class Ship:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def travel(self):
        return "Sail!"
    
plane1 = Plane("Thai Air Ways", "727")
car1 = Car("Ford", "Mustang")
ship1 = Ship("Ocean Liner", "Touring 20")

def move(vehicle):
    return vehicle.travel()

# print(move(plane1))
# print(move(car1))
# print(move(ship1))

# for vehicle in (car1, plane1, ship1):
#     print(vehicle.travel())



# -----------------------------------------------------------------------------------------



# * Inheritance Class Polymorphism 
# Method Overriding 

class Vehicle:
    def __init__(self, brand, model):
        self.model = model 
        self.brand = brand
    
    def move(self):
        return "Transport!"

class Car(Vehicle):
    pass

car1 = Car("Ford", "Mustang")

class Plane(Vehicle):
    def __init__(self, brand, model, engine):
        # Plane.__init__(self, brand, model)
        super().__init__(brand, model)
        self.engine = engine

    def move(self):
        return "Fly!"
    
plane1 = Plane("Thai Air Ways", "747", "Turboshaft")
# print(plane1.engine)
# print(plane1.move())


class Ship(Vehicle):
    def move(self):
        return "Sail!"
    
    def __repr__(self):
        return "This is __repr__ method"

ship1 = Ship("Ocean Liner", "Touring 20")
# print(ship1.move())
# print(ship1.__repr__())
# print(repr(ship1))

def travel(vehicle_type):
    return vehicle_type.move()
    
# print(travel(car1))
# print(travel(plane1))
# print(travel(ship1))

# for vehicle in (car1, plane1, ship1):
#     print(vehicle.move()) 



# Child classes inherits the properties and methods from the parent class.
# the Car class is empty, but it inherits brand, model, and move() from Vehicle.
# Ship and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
# Because of polymorphism we can execute the same method for all classes
