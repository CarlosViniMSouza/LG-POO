from Employeer import Employeer

class EmployeerCommissioned(Employeer):
    def __init__(self, name: str, register: int, base_salary: float, sales: int, commission_rate: float) -> None:
        super().__init__(name, register)
        self._base_salary = base_salary
        self._sales = sales
        self._commission_rate = commission_rate

    def calculate_salary(self) -> float:
        return self._base_salary + (self._sales * self._commission_rate)

    def calculate_salary_project(self, value_project: float) -> float:
        return value_project

    def get_base_salary(self) -> float:
        return self._base_salary

    def get_sales(self) -> int:
        return self._sales

    def get_commision_rate(self) -> float:
        return self._commission_rate

    def set_base_salary(self, base_salary) -> None:
        self._base_salary = base_salary

    def set_sales(self, sales) -> None:
        self._sales = sales

    def set_commision_rate(self, commission_rate) -> None:
        self._commission_rate = commission_rate