class Cookie:

    def __init__(self, shape, size, thisType, inOven, ingredients=[]):

# attributes
        self.shape=shape
        self.size=size
        self.type=thisType
        self.min_in_Oven=inOven
        self.ingredients=[]

# methods (functions are a method of class)
    def isCooked(self):
        if self.min_in_Oven > 10:
            if self.min_in_Oven > 30:
                print("Your cookie is burnt, bro.")
            else:
                print("Cookie is cooked, fully.")
        else:
            print("Cookie isn't quite done yet.")
        return self
    
    def getType(self):
        this_string = f"This Cookie type is: {self.type}"
        print(this_string)
        return self

    def getShape(self):
        this_string = f"This Cookie shape is {self.shape}"
        print(this_string)
        return self

class Player:

    def __init__ (self, powerlevel, power_ups, strength, stamina, name, ):
        self.powerlevel = powerlevel
        self.power_ups = power_ups
        self.strength = strength
        self.stamina = stamina
        self.name = name

    def set_power_level(self, power):
        self.power_level = self.power_level + power
        return self




new_player = Player(100, ["Jump a lot"], 100, 80, "Prise")
