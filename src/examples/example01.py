"""
Pages: 18
Image: 01
"""

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_yourself(self):
        print(f"My name is {self.name}, and I\'m {self.age} years old!")

people = People("Carlos", 23)
people.show_yourself()
