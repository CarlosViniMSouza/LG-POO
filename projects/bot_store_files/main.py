from botcity.web import WebBot, Browser
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.models.Product import Product
from src.models.Order import Order
from src.models.OrderManager import OrderManager

from src.services.forms.fillout_forms import fillout_forms
from src.services.forms.fillout_excel import fillout_excel

from src.services.spreadsheets import spreadsheets
from src.services.database import database

# Paths de Arquivos (CASA)
path_json = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\assets\orders.json"
path_pickle = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\assets\orders.pkl"
path_csv = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\assets\orders.csv"
path_xlsx = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_store_files\assets\products.xlsx"

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.EDGE
    bot.driver_path = EdgeChromiumDriverManager().install()

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_store_files/web/index.html")
        bot.wait(2000)

        product01 = Product("T-shirt", 50.0, "Clothes")
        product02 = Product("Jeans", 100.0, "Clothes")
        product03 = Product("Shoe", 150.0, "Footwear")

        products = [product01, product02, product03]

        try:
            fillout_forms(bot, product01)
            fillout_excel(products, path_xlsx)
        
        except Exception as ex:
            print(ex)
        
        order01 = Order("Cliente 1")
        order01.add_product(product01, 10)
        order01.add_product(product02, 20)

        manager = OrderManager()
        manager.add_order(order01)

        try:
            manager.save_json(path_json)
            manager.save_csv(path_csv)
            manager.save_pickle(path_pickle)
        
        except Exception as ex:
            print(ex)

        print('Working with Spreadsheet')

        try:
            df = spreadsheets.read_excel(path_xlsx, 'Products Order')

            for index, product in df.iterrows():
                database.insert_product_db(product)

            spreadsheets.show_data_excel(df)

        except Exception as ex:
            print(ex)

    except Exception as exc:
        print(exc)
    
    finally:
        print("Finished")

    # bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
