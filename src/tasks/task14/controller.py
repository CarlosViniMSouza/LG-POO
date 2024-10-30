from functools import reduce

class Sales:
    def __init__(self, name: str, quantity: int, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

class SalesHistoric(Sales):
    list_sales = []

    @classmethod
    def get_list_sales(cls) -> None:
        print(cls.list_sales)

    @classmethod
    def add_product_to_list(cls, name, quantity, price) -> None:
        product = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        cls.list_sales.append(product)

    @classmethod
    def total_per_product(cls) -> float:
        for product in cls.list_sales:
            total_sales = reduce(lambda acc, product: acc + product["price"], cls.list_sales, 0) # work it

        return total_sales

    # Generator
    @classmethod
    def list_sales_above(cls, value) -> list:
        sales = list(filter(lambda product: float(product["price"]) >= value, cls.list_sales))
        
        return sales
    
###

def auth_access(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user and user.position == "Manager":
            return func(*args, **kwargs)
        else:
            raise PermissionError("Access denied!")
    return wrapper

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employees):
        self.employees.append(employees)

    @auth_access
    def increase_salary(self, user, name_employee, increment):
        for employees in self.employees:
            if employees.name == name_employee:
                employees.salary += increment
                print(f"{user.name} has authorized {name_employee} to start receiving R$ {employees.salary} next month")
                return
            
        print(f"{name_employee} Not Found!")

###

class Account:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, type, value):
        self.transactions.append({'type': type, 'value': value})

    def filter_transactions_por_type(self, type):
        return list(filter(lambda transaction: transaction['type'] == type, self.transactions))

    def apply_fee(self, rate):
        def rate_withdrawal_applied(transaction):
            if transaction['type'] == 'Withdrawal':
                transaction['value'] -= rate
            return transaction
        
        self.transactions = list(map(rate_withdrawal_applied, self.transactions))
