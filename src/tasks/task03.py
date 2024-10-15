class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def infos(self) -> None:
        print(f"Marca: {self.brand} \nModel: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, number_ports: int):
        super().__init__(brand, model)
        self.number_ports = number_ports

    def infos_complete(self) -> None:
        print(f"Marca: {self.brand} \nModel: {self.model} \nNum. Portas: {self.number_ports}")

myCar = Car("Toyota", "Corolla", 4)
myCar.infos()
myCar.infos_complete()
