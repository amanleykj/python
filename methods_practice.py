class Player:

    def __init__ (self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

def getPlayerDeets(self):
    print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.password}')
    return(self)

anthony = Player('anthony', 'manley', 'anthony@anthonybutt.com', 'ilikewhiskey')
miho = Player('miho', 'irie', 'miho@mihoface.com', 'ilikebeery')

anthony.getPlayersDeets()
miho.getPlayerDeets()