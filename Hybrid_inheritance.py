# Code to illustrate Hybrid Inheritance.

# Base class

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Class inheriting from both Dog and Cat
class Pet(Dog, Cat):
    def speak(self):
        # Call the speak method of the Dog class
        dog_speech = Dog.speak(self)
        # Call the speak method of the Cat class
        cat_speech = Cat.speak(self)
        return f"{self.name} says: {dog_speech} and {cat_speech}"

# Class inheriting from Pet
class ExoticPet(Pet):
    def speak(self):
        # Call the speak method of the Pet class
        pet_speech = Pet.speak(self)
        return f"{self.name} is an exotic pet. {pet_speech}"

# Creating objects of classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
pet = Pet("Max")
exotic_pet = ExoticPet("Zara")

# Calling the speak method of the objects
print(dog.name + ": " + dog.speak())  # Output: Buddy: Woof!
print(cat.name + ": " + cat.speak())  # Output: Whiskers: Meow!
print(pet.name + ": " + pet.speak())  # Output: Max says: Woof! and Meow!
print(exotic_pet.name + ": " + exotic_pet.speak())  # Output: Zara is an exotic pet. Max says: Woof! and Meow!




