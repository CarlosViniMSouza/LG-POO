"""
Pages: 25, 26
Image: 06, 07
"""

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._age = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Value cannot be empty")
        self._name = value

# Creating a people class interface
try:
    people = People("Carlos", 25)
    print(f"Your age: {people.age}")
    # people.idade -= 5 # throws a ValueError
except ValueError as ex:
    print(ex) # output: "the exit cannot be negative"

# Verify the validation of the attribute name
try:
    # people.name = "" # throws a ValueError
    print(f"Your name: {people.name}")
except ValueError as ex:
    print(ex) # output: "the name cannot be empty"