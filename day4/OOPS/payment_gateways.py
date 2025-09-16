class Payment:
    def pay(self,amt):
        pass

class CashPayment(Payment):
    def pay(self,amt):
        print(f"Paid Rs.{amt} in cash")

class CardPayment(Payment):
    def pay(self,amt):
        print(f"Paid Rs.{amt} using credit/debit")

class UPIPayment(Payment):
    def pay(self,amt):
        print(f"Paid {amt} using UPI")


Payments = [CashPayment(),CardPayment(),UPIPayment()]

for p in Payments:
    p.pay(2000)