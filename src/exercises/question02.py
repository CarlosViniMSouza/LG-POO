"""
* Exercício 2: Encapsulamento 

- Objetivo: Entender e aplicar o conceito de encapsulamento, usando getters e setters para validação. 

- Enunciado: 
1. Crie uma classe ContaBancaria com os atributos privados 'saldo' e 'titular'.
2. Implemente métodos getters e setters para o atributo 'saldo', garantindo que não seja possível definir um saldo negativo.
"""

class BankAccount:
    def __init__(self, account_holder: str, bank_balance: float) -> None:
        self._account_holder = account_holder
        self._bank_balance = bank_balance

    @property
    def account_holder(self):
        return self._account_holder
    
    @property
    def bank_balance(self):
        return self._bank_balance

    @account_holder.setter
    def account_holder(self, account_holder):
        self._account_holder = account_holder
    
    @bank_balance.setter
    def bank_balance(self, bank_balance: float) -> None:
        self._bank_balance = bank_balance

myAccount = BankAccount("Current Account", 3135.65)

print(f"Your \"{myAccount.account_holder}\" have R$ {myAccount.bank_balance} deposited!")