from abc import ABC, abstractclassmethod

class Payment(ABC):
    @abstractclassmethod
    def process_payment(self):
        pass

    def details_payment(self, method):
        print(f"Processing payment way {method}!")
    
class PaymentCard(Payment):
    def process_payment(self):
        print(f"Payment processed with card!")

class PaymentBillet(Payment):
    def process_payment(self):
        print(f"Payment processed with billet!")

def test_payment():
    payment_card = PaymentCard()
    payment_billet = PaymentBillet()

    print("\nPayment with card:")
    payment_card.details_payment(method="card")
    payment_card.process_payment()

    print("\nPayment with billet:")
    payment_billet.details_payment(method="billet")
    payment_billet.process_payment()

if __name__ == "__main__":
    test_payment()

"""
IF YOU DON'T IMPLEMENT THE ABSTRACT CLASS:

TypeError: Can't instantiate abstract class PaymentCard without an implementation for abstract method 'process_payment'
"""