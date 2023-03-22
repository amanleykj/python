# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Anthony"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +

# 3. print "Hello 42!" with the number in a variable
number = 31
print("Hello", number)	# with a comma
number = (str)(number)
print("Hello " + number)	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "뼈해장국"
fave_food2 = "ほうとう"
country1 = "Korea"
country2 = "Japan"
print("I love to eat {} and {}. These foods are from {} and {}, respectively.".format(fave_food1, fave_food2, country1, country2))
# print( your code here ) # with an f string
print(f"I love to eat {fave_food1} and {fave_food2}. These foods are from {country1} and {country2}, respectively.")