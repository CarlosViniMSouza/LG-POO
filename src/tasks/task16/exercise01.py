## Exercicio 01

class InsufficientBalanceError(Exception):
    # Lançada ao tentar sacar um valor superior ao saldo disponível.
    pass

class LimitExceededError(Exception):
    # Lançada ao tentar transferir um valor que ultrapassa o limite da conta.
    pass

class InvalidDestinationAccountError(Exception):
    # Lançada ao tentar transferir para uma conta inexistente.
    pass

class Account:
    def __init__(self, account_holder: str, balance: float, limit: float) -> None:        
        self.account_holder = account_holder
        self.balance = balance
        self.limit = limit

    def deposit(self, amount_deposited: float) -> str:
        self.balance += amount_deposited

        return f"Deposit Made: R$ {amount_deposited}"

    def withdraw(self, amount_withdrawn: float) -> str:
        try:           
            if amount_withdrawn > self.balance:
                raise InsufficientBalanceError(f"Amount to be withdrawn (R$ {amount_withdrawn}) greater than the current amount (R$ {self.balance})")
            else:
                self.balance -= amount_withdrawn
                return f"Amount after withdrawal: R$ {self.balance}"

        except Exception as exc:
            return exc
        
    def transfer(self, amount_transferred: float, destination_account) -> str:
        if not isinstance(destination_account, Account): 
            raise InvalidDestinationAccountError("Conta de destino inválida.") 
        if amount_transferred > self.limit: 
            raise LimitExceededError("Valor ultrapassa o limite da conta.") 
        if amount_transferred > self.balance: 
            raise InsufficientBalanceError("Saldo insuficiente para realizar a transferência.") 
        
        self.balance -= amount_transferred 
        destination_account.deposit(amount_transferred) 
        
        return f"Transferência realizada: {amount_transferred}. Saldo atual: {self.balance}"

def create_transactions():
    # Exemplo de uso com bloco try-except 
    try: 
        source_account = Account("Alice", 1000, 500) 
        destination_account = Account("Bob", 500, 300) 
        
        print(source_account.deposit(200)) 
        print(source_account.withdraw(50))
        print(source_account.transfer(700, destination_account))
    
    except InsufficientBalanceError as err:
        print(f"Erro: {err}")
    except LimitExceededError as err:
        print(f"Erro: {err}")
    except InvalidDestinationAccountError as err:
        print(f"Erro: {err}")