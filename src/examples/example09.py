"""
Pages: 33
Image: 11
"""

class Calculator:
    def add(self, *args):
        return sum(args)
    
calc = Calculator()
print(calc.add(10))
print(calc.add(5, 15))
print(calc.add(5, 10, 15))