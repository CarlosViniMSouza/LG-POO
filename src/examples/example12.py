"""
Pages: 39
Images: 15, 16
"""

class Motor:
    def __init__(self, potency):
        self.potency = potency

    def on_motor(self):
        print(f"{self.potency} horsepower engine on")

class Wheel:
    def __init__(self, size):
        self.size = size

    def rotate(self):
        print(f"{self.size} inch wheel spinning")
    
class Car:
    def __init__(self, brand, model, motor_potency, size_wheels):
        self.brand = brand
        self.model = model
        self.motor = Motor(motor_potency)
        self.wheels = [Wheel(size_wheels) for _ in range(4)]

    def on_car(self):
        print(f"Car {self.brand}, {self.model} ON!")

        self.motor.on_motor()
        for wheel in self.wheels:
            wheel.rotate()

myCar = Car("Toyota", "Corolla", 150, 25)

myCar.on_car()
