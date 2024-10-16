# from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.forms import *
from services.methods_forms import *

def main():
    car01 = Car("Chevrolet S10", 2024, 300, "gasolina")
    bike01 = Motorcycle("BMX XL", 2020, 75, 500)

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/index.html")
        fillout_forms_base(bot, bike01)

        # http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/forms/index.html
        # Criar função para escolher qual veículo selecionar

        button = 2
        
        if button == 1:
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/forms/forms_car.html")

            fillout_forms_car(bot, car01)
            save_forms(car01)

        elif button == 2:
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/forms/forms_motocycle.html")

            fillout_forms_motocycle(bot, bike01)
            save_forms(bike01)

        else:
            print(f"Error changing forms")

    except Exception as ex:
        print(ex)
        bot.save_screenshot('./resources/erro.png')

    finally:        
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
