class Player:
    def __init__(self, data, int):
        self.name = data[int]["name"]
        self.age = data[int]["age"]
        self.position = data[int]["position"]
        self.team = data[int]["team"]

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

player_kevin = Player(players, 0)
player_jason = Player(players, 1)
player_kyrie = Player(players, 2)
player_damian = Player(players, 3)
player_joel = Player(players, 4)

player_joel.print_deets()


# player_kevin = Player(kevin)
# player_jason = Player(players[0][""])

# print(player_jason.print_deets)

# player_kevin.print_deets()


# for key,value in kevin.items():
#     print(key + " " + value)