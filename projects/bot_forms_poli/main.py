from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.services import *
from services.methods_forms import *

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    forms_base = BotBase("Carlos Souza", "cvmds", "cvmds@email.com", "admin123")
    forms_atualizar = BotAtualizacao("Carlos Vinicius", "cvmds_2024")
    forms_cadastro = BotCadastro("cvmds_2024", "admin123")

    try:
        fillout_forms_base(bot, forms_base)
        print(forms_base.preencher_formulario())

        fillout_forms_cadastro(bot, forms_cadastro)
        print(forms_cadastro.preencher_formulario())

        fillout_forms_atualizar(bot, forms_atualizar)
        print(forms_atualizar.preencher_formulario())

    except Exception as ex:
        print(ex)
    
    finally:        
        bot.wait(2000)
        print("Finished")

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
