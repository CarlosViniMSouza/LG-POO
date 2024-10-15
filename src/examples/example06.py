"""
Pages: 30
Image: 08
"""

class Animal: # Superclass
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal): # Subclass 01
    def speak(self):
        return f"\n{self.name} says 'Au Au!' ..."
    
class Cat(Animal): # Subclass 02
    def speak(self):
        return f"{self.name} says 'Meow!' ..."
    
dog = Dog("Totô")
cat = Cat("Felino")

print(dog.speak())
print(cat.speak())
