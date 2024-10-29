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
    
### Continue Here to below

class Employeer:
    def __init__(self, name: str, position: str, salary: float) -> None:
        self.name = name
        self.position = position
        self.salary = salary

class HRSystem(Employeer):
    list_employeers = []

    def increase_salary(self) -> float:
        self.salary += 0.2 # 20% increment    
        return self.salary 
    
    # @classmethod # Decorator
    def authenticate_access(self) -> None:
        if self.position == "Manager":
            return f"Approved Salary Increase"
        else:
            print(f"Rejected Salary Increase")

###

class Account:
    transaction_list = []

    def filter_transaction_type(cls, type_transaction) -> list:
        type_transaction = list(filter(lambda x: x == "Deposit", cls.transaction_list))

        return type_transaction

    def applied_rate(cls, rate) -> list:
        rate_transaction = list(map(lambda x: x == "Withdrawal", cls.transaction_list))

        for transaction in rate_transaction:
            rate_transaction *= 0.1

        return rate_transaction
