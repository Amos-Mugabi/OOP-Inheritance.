# Code to illustrate Hybrid Inheritance.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class 3
class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Calling the speak method of the objects
print(dog.name + ": " + dog.speak())  # Output: Buddy: Woof!
print(cat.name + ": " + cat.speak())  # Output: Whiskers: Meow!
print(bird.name + ": " + bird.speak())  # Output: Tweetie: Chirp!
