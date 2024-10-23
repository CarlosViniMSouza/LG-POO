from botcity.core import DesktopBot, Backend
from botcity.maestro import *

from services.methods_forms import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    # app_path = r"C:\Users\matutino\Documents\projects\LG-POO\assets\dist\task13.exe"

    bot = DesktopBot()
    # bot.execute(app_path)

    fillout_windows(bot)

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()