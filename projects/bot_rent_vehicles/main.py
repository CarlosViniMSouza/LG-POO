# from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.forms import *
from services.methods_forms import *

def main():
    # vehicle01 = Vehicle("name_vehicle", 2024, 1.0)
    car01 = Car("Chevrolet S10", 2024, 300, "gasolina")
    bike01 = Motorcycle("BMX XL", 2020, 75, 500)

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        # This is all pseudocode
        bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/resources/forms_base.html")
        fillout_forms_base(bot, car01)        

        # save_forms(car01)

        # http://127.0.0.1:5500/projects/bot_rent_vehicles/resources/forms_base.html
        # Criar função para escolher qual veículo selecionar

        button = 2
        
        if button == 1:
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/resources/forms_car.html")

            fillout_forms_car(bot, car01)
            save_forms(car01)

        elif button == 2:
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/resources/forms_motocycle.html")

            fillout_forms_motocycle(bot, bike01)
            save_forms(bike01)

        else:
            pass

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
