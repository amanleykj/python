# Challenge 1
"""
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def print_deets(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
	"team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

player_kevin = Player(players)
player_jason = Player(players)
player_kyrie = Player(players)
player_damian = Player(players)
player_joel = Player(players)

player_joel.print_deets()
"""

# Challenge 2
"""
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def print_deets(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "point guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.print_deets()
player_jason.print_deets()
player_kyrie.print_deets()


# Challenge 3
"""
class Player:
    #new_team = [] this was unncessary

    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    @classmethod
    def create_team(cls, players):
        new_team = []
        for playa in players:
            new_team.append(cls(playa))
        return new_team

# above is a factory pattern, which is used to create
# decorator method makes the function above runnable without creating an instance of an object.
# factory pattern is what's creating multiple of the above (observer pattern is another)
# other programming languages create two methods

    def print_deets(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
	"team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    }
]

player_list = Player.create_team(players)
print(len(player_list))

player_list[2].print_deets()

# player_kevin = Player(players[0])
# player_jason = Player(players[1])
# player_kyrie = Player(players[2])
# player_damian = Player(players[3])