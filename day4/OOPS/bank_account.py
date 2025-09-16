class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amt):
        self.balance += amt
        
    def withdraw(self, amt):
        if self.balance > 0 and self.balance >= amt:
            self.balance -= amt
            return amt
        else:
            return None
    
    
acc = BankAccount(5000)
print(f'Available balance: {acc.balance}')
acc.deposit(200)
print(f'Available balance: {acc.balance}')
print(f'Withdraw amount: {acc.withdraw(3000)}')
        