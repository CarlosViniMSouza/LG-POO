"""
Page: 53
Image: -
"""

from abc import ABC, abstractclassmethod # abstractmethod

class Animal(ABC):
    @abstractclassmethod
    #@abstractmethod
    #@classmethod
    def do_sound(self):
        pass

    def sleep(self):
        print("The animal is sleeping!")

class Dog(Animal):
    def do_sound(self):
        print("The dog do AuAu!")

class Cat(Animal):
    def do_sound(self):
        print("The cat do Meow!")

dog = Dog()
cat = Cat()

# using methods from subclasses
dog.do_sound()
cat.do_sound()

# using concrete methods from abstract class
dog.sleep()
cat.sleep()
