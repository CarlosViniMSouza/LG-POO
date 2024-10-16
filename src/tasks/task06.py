class Vehicle:
    def __init__(self, name: str, year: int, daily_value: float) -> None:
        self._name = name
        self._year = year
        self._daily_value = daily_value

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def year(self) -> int:
        return self._year
    
    @property
    def daily_value(self) -> float:
        return self._daily_value
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @year.setter
    def year(self, year: int) -> None:
        self._year = year

    @daily_value.setter
    def daily_value(self, daily_value: float) -> None:
        self._daily_value = daily_value

    def calc_total_rental(self, number_days: int, discount: float) -> float:
        result = self.daily_value * number_days * (1 - discount)

        if number_days > 7:
            result *= 0.9 # 10% discount
        
        return result

    @classmethod
    def increase_rent(cls, percent) -> float:
        cls.daily_value = cls.daily_value * (percent / 100)

        return cls.daily_value

class Car(Vehicle):
    def __init__(self, name: str, year: int, daily_value: float, type_gasoline: str) -> None:
        super().__init__(name, year, daily_value)
        self.type_gasoline = type_gasoline

class Motorcycle(Vehicle):
    def __init__(self, name: str, year: int, daily_value: float, cc: int):
        super().__init__(name, year, daily_value)
        self.cc = cc

    def calc_total_rental(self, number_days, discount=0) -> float:
        total_value = super().calc_total_rental(number_days, discount)

        if self.cc > 200:
            total_value += 1.10

        return total_value