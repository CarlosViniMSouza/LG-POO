# Import for the Web Bot
from webdriver_manager.chrome import ChromeDriverManager

from services.forms import *
from services.methods_forms import *

def main():
    forms_base = FormsBase("Carlos Souza", "2021002252@ifam.edu.br", "admin123")
    forms_contact = FormsContact("(12) 1234-1234")
    forms_login = FormsLogin("CarlosViniMSouza")

    # remover depois
    # forms_complete = FormsComplete("Carlos Souza", "2021002252@ifam.edu.br", "admin123", "(12) 1234-1234", "CarlosViniMSouza")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        bot.browse("http://127.0.0.1:5500/projects/bot_multiples_forms/resources/forms_base.html")
        data_base = fillout_forms_base(bot, forms_base)

        bot.browse("http://127.0.0.1:5500/projects/bot_multiples_forms/resources/forms_contact.html")
        data_contact = fillout_forms_contact(bot, forms_contact)

        bot.browse("http://127.0.0.1:5500/projects/bot_multiples_forms/resources/forms_login.html")
        data_login = fillout_forms_login(bot, forms_login)

        # save_forms(forms_complete)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        # print(forms_base.show_infos_name())

        data_complete = FormsComplete(
            forms_base.show_infos_name(), 
            forms_base.show_infos_email(), 
            forms_base.show_infos_password(),
            forms_contact.show_infos_contact(),
            forms_login.show_infos_login()
        )

        save_forms(data_complete)
        
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
