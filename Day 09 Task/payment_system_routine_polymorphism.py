class Payment:
    def process_payment(self):
        print("Processing Payment")


class CreditCard(Payment):
    def process_payment(self):
        print("Payment through Credit Card")


class UPI(Payment):
    def process_payment(self):
        print("Payment through UPI")


class NetBanking(Payment):
    def process_payment(self):
        print("Payment through Net Banking")


payments = [CreditCard(), UPI(), NetBanking()]

for p in payments:
    p.process_payment()