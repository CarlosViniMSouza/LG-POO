"""
* Exercício 7: Tratamento de Exceções 

- Objetivo: Praticar o tratamento de exceções para garantir que o programa lide com erros de forma controlada.

- Enunciado: 
1. Crie uma função dividir que recebe dois números e retorna o resultado da divisão.  
2. Implemente o tratamento de exceções para lidar com divisão por zero e entrada de dados inválida.
"""

class Calculator:
    def __init__(self, number01: int, number02: int) -> None:
        self.number01 = number01
        self.number02 = number02

    def divide(self) -> float:
        try:
            return self.number01 / self.number02
        except Exception as err:
            print(f"Error: {err}")
            
            return None
    
calculator = Calculator(10, 0)
print(calculator.divide())
