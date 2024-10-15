"""
Pages: 32
Image: 10
"""

class Animal:
    def do_sound(self):
        print("The animal did a sound!")

class Dog(Animal):
    def do_sound(self):
        print("The dog do 'AuAu' ...")

animal = Animal()
dog = Dog()

animal.do_sound()
dog.do_sound()
