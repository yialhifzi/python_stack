class BankAccount:
    def __init__(self, int_rate=1, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Interest rate is",self.int_rate,"%.", " Balance after interest yield is",self.balance)

    def yield_interest(self):
        self.balance *= (1+(self.int_rate/100))
        return self

acc1=BankAccount(2)
acc2=BankAccount(4)

acc1.deposit(100).deposit(100).deposit(50).withdraw(200).yield_interest().display_account_info()
acc2.deposit(1000).deposit(100).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
