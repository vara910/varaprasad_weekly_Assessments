class Payment:
    def process_payment(self, amount):
        return f"Processing payment of {amount}"

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Bitcoin payment of {amount}"

credit = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = BitcoinPayment()
print(credit.process_payment(5000))
print(paypal.process_payment(3000))
print(bitcoin.process_payment(7000))
