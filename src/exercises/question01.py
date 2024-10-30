"""
* Exercício 1: Definição de Classes e Objetos 

- Objetivo: Praticar a definição de classes e a criação de objetos. 

- Enunciado:
1. Crie  uma  classe  Pessoa  que  tenha  os  atributos  nome  e idade. 
2. Implemente um método 'apresentar' que imprima uma mensagem  apresentando a pessoa. 
3. Crie dois objetos da classe Pessoa e chame o método apresentar para cada um.
"""

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        return f"Hello {self.name}, you are {self.age} years old!"
    
carlos = People("Carlos", 23)
vinicius = People("Vinicius", 24)   

print(carlos.show())
print(vinicius.show())
