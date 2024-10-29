from functools import reduce

class Sales:
    def __init__(self, name: str, quantity: int, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

class SalesHistoric(Sales):
    list_sales = []

    """
    def __init__(self, name_product, quantity_product, price_product):
        super().__init__(name=name_product, quantity=quantity_product, price=price_product)
    """

    @classmethod
    def add_product_to_list(cls, self) -> None:
        product = {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

        cls.list_sales.append(product)

    @classmethod
    def total_per_product(cls) -> float:
        total_sales = reduce(lambda x, y: x + y, cls.list_sales) # work it

        return total_sales

    @classmethod # Generator 
    def list_sales_above(cls, value) -> float:
        sales = list(filter(lambda x: x >= value, cls.list_sales)) # work it

        return sales

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
