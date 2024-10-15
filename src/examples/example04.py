"""
Pages: 23, 24
Image: 04, 05
"""

class BankAccount:
    interest_rate = 0.02

    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    def deposit(self, value):
        if value > 0:
            self.__balance += value
            print(f"Deposit of R${value:.2f} made successfully!")
        else:
            print(f"Value should be positive!")

    def withdraw(self, value):
        if value > 0 and value <= self.__balance:
            self.__balance -= value
            print(f"Withdraw of R${value:.2f} made successfully!")
        else:
            print("Insufficient balance or Value invalidated!")

    def show_balance(self):
        print(f"Balance from {self.__holder}: R${self.__balance:.2f}")

    @classmethod
    def interest_bearing_account(cls, holder, initial_balance):
        interest_bearing_balance = initial_balance * (1 + cls.interest_rate)

        return cls(holder, interest_bearing_balance)
    
account01 = BankAccount("Carlos", 1500)
account02 = BankAccount.interest_bearing_account("Vinicius", 1000)

print("\nAccount 01\n")

account01.show_balance()
account01.deposit(300)
account01.withdraw(450)
account01.show_balance()

print("\nAccount 02\n")

account02.show_balance()
account02.deposit(250)
account02.withdraw(550)
account02.show_balance()