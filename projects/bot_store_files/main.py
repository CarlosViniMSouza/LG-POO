from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

from src.models.Product import Product
from src.models.Order import Order
from src.models.OrderManager import OrderManager
from src.services.fillout_forms import fillout_forms

# Paths de Arquivos (LAB)
path_json_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.json"

path_pickle_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.pkl"

path_csv_lab = r"C:\Users\matutino\Documents\projects\LG-POO\projects\bot_store_files\src\assets\orders.csv"

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_store_files/web/index.html")

        bot.wait(2000)
        
        product01 = Product("T-shirt", 50.0, "Clothes")
        product02 = Product("Jeans", 100.0, "Clothes")
        
        fillout_forms(bot, product01)

        order01 = Order("Cliente 1")
        order01.add_product(product01, 10)
        order01.add_product(product02, 20)

        manager = OrderManager()
        manager.add_order(order01)

        manager.save_json(path_json_lab)
        manager.save_csv(path_csv_lab)
        manager.save_pickle(path_pickle_lab)

        #NOTE: To-do fillout_excel()

    except Exception as exc:
        print(exc)
    
    finally:
        bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
