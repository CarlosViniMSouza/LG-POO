class Account:
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

    def showInfos(self) -> int:
        return f"Your infos: \
            \nNumber account: {self.number} \
            \nTotal amount: R${self.amount}"


class People:
    number_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        People.number_people += 1

    @classmethod
    def total_peoples(cls) -> None:
        print(f"Total calculated: {cls.number_people}")


class BankAccount:
    def __init__(self, title, balance):
        self.title = title
        self._balance = balance

    def deposit(self, value):
        self._balance += value

        return self._balance

    def withdraw(self, value):
        print(f"Taking out: {value}")

        if value <= self._balance:
            self._balance -= value

            return self._balance
        else:
            print("Insufficient Balance")

    def show_balance(self):
        return self._balance

if __name__ == "__main__":
    #accountNumber = 123456
    #accountAmount = 1000

    #userAccount = Account(accountNumber, accountAmount)
    #print(userAccount.showInfos())

    #people1 = People("Carlos", 22)
    #people2 = People("Souza", 23)

    #People.total_peoples()

    myAccount = BankAccount("Current", 1000)
    print(f"Depositing: R${myAccount.deposit(500)}") # Depositando
    myAccount.withdraw(5000) # Sacando
    print(f"Remaining: R${myAccount.show_balance()}") # Restando

    print(BankAccount._balance)