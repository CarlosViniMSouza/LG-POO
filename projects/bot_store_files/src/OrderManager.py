from functools import reduce
import json, csv, pickle

from .utils.log_activity import log_activity
from .Product import Product
from .Order import Order

@log_activity
class OrderManager:
    def __init__(self) -> None:
        self.orders = []

    # @log_activity
    def add_order(self, order) -> None:
        self.orders.append(order)

    # @log_activity
    def list_orders_by_status(self, status) -> list:
        list_orders = list(
            filter(lambda order: order.status == status, self.orders)
        )

        return [order.details_order() for order in list_orders]

    def orders_by_category(self, category) -> dict:
        products_by_category = list(
            filter(
                lambda product: any(
                    prod.category == category for prod in product.products
                ),
                self.orders
            )
        ) 
        
        return {category: len(products_by_category)}

    def total_sales(self) -> float:
        total = map(
            lambda order: sum(
                product.price * order.quantity[product] for product in order.products
            ), self.orders)
        
        total_sales = reduce(lambda x, y: x + y, total, 0) 

        return total_sales

    ## Save File (JSON) ##
    def save_json(self, file) -> None:
        try:
            with open(file, 'w') as file_json:
                json.dump([order.to_dict() for order in self.orders], file_json)
            print(f"Data saved successfully at {file} \n")

        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError:
            print(f"Error: Problem saving data to file {file}.")

    ## Load File (JSON) ##
    def load_json(self, file) -> None:
        try:
            with open(file, "r") as file_json:
                data = json.load(file_json)
                self.orders = [Order.from_dict(order) for order in data]
            print(f"Data loaded successfully from {file} \n")

        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError:
            print(f"Error: Problem saving data to file {file}.")

    ## Save File (CSV) ##
    def save_csv(self, file) -> None:
        try: 
            with open(file, 'w', newline='') as file_csv: 
                fieldnames = ['client', 'status', 'name', 'price', 'category', 'quantity'] 
                writer = csv.DictWriter(file_csv, fieldnames=fieldnames) 
                writer.writeheader()
                
                for order in self.orders: 
                    for product in order.products:
                        writer.writerow({
                            'client': order.client, 
                            'status': order.status, 
                            'name': product.name, 
                            'price': product.price, 
                            'category': product.category, 
                            'quantity': order.quantity[product]
                        })
            
            print(f"Data saved successfully at {file} \n")

        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError: 
            print(f"Error: Problem saving data to file {file}.")

    ## Load File (CSV) ##
    def load_csv(self, file): 
        try: 
            with open(file, 'r') as file_csv: 
                reader = csv.DictReader(file_csv) 
                dict_orders = {}

                for row in reader: 
                    client = row['client'] 
                    
                    if client not in dict_orders: 
                        dict_orders[client] = Order(client) 
                        dict_orders[client].status = row['status']

                        product = Product(
                            name=row['name'],
                            price=float(row['price']), 
                            category=row['category']
                        ) 

                        quantity = int(row['quantity'])
                        dict_orders[client].add_product(product, quantity) 
                    
                    self.orders = list(dict_orders.values())

            print(f"Data loaded successfully from {file} \n")

        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError: 
            print(f"Error: Problem saving data to file {file}.")

    ## Save File (PICKLE) ##
    def save_pickle(self, file) -> None:
        try:
            with open(file, "wb") as file_pkl:
                pickle.dump(self.orders, file_pkl)

            print(f"Data saved successfully at {file} \n")

        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError: 
            print(f"Error: Problem saving data to file {file}.")

    ## Load File (PICKLE) ##
    def load_pickle(self, file) -> None:
        try:
            with open(file, "rb") as file:
                self.orders = pickle.load(file)

            print(f"Data loaded successfully from {file} \n")
        
        except FileNotFoundError:
            print(f"Error: File {file} Not Found!")

        except IOError: 
            print(f"Error: Problem saving data to file {file}.")