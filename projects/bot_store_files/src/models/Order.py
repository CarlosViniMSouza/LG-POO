from ..exceptions.InvalidQuantityError import InvalidQuantityError
from .Product import Product as prod

from functools import reduce

class Order:
    def __init__(self, client: str) -> None:
        self.products = [] # instances list
        self.quantity = {} # dictionarie product
        self.client = client
        self.status = "New"
    
    def add_product(self, product, quantity) -> None:
        if quantity <= 0:
            raise InvalidQuantityError("Quantity of Products must be greater than 0")
        
        if product in self.quantity:
            self.quantity[product] += quantity 
        else: 
            self.products.append(product)
            self.quantity[product] = quantity

    def update_status(self, new_status) -> None:
        if new_status in ['New', 'Processing', 'Submitted']: 
            self.status = new_status 
        else: 
            raise ValueError("Invalid status. Use 'New', 'Processing' or 'Submitted'...")

    def total_order(self) -> float:
        return reduce(lambda acc, product: acc + product.price * self.quantity[product], self.products, 0)

    def details_order(self):
        details = f"Client: {self.client} | Status: {self.status} | \nProducts:\n"
        
        for product in self.products:
            details += f"{prod.details_product(product)} - Quantity: {self.quantity[product]}\n"
        
        details += f"Total Order: R$ {self.total_order()}"
        return details
    
    def to_dict(self): 
        return {
            'client': self.client,
            'status': self.status,
            'products': [product.to_dict() for product in self.products], 
            'quantity': {product.name: quant for product, quant in self.quantity.items()},
        }
    
    @classmethod 
    def from_dict(cls, data): 
        order = cls(client=data['client'])
        order.status = data['status'] 
        
        for data_product in data['products']: 
            product = prod.from_dict(data_product) 
            quantity = data['quantity'][product.name] 
            order.add_product(product, quantity) 
            
        return order
    
    def __repr__(self):
        return f"Order(client={self.client}, status={self.status}, total={self.total_order()})"
