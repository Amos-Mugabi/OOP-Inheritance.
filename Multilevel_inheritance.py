# Code to illustrate Multilevel inheritance.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class inheriting from Dog
class Labrador(Dog):
    def speak(self):
        return "Woof! I am a Labrador."

# Derived class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects of derived classes
dog = Dog("Buddy")
labrador = Labrador("Max")
cat = Cat("Whiskers")

# Calling the speak method of the objects
print(dog.name + ": " + dog.speak())  # Output: Buddy: Woof!
print(labrador.name + ": " + labrador.speak())  # Output: Max: Woof! I am a Labrador.
print(cat.name + ": " + cat.speak())  # Output: Whiskers: Meow!