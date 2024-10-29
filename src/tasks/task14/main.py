from controller import *

def main():
    sale01 = SalesHistoric.add_product_to_list("T-shirt", 10, 100.5)
    sale02 = SalesHistoric.add_product_to_list("Jeans", 20, 90)
    sale03 = SalesHistoric.add_product_to_list("Bag", 30, 60.5)

    SalesHistoric.get_list_sales()

    print(f"\nTotal sales: R$ {SalesHistoric.total_per_product()}")

    print(f"\nSales above R$70: {SalesHistoric.list_sales_above(70)}")

if __name__ == "__main__":
    main()