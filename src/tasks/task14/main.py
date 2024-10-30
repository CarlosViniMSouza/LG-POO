from controller import *

def main():
    """
    SalesHistoric.add_product_to_list("T-shirt", 10, 100.5)
    SalesHistoric.add_product_to_list("Jeans", 20, 90)
    SalesHistoric.add_product_to_list("Bag", 30, 60.5)

    SalesHistoric.get_list_sales()

    print(f"Total sales: R$ {SalesHistoric.total_per_product()}")
    print(f"Sales above R$70: {SalesHistoric.list_sales_above(70)}")
    """

    """
    user_manager = Employee("Alice", "Manager", 5000)
    user_employee01 = Employee("Bob", "Cleaner", 1000)
    user_employee02 = Employee("John", "Receptionist", 2000)

    hrsystem = HRSystem()
    hrsystem.add_employee(user_manager)
    hrsystem.add_employee(user_employee01)
    hrsystem.add_employee(user_employee02)

    hrsystem.increase_salary(user=user_manager, name_employee="Bob", increment=500)
    hrsystem.increase_salary(user=user_manager, name_employee="John", increment=300)
    """

    """
    account = Account()
    account.add_transaction('Deposit', 1500)
    account.add_transaction('Withdrawal', 300)
    account.add_transaction('Withdrawal', 150)
    account.add_transaction('Deposit', 1200)

    withdrawals = account.filter_transactions_por_type('Withdrawal')
    print("Withdrawal Transactions:", withdrawals)

    account.apply_fee(60)
    print("Transactions after application of fee:", account.transactions)
    """

if __name__ == "__main__":
    main()