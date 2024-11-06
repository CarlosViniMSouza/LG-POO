from .exceptions.InvalidValueError import InvalidValueError

class Product:
    def __init__(self, name: str, price: float, category: str) -> None:
        if price <= 0:
            raise InvalidValueError("Price must be positive value")
        
        self.name = name
        self.price = price
        self.category = category

    def details_product(self) -> str:
        return f"Product: {self.name} | Price: R$ {self.price} | Category: {self.category}"
    
    def to_dict(self):
        return {
            'name': self.name, 
            'price': self.price, 
            'category': self.category
        }
    
    @classmethod 
    def from_dict(cls, data): 
        return cls(name=data['name'], price=data['price'], category=data['category'])
    
    def __repr__(self): 
        return f"Product(name={self.name}, price={self.price}, category={self.category})"