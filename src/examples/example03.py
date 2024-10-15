"""
Pages: 20
Image: 03
"""

class Example:
    counter = 0

    def __init__(self, value):
        self.value = value
        Example.counter += 1

    def instance_method(self):
        print(f"Instance value: {self.value}")

    @classmethod
    def class_method(cls):
        print(f"Class counter: {cls.counter}")

obj01 = Example(5)
obj02 = Example(6)

obj01.instance_method()
obj02.instance_method()

Example.class_method()
