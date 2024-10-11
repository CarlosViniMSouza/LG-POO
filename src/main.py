class Account:
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

    def showInfos(self):
        return f"Your infos: \
            \nNumber account: {self.number} \
            \nTotal amount: R${self.amount}"


if __name__ == "__main__":
    accountNumber = 123456
    accountAmount = 1000

    userAccount = Account(accountNumber, accountAmount)
    print(userAccount.showInfos())
