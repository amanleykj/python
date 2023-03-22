class User:		
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
# #1 look at how print format works
# #2 then, look at how dictionaries are created
# #3 give it the key/values I want
# #4 then, print dictionaries --- this method is within the above method;
# later creating an all_users 

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points <= 0:
            print("No points to spend")
        elif self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
            return self

    def greeting(self):
        print(f"Hello, my name is {self.first_name}.")

user_anthony = User("Anthony", "Manley", "maka@maka.com", 36)

# user_anthony.display_info()

user_anthony.enroll()

user_miho = User("Miho", "Irie", "miho@irie.com", 36)
user_lindsay = User("Lindsay", "Peterson", "han@hanzy.com", 40)

user_anthony.display_info()
#  gives the "address" of where user_anthony is stored

user_anthony.spend_points(50).display_info()
user_miho.enroll().spend_points(80).display_info()

# user_lindsay.display_info()