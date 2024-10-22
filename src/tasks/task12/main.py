from EmployeerCommissioned import EmployeerCommissioned
from EmployeerPerHour import EmployeerPerHour
from EmployeerSalary import EmployeerSalary

def process_payment():
    list_employeers = [
        EmployeerPerHour("Victor", 1000, 160, 30.55),
        EmployeerSalary("Vinicius M. S.", 1001, 5538.89),
        EmployeerCommissioned("Bia", 1002, 3450.6, 10, 25.45)
    ]

    for item in list_employeers:
        print(f"Salary of {item.get_name()}: R$ {item.calculate_salary()}")

    # modifying 'hours_worked' and 'value_hour' from 'EmployeerPerHour'
    list_employeers[0].set_hours_worked(100)
    list_employeers[0].set_value_hour(30.55)
    
    print(f"New salary of bricklayer: R$ {list_employeers[0].calculate_salary()}")

if __name__ == "__main__":
    process_payment()

# Execute how (git bash): python src/tasks/task12/main.py