from ..exceptions.InvalidValueError import InvalidValueError

class Product:
    def __init__(self, name: str, price: float, category: str) -> None:
        if price <= 0:
            raise InvalidValueError("Price must be positive value")
        
        self.name = name
        self.price = price
        self.category = category

    #@property
    def get_name(self) -> str:
        return self.name

    #@property
    def get_price(self) -> float:
        return self.price

    #@property
    def get_category(self) -> str:
        return self.category
    
    #@name.setter
    def set_name(self, name) -> None:
        self.name = name

    #@price.setter
    def set_price(self, price) -> None:
        self.price = price

    #@category.setter
    def set_category(self, category) -> None:
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