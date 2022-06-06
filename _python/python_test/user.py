class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, self2, amount):
        self2.account_balance+=amount
        self.account_balance-=amount



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Adam = User("Adam Ahmed", "adam@python.com")


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(200)

monty.make_deposit(300)
monty.make_deposit(400)
monty.make_withdrawal(300)
monty.make_withdrawal(500)

Adam.make_deposit(9000)
Adam.make_withdrawal(300)
Adam.make_withdrawal(500)
Adam.make_withdrawal(500)

guido.transfer_money(Adam,300)


guido.display_user_balance()
monty.display_user_balance()
Adam.display_user_balance()
