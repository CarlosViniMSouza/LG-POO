from botcity.core import DesktopBot, Backend
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    app_path = r"C:\Users\matutino\Documents\projects\LG-POO\assets\dist\task13.exe"

    bot = DesktopBot()
    bot.execute(app_path)

    # Connecting to the application using the 'path' and 'title' selectors.
    bot.connect_to_app(Backend.WIN_32, path=app_path, title="Cadastro de Funcionários e Pagamentos")

    # Searching for the element that is in the context of the found window.
    btn_continue = bot.find_app_element(title="painel ''", class_name="TkChild")

    # Performing some operations with the found element.
    btn_continue.click()
    
    #bot.mouse_move(x=249, y=258)
    #bot.click_at(x=249, y=258)
    bot.kb_type("Carlos Souza")

    bot.wait(3000)

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()