# from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.services import *
from services.forms import fillout_forms_base

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    book_loan = Book("The C++ Programming Language", "The Man", 100)

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_bookstore/bootstrap/index.html")

        fillout_forms_base(bot, book_loan)

        bot.browse("http://127.0.0.1:5500/projects/bot_bookstore/bootstrap/models/index.html")

    except Exception as ex:
        print(ex)
        bot.save_screenshot(r'C:\Users\matutino\Documents\projects\lg-poo\projects\bot_bookstore\resources\erro.png')

    finally:        
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
