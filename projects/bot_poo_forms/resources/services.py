class Product:
    def __init__(self, name, price, quant):
        self._name = name
        self._price = price
        self._quant = quant

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quant(self):
        return self._quant

    def update_name(self, name):
        self._name = name

    def update_price(self, price):
        self._price = price

    def update_quant(self, quant):
        self._quant = quant

# product = Product("Notebook", 5000, 1)
# product.show_infos()
# 
# print("\n Updating ... \n")
# 
# product.update_name("Notebook Lenovo")
# product.update_price(5500)
# product.update_quant(5)
# 
# product.show_infos()