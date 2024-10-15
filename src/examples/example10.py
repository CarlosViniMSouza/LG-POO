"""
Pages: 33
Image: 11
"""

class Animal:
    def do_sound(self):
        print("\nThe animal did a sound!")

class Cat(Animal):
    def do_sound(self):
        print("The cat do 'Meow!' ...")

animal = Animal()
cat = Cat()

animal.do_sound()
cat.do_sound()
