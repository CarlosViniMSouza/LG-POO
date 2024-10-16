class Vehicle:
    _number_vehicles = 0

    def __init__(self, name: str, year: int, daily_value: float):
        self._name = name
        self._year = year
        self._daily_value = daily_value
        Vehicle._number_vehicles += 1

    @property
    def name(self):
        return self._name
    
    @property
    def year(self):
        return self._year
    
    @property
    def daily_value(self):
        return self._daily_value
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @year.setter
    def year(self, year: int):
        self._year = year

    @daily_value.setter
    def daily_value(self, daily_value: float):
        self._daily_value = daily_value

    def calc_total_rental(self, number_days: int, discount: float):
        result = self.daily_value * number_days * (1 - discount)

        if number_days > 7:
            result *= 0.9 # 10% discount
        
        return result
    
    @classmethod
    def counter_vehicles(cls):
        return cls._number_vehicles

    @classmethod
    def increase_rent(cls, percent):
        cls.daily_value = cls.daily_value * (percent / 100)

        return cls.daily_value

class Car(Vehicle):
    def __init__(self, name: str, year: int, daily_value: float, type_gasoline: str):
        super().__init__(name, year, daily_value)
        self.type_gasoline = type_gasoline

class Motorcycle(Vehicle):
    def __init__(self, name: str, year: int, daily_value: float, cc: int):
        super().__init__(name, year, daily_value)
        self.cc = cc

    def calc_total_rental(self, number_days, discount=0):
        total_value = super().calc_total_rental(number_days, discount)

        if self.cc > 200:
            total_value += 1.10

        return total_value
    
# # Criando 4 automoveis diferentes
# car01 = Car("Chevrolet S10", 2024, 300, "gasolina")
# car02 = Car("Hylux Toyota", 2024, 315, "diesel")

# bike01 = Motorcycle("BMX XL", 2020, 75, 500)
# bike02 = Motorcycle("BMX XXL", 2020, 85, 525)

# print("\nTotal Value Rental (with discount)\n")
# print(f"Rent Total Value (S10) by 7 days: R${car01.calc_total_rental(7, 0.1)}")
# print(f"Rent Total Value (Hylux) by 7 days: R${car02.calc_total_rental(7, 0.15)}")

# print(f"Rent Total Value (BMX XL) by 7 days: R${bike01.calc_total_rental(7, 0.1)}")
# print(f"Rent Total Value (BMX XXL) by 7 days: R${bike02.calc_total_rental(7, 0.15)}")

# print("\nTotal Value Rental (without discount)\n")
# print(f"Rent Total Value (S10) by 7 days: R${car01.calc_total_rental(7, 0)}")
# print(f"Rent Total Value (Hylux) by 7 days: R${car02.calc_total_rental(7, 0)}")

# print(f"Rent Total Value (BMX XL) by 7 days: R${bike01.calc_total_rental(7, 0)}")
# print(f"Rent Total Value (BMX XXL) by 7 days: R${bike02.calc_total_rental(7, 0)}")

# # Contagem de veiculos
# print(f"\nCounter vehicles: {Vehicle.counter_vehicles()}\n")