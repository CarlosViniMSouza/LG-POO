class Product:
    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category

    def details(self) -> str:
        return f"Product details: {self.name}: R$ {self.price} | Category: {self.category}"