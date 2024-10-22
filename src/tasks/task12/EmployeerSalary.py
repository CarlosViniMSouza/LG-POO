from Employeer import Employeer

class EmployeerSalary(Employeer):
    def __init__(self, name: str, register: int, monthly_salary: float) -> None:
        super().__init__(name, register)
        self._monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        return self._monthly_salary

    def calculate_salary_project(self, value_project: float) -> float:
        return value_project

    def get_montly_salary(self) -> float:
        return self._monthly_salary

    def set_montly_salary(self, monthly_salary) -> None:
        self._monthly_salary = monthly_salary