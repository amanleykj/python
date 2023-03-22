class BankAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your account now has ${self.balance} in it.")
        return self
    
    def withdraw (self, amount):
        penalty_fee = 5
        if self.balance - amount < 0:
            self.balance = self.balance - penalty_fee
            print(f"Insufficient funds. Charging a ${penalty_fee} fee. Your account now has ${self.balance} in it.")
            return self
        else:
            self.balance = self.balance - amount
            print(f"Your account now has ${self.balance} in it.")
            return self

    def display_account(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.int_rate*self.balance) + self.balance
            print(f"Your account has accrued interest at a {self.int_rate}% rate. Your new balance is {self.balance}. Nice.")
            return self
        else:
            print(f"Your account will not accrue interest because you only have {self.balance} in your account.")
            return self

    def print_all(self):
        print(f"Your account balance is {self.balance}. Your current interest rate is {self.int_rate}%. ")
        return self

account1 = BankAccount(5000, .025)
account2 = BankAccount(100, .012)

account1.deposit(2000).deposit(1400).deposit(2400).withdraw(5000).yield_interest().display_account()
account2.deposit(2400).deposit(5400).withdraw(5000).withdraw(200).withdraw(120).withdraw(100).yield_interest().display_account()