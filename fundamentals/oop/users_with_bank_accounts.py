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

class User:
    list_of_accounts = []
# do this 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(2000, .025)
        self.age = age
        User.list_of_accounts.append(self)
    # give this method below a try again (try adding .balance below to the account part; that's the lead from Michael)
    def one_year_calc(self):
        if self.account > 8000:
            one_year_total = self.account * self.account
            print(f"In the next year, you will gain {one_year_total} in US dollars.")
        elif self.account > 3000:
            one_year_total = self.account * self.account
            print(f"In the next year, you will gain {one_year_total} in US dollars.")
        elif self.account > 500:
            one_year_total = self.account * self.account
            print(f"In the next year, you will gain {one_year_total} in US dollars.")

    def make_deposit(self, num):
        self.account.deposit(num)

    def make_withdrawal(self, num):
        self.account.withdraw(num)

    def display_user_balance(self):
        self.account.display_account()

# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------

anthony_account = User("Anthony", "Manley", "maka@email.com", 36)
miho_account = User("Miho", "Irie", "miho@mihohotel.com", 36)

anthony_account.make_deposit(200)
anthony_account.make_withdrawal(2211)
anthony_account.one_year_calc()

# STILL WORKING ON SENSEI BONUS TASKS IN THE USERS WITH BANK ACCOUNTS ASSIGNMENTS. THESE ARE CURRENTLY NOT COMPLETED.