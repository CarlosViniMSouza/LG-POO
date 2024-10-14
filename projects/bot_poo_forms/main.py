# Import for the Web Bot
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser, By

from resources.services import Product

def create_product(bot, product):
    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(product.get_name())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="price"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="price"]', By.XPATH).send_keys(product.get_price())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="quant"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="quant"]', By.XPATH).send_keys(product.get_quant())
    bot.wait(1000)

    bot.enter()

def save_product(product):
    # Open a file in append mode
    file = open(r"C:\Users\matutino\Documents\projects\lg-poo\projects\bot_poo_forms\resources\product.txt", "a")

    # Append some text to the file
    file.write(product.get_name() + "\n")
    file.write(str(product.get_price()) + "\n")
    file.write(str(product.get_quant()) + "\n")

    # Close the file
    file.close()


def main():
    product = Product("Notebook", 5000, 1)

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("http://127.0.0.1:5500/projects/bot_poo_forms/resources/index.html")

    try:
        data = create_product(bot, product)
        save_product(product)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)  

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
