from BankAccount import BankAccount

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name, self.account.balance)

    def transfer_money(self, self2, amount):
        self2.account.balance+=amount
        self.account.balance-=amount



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Adam = User("Adam Ahmed", "adam@python.com")


guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(200)

monty.make_deposit(300).make_deposit(400).make_withdrawal(300).make_withdrawal(500)

Adam.make_deposit(9000).make_withdrawal(300).make_withdrawal(500).make_withdrawal(500)

guido.transfer_money(Adam,300)


guido.display_user_balance()
monty.display_user_balance()
Adam.display_user_balance()
