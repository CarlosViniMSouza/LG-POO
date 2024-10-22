from abc import ABC, abstractclassmethod

class Employeer(ABC):
    def __init__(self, name: str, register: int) -> None:
        self._name = name
        self._register = register

    @abstractclassmethod
    def calculate_salary(self):
        pass
        # print("Your salary is X")

    @abstractclassmethod
    def calculate_salary_project(self):
        pass

    def get_name(self) -> str:
        return self._name

    def get_register(self) -> int:
        return self._register

    def set_name(self, name: str) -> None:
        self._name = name

    def set_register(self, register: int) -> None:
        self._register = register
