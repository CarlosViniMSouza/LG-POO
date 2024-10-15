"""
Pages: 31
Image: 09
"""

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
calc = Calculator()
print(calc.add(10))
print(calc.add(5, 15))
print(calc.add(5, 10, 15))