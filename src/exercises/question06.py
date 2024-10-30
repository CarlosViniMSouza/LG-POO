"""
* Exercício 6: Composição 

- Objetivo: Demonstrar o uso da composição para construir objetos complexos 
a partir de componentes mais simples. 

- Enunciado: 
1. Crie uma classe Motor e uma classe Roda. 
2. Em seguida, crie uma classe Carro que tenha instâncias de Motor e Roda como atributos.  
3. Implemente métodos na classe Carro para ligar o motor e girar as rodas.
"""

class Motor:
    def __init__(self, potency) -> None:
        self.potency = potency

    def motor_on(self) -> str:
        return f"{self.potency} horsepower motor on!"
    
class Wheel:
    def __init__(self, size) -> None:
        self.size = size

class Car:
    def __init__(self, motor_potency, wheel_size) -> None:
        self.motor = Motor(motor_potency)
        self.wheel = Wheel(wheel_size)
    
    def show_infos(self) -> None:
        print(f"Motor Potency: {self.motor.potency} horsepower")
        print(f"Wheel Size: {self.wheel.size} inches")

myCar = Car(1000, 45)
myCar.show_infos()
