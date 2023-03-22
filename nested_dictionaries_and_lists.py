
#1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

(x[1][0]) = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

#2 Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for i in range(0, len(list)):
        string_make = ""
        for key,val in list[i].items():
            string_make += f" {key} - {val},"
        print(string_make)

iterate_dictionary(students)

#3 Get Values from a List of Dictionaries

# I researched this method online and it seems to be a good method to handle this task

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(key, list):
    list_comp_method = [ sub[key] for sub in list]
    for i in list_comp_method:
        print(i)

iterateDictionary('last_name', students)

#4 Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# get length of list within dict
# on the same line, print the key name in all capital letters
# print the different indexes of the above list on separate lines

def printInfo(dict):
    print(len(dict['locations']))
    print("LOCATIONS")
    for i in dict["locations"]:
        print(i)

    print(len(dict['instructors']))
    print("INSTRUCTORS")
    for i in dict["instructors"]:
        print(i)

printInfo(dojo)