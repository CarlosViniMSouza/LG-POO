from functools import reduce
from json import dumps

from .Order import Order
from .Product import Product

class FileNotFoundError(Exception):
    """
    Error opening or loading a file
    """
    pass

class InvalidValueError(Exception):
    """
    Prices must be positive value.
    """
    pass

class InvalidQuantityError(Exception):
    """
    Quantity must be positive value.
    """
    pass

class OrderManager:
    def __init__(self) -> None:
        self.orders: list = []

    ## Decorator Logs ##

    def log_activity(func):
        def wrapper(*args, **kwargs):
            pass
            
        return wrapper

    ## Methods ##

    def show_orders(self) -> list:
        return self.orders

    # @log_activity
    def add_order(self, order) -> None:
        self.orders.append(order)

    # @log_activity
    def list_orders_by_status(self, status) -> list:
        return list(filter(lambda order: order.status == status, self.orders)) 

    def orders_by_category(self, category) -> int:
        quantities = map(
            lambda order: sum(
                order.quantity[product] for product in order.products if product.category == category),
            self.orders
        ) 
        
        total_quantity = reduce(lambda x, y: x + y, quantities, 0)
        
        return total_quantity

    def total_sales(self): 
        total = map(
            lambda order: sum(product.price * order.quantity[product] for product in order.products),
                self.orders
            )
                
        total_sales = reduce(lambda x, y: x + y, total, 0) 
        # Valor inicial 0 return total_sales

        return total_sales

    ## File Manipulation ##

    def save_data_json(self) -> None:
        pass

    def load_data_json(self) -> None:
        pass

    def save_data_binary(self) -> None:
        pass

    def load_data_binary(self) -> None:
        pass
