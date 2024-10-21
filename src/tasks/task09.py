class Payment:
    def process_payment(self) -> None:
        pass
    
class PaymentCreditCard(Payment):
    def __init__(self, number_card: int) -> None:
        self.number_card = number_card

    def process_payment(self) -> None:
        print(f"Payment Credit Card\n From Number Card: {self.number_card}\n Status: Processed Successfully!\n")
    
class PaymentBillet(Payment):
    def __init__(self, code_billet: int) -> None:
        self.code_billet = code_billet

    def process_payment(self) -> None:
        print(f"Payment Billet\n From Billet: {self.code_billet}\n Status: Processed Successfully!\n")

class PaymentPix(Payment):
    def __init__(self, pix_key: int) -> None:
        self.pix_key = pix_key

    def process_payment(self) -> None:
        print(f"Payment Pix\n From Pix Key: {self.pix_key}\n Status: Processed Successfully!\n")
    
def process_payment(payment: Payment) -> None:
    payment.process_payment()

payment_credit_card = PaymentCreditCard(123)
payment_billet = PaymentBillet(123456)
payment_pix = PaymentPix(123456789)

process_payment(payment_credit_card)
process_payment(payment_billet)
process_payment(payment_pix)