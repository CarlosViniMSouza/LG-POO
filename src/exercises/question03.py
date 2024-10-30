"""
* Exercício 3: Herança 

- Objetivo: Implementar a herança entre classes e entender como reutilizar código. 

- Enunciado: 
1. Crie uma classe base Animal com um método fazer_som que levanta uma exceção NotImplementedError.  
2. Crie duas subclasses Cachorro e Gato que herdam de Animal e implementam o método fazer_som. 
"""

class Animal:
    def make_sound(self):
        raise NotImplementedError("This method should be implemented by subclasses!")
    
class Dog(Animal):
    def make_sound(self):
        return "Au Au"

    def run_and_jump(self):
        return "Jump and Run!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(f"The dog does {dog.make_sound()}")
print(f"The cat does {cat.make_sound()}")
