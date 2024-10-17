# from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.forms import *
from services.methods_forms import *

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    car = Car("Chevrolet S10", 2024, 300, "gasolina")
    bike = Motorcycle("BMX XL", 2020, 75, 500)

    select = bike # button for select Car or Bike

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/index.html")

        fillout_forms_base(bot, select)
        
        if select == car:
            select_check_ratio_car(bot)
            
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/forms/forms_car.html")
            
            fillout_forms_car(bot, select)
            submit_vehicle_calc_rent(bot)
            save_forms_car(select)

        elif select == bike:
            select_check_ratio_motorcycle(bot)
            
            bot.browse("http://127.0.0.1:5500/projects/bot_rent_vehicles/bootstrap/forms/forms_motorcycle.html")

            fillout_forms_motocycle(bot, select)
            submit_vehicle_calc_rent(bot)
            save_forms_motorcycle(select)
        else:
            print("Erro changing forms!")

    except Exception as ex:
        print(ex)
        bot.save_screenshot(r'C:\Users\matutino\Documents\projects\lg-poo\projects\bot_rent_vehicles\resources\erro.png')

    finally:        
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
