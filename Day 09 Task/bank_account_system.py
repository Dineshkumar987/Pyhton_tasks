class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)


b = BankAccount(12345, 1000)
b.deposit(500)
b.withdraw(300)
b.display() 