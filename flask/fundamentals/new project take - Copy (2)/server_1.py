class BankAccount:

    def __init__(self, balance, int_rate):

        self.balance = balance
        self.int_rate = int_rate
        self.isMember = False

    def deposit(self, amount):

        self.balance += amount
        print("$" + str(self.balance))
        return self

    def display_account(self):

        print("Account Balance: ")
        print("$" + str(self.balance))
        print("Interest Rate: ")
        print(str(self.int_rate) + "%")
        return self

    def yield_interest(self):

        earned_amount = self.int_rate * self.balance
        self.balance = self.balance + earned_amount
        print(f"You have earned ${earned_amount} in interest.")
        print(f"Your new total is ${self.balance}")
        return self

    def withdraw(self, amount):

        if (self.balance - amount) < 0:
            print(f"You cannot make a withdrawal of ${amount} due to insufficient funds.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal for ${amount} complete. Your new account balance is ${self.balance}.")
        return self


class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(balance=0, int_rate=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account()
        print("First Name: ")
        print(self.first_name)
        print("Last Name: ")
        print(self.last_name)
    
    def standard_upgrade(self):
        self.account.int_rate = BankAccount.standard
        return