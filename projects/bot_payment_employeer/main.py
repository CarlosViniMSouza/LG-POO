from botcity.maestro import *

from services.services import *
from services.methods_forms import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    employeer_per_hour = EmployeerPerHour(name="Victor", register=1000, hours_worked=160, value_hour=30.55)
    employeer_salary = EmployeerSalary(name="Vinicius M. S.", register=1001, monthly_salary=5538.89)
    employeer_commissioned = EmployeerCommissioned(name="Vitoria", register=1002, base_salary=3450.6, sales=10, commission_rate=25.45)
    app_path_home = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\assets\dist\tkinter-gui.exe"
    # app_path_lab = r"C:\Users\matutino\Documents\projects\LG-POO\assets\dist\tkinter-gui.exe"

    bot = DesktopBot()
    bot.execute(app_path_home)

    try:
        fillout_employeer_per_hour(employeer_per_hour)
        fillout_employeer_salary(employeer_salary)
        fillout_employeer_commissioned(employeer_commissioned)

    except Exception as ex:
        print(ex)
    
    finally:
        print("Finished")

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()