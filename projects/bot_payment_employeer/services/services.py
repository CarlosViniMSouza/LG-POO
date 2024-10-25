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
    
def process_payment():
    list_employeers = [
        EmployeerPerHour("Victor", 1000, 160, 30.55),
        EmployeerSalary("Vinicius M. S.", 1001, 5538.89),
        EmployeerCommissioned("Bia", 1002, 3450.6, 10, 25.45)
    ]

    for item in list_employeers:
        print(f"Salary of {item.get_name()}: R$ {item.calculate_salary()}")

    # modifying 'hours_worked' and 'value_hour' from 'EmployeerPerHour'
    list_employeers[0].set_hours_worked(100)
    list_employeers[0].set_value_hour(30.55)
    
    print(f"New salary of bricklayer: R$ {list_employeers[0].calculate_salary()}")

# if __name__ == "__main__":
#     process_payment()
