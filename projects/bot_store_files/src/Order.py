from functools import reduce

class Order:
    def __init__(self, products: list, quantity: dict, client: str, status: str = "Novo") -> None:
        self.products = products # instances list
        self.quantity = quantity # dictionarie product
        self.client = client
        self.status = status # "Novo", "Processando", "Enviado"
    
    def add_product(self, product, quantity) -> None:
        if product in self.quantity:
            self.quantity[product] += quantity 
        else: 
            self.products.append(product)
            self.quantity[product] = quantity

    def update_status(self, new_status) -> None:
        if new_status in ["Novo", "Processando", "Enviado"]: 
            self.status = new_status 
        else: 
            raise ValueError("Status inválido. Use 'Novo', 'Processando' ou 'Enviado' ...")

    def total_order(self) -> float:
        prices = map(lambda product: product.price * self.quantity[product], self.products)
        total_products = reduce(lambda x, y: x + y, prices)

        return total_products

    def total_quantity(self) -> float:
        quantities = map(lambda product: self.quantity[product], self.products) 
        total_quantity = reduce(lambda x, y: x + y, quantities)

        return total_quantity

    def details_order(self, order):
        return f"Product details: {self.products} | Quant: {self.quantity} | Client: {self.client} | Status: {self.status}"
