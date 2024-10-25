from botcity.maestro import *

from services.methods_forms import *
from services.services import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    employeer = EmployeerSalary(name="Vinicius M. S.", register=12345, monthly_salary=6730)
    # app_path_home = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\assets\dist\task13.exe"
    # app_path_lab = r"C:\Users\matutino\Documents\projects\LG-POO\assets\dist\task13.exe"

    # bot = DesktopBot()
    # bot.execute(app_path_home)

    try:
        fillout_windows(employeer)
    except Exception as ex:
        print(ex)
    finally:
        bot.wait(2000)

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()