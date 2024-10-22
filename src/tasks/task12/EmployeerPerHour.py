from Employeer import Employeer

class EmployeerPerHour(Employeer):
    def __init__(self, name: str, register: int, hours_worked: int, value_hour: float) -> None:
        super().__init__(name, register)
        self._hours_worked = hours_worked
        self._value_hour = value_hour
        
    def calculate_salary(self) -> float:
        return self._hours_worked * self._value_hour

    def calculate_salary_project(self, value_project: float) -> float:
        return value_project

    def get_hours_worked(self) -> int:
        return self._hours_worked

    def get_value_hour(self) -> float:
        return self._value_hour

    def set_hours_worked(self, hours_worked) -> None:
        self._hours_worked = hours_worked

    def set_value_hour(self, value_hour) -> None:
        self._value_hour = value_hour