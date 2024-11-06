from .models.Product import Product
from .models.Order import Order
from .models.OrderManager import OrderManager

# Paths de Arquivos (CASA)
path_json = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.json"

path_pickle = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.pkl"

path_csv = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.csv"

# Paths de Arquivos (LAB)
path_json_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.json"

path_pickle_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.pkl"

path_csv_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.csv"

def use_case():
    # Criação dos products
    product01 = Product("T-shirt", 50.0, "Clothes")
    product02 = Product("Jeans", 100.0, "Clothes")
    product03 = Product("Short", 60.0, "Clothes")
    product04 = Product("Hat", 30.0, "Clothes")

    # Criação do pedido
    order01 = Order("Cliente 1")
    order01.add_product(product01, 10)
    order01.add_product(product02, 20)

    order02 = Order("Cliente 2")
    order02.add_product(product03, 30)
    order02.add_product(product04, 40)

    # Criação do manager de pedidos
    manager = OrderManager()
    manager.add_order(order01)
    manager.add_order(order02)

    """
    # Detalhes do pedido
    print(f"\n{order01.details_order()}\n")
    print(order02.details_order(), "\n")

    # Alterar status dos pedidos
    order01.update_status("Processing")
    # order02.update_status("Enviado")

    # Listar pedidos por status
    print(f"List Orders 'New': {manager.list_orders_by_status("New")}", "\n")
    print(f"List Orders 'Processing':  {manager.list_orders_by_status("Processing")}", "\n")
    # print(manager.list_orders_by_status("Enviado"))

    # Detalhes do pedido atualizado
    print(f"\n{order01.details_order()}\n")

    # Pedidos por categoria
    print(f"'Clothing' Requests: {manager.orders_by_category("Clothes")}", "\n")

    # Total de vendas
    print(f"Total Sales: R$ {manager.total_sales()}")
    """

    manager.save_json(path_json_lab)
    manager.save_csv(path_csv_lab)
    manager.save_pickle(path_pickle_lab)
    
    # manager.load_json(path_json_lab)
    # manager.load_csv(path_csv_lab)
    # manager.load_pickle(path_pickle_lab)
