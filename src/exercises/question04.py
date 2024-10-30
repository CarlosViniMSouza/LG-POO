"""
* Exercício 4: Polimorfismo 

- Objetivo: Demonstrar o polimorfismo, permitindo que diferentes classes implementem a mesma interface. 

- Enunciado: 
1. Crie uma função 'fazer_animais_falarem' que aceita uma lista de objetos da classe 'Animal' 
    e chama o método 'fazer_som' para cada um. 
2. Teste a função com uma lista contendo objetos de 'Cachorro' e 'Gato'.
"""

class Animal:
    list_animals = []
    
    @classmethod
    def add_animals(cls, animal) -> None:
        cls.list_animals.append(animal)

    @classmethod
    def make_sound(cls):
        return "It made noise"
    
    @classmethod
    def make_animals_talk(cls) -> None:
        if len(cls.list_animals) == 0:
            print("List animals is empty!")
            return None
        else:
            for animal in cls.list_animals:
                print(f"The {animal} is: {cls.make_sound()}")

Animal.add_animals("Dog")
Animal.add_animals("Cat")
print(Animal.make_animals_talk())