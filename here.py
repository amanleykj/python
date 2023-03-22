class Player:

    def __init__ (self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def showUser(self):
        if self.min_in_Oven > 10:
            if self.min_in_Oven > 30:
                print("Your cookie is burnt, bro.")
            else:
                print("Cookie is cooked, fully.")
        else:
            print("Cookie isn't quite done yet.")
        return self

print()