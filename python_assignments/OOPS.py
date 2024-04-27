# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Subclass 3
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Function demonstrating polymorphism
def animal_sound(animal):
    return animal.make_sound()

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Using polymorphism
print(animal_sound(dog))   # Output: Woof!
print(animal_sound(cat))   # Output: Meow!
print(animal_sound(bird))  # Output: Chirp!