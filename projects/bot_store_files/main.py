from botcity.maestro import *
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

from src.Product import Product
from src.Order import Order
from src.OrderManager import OrderManager

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    """
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # Implement here your logic...
    bot.browser("https://google.com")

    bot.wait(3000)
    bot.stop_browser()
    """

    ## Testing ##

    # Criando instâncias de Products com categorias 
    product01 = Product("Caneta", 1.50, "Escolar") 
    product02 = Product("Caderno", 10.00, "Escolar") 
    product03 = Product("Borracha", 0.75, "Escolar") 
    product04 = Product("Café", 5.00, "Alimento") 
    
    # Criando Orders com os Products 
    products01 = [product01, product02] 
    quant01 = {product01: 3, product02: 2} 
    order01 = Order(products01, quant01, "João") 
    
    products02 = [product03, product04] 
    quant02 = {product03: 4, product04: 1} 
    order02 = Order(products02, quant02, "Maria") 
    
    # Criando instância da classe manager e adicionando Orders  
    manager = OrderManager()
    manager.add_order(order01)
    manager.add_order(order02)

    # Vendo os pedidos realizados
    print(manager.show_orders())

    # Total de vendas
    print(manager.total_sales())
    
    # Verificando a quantidade vendida de Products da categoria "Escolar" 
    quant_schools_products = manager.orders_by_category("Escolar") 
    print(f"Quantidade vendida na categoria 'Escolar': {quant_schools_products}")

    # Vendo quantos produtos tem status "Novo"
    search_prod_by_status = manager.list_orders_by_status("Novo")

    for product in search_prod_by_status:
        print(f"Produtos com status 'Novo': {product}")

    ## End Test ##

    """
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )
    """

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
