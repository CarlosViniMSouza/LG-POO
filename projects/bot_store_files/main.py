# from botcity.web import WebBot, Browser, By
# from webdriver_manager.chrome import ChromeDriverManager

from src.Product import Product
from src.Order import Order
from src.OrderManager import OrderManager

def main():
    """
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browser("https://google.com")
    
    bot.wait(3000)
    bot.stop_browser()
    """

    # Criação dos products
    product01 = Product("Camisa", 50.0, "Roupas")
    product02 = Product("Calça", 100.0, "Roupas")
    product03 = Product("Short", 60.0, "Roupas")
    product04 = Product("Sunga", 30.0, "Roupas")

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
    print(f"'Clothing' Requests: {manager.orders_by_category("Roupas")}", "\n")

    # Total de vendas
    print(f"Total Sales: R$ {manager.total_sales()}")

    # Salvar e carregar dados (MUDAR PATH ENTRE PCs)
    path_json = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.json"
    path_pickle = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.pkl"
    path_csv = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\src\assets\orders.csv"
    
    manager.save_json(path_json)
    manager.load_json(path_json)

    manager.save_csv(path_csv)
    manager.load_csv(path_csv)

    manager.save_pickle(path_pickle)
    manager.load_pickle(path_pickle)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
