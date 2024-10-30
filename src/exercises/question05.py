"""
* Exercício 5: Classes Abstratas 

- Objetivo: Utilizar classes abstratas para definir interfaces que devem ser implementadas pelas subclasses.

- Enunciado:  
1. Crie uma classe abstrata 'Forma' com um método abstrato 'Area' e um método concreto 'mostrar_area' que imprime a área calculada pela subclasse.  
2. Crie duas subclasses 'Quadrado' e 'Circulo' que implementam o método area.
"""
from abc import ABC, abstractclassmethod # abstractmethod

class GeometricShape(ABC):

    @abstractclassmethod
    # @classmethod
    # @abstractmethod
    def area_formula(cls):
        pass

    def show_area(cls) -> float:
        return f"The area calculated is {cls.area_formula()} m2"
    
class Square(GeometricShape):
    def __init__(self, side: float) -> None:
        self.side = side
    
    def area_formula(self) -> float:
        return self.side ** 2
    
class Circle(GeometricShape):
    def __init__(self, ray: float) -> None:
        self.ray = ray

    def area_formula(self) -> float:
        # pi = 3.1415
        result = 3.1415 * (self.ray ** 2)
        return "{:.2f}".format(result)

mySquare = Square(side=4)
print(mySquare.show_area())

myCircle = Circle(ray=4)
print(myCircle.show_area())