# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"},
    {"first": "Alan", "last": "Turing"},
    {"first": "Eric", "last": "Idle"}
]
# Dictionary of lists # below won't actually be on the exam
resume_data = {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies":["rock climbing", "knitting"]
}

for i in resume_data:
    # print(resume_data[i]) # this is a list; treat it like that
    for k in resume_data[i]:
        print(k)



    #    break
# personal challenge: get each value of list first (front-end, Python, rock climbing, back-end, ...)
# print(my_dict["this"])
# peeling back each section
# **** pulling back a list of dictionaries from DB (exam)
# 11 to 8pm

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Phoenix Suns"
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
    "team": "Dallas Mavericks"
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

