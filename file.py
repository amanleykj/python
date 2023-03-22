num1 = 42 # variable declaration; data type-primitive-number; comment (single line)
num2 = 2.3 # variable declaration; data type-primitive-number; comment (single line)
boolean = True # variable declaration; data type-primitive-boolean; comment (single line) last occurence of "comment" comment
string = 'Hello World' # variable declaration; data type-primitive-string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
"""
list initialize 
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
"""
dictionary initialize
"""
fruit = ('blueberry', 'strawberry', 'banana')
"""
tuple initialize
"""

print(type(fruit)) # tuple type check
print(pizza_toppings[1]) # list access value
pizza_toppings.append('Mushrooms') # # list add value
print(person['name']) # dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary change value
print(fruit[2]) # tuple access value

if num1 > 45: # conditional if
    print("It's greater")
else: # conditional else
    print("It's lower")

if len(string) < 5: # conditional if
    print("It's a short word!")
elif len(string) > 15: # conditional else if
    print("It's a long word!")
else: # conditional else
    print("Just right!")

for x in range(5): # for loop start
    print(x)
for x in range(2,5): # for loop 
    print(x)
for x in range(2,10,3): # for loop
    print(x)
x = 0 # variable declaration
while(x < 5): # while loop start
    print(x)
    x += 1 # while loop start

pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list delete value

print(person)
person.pop('eye_color') # dictionary delete value
print(person)

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement')
    if topping == 'Olives': # conditional if 
        break # for loop break

def print_hello_ten_times(): # function parameter
    for num in range(10): # function argument
        print('Hello') # function return

print_hello_ten_times() # function return

def print_hello_x_times(x): # function parameter
    for num in range(x): # function argument
        print('Hello') # function return

print_hello_x_times(4) # function return

def print_hello_x_or_ten_times(x = 10): # function parameter
    for num in range(x): # function argument
        print('Hello') # function return

print_hello_x_or_ten_times() # function return
print_hello_x_or_ten_times(4) # function return


"""
Bonus section
"""

print(num3) # NameError: name <variable name> is not defined
num3 = 72 # if this variable is defined after the above print statement, it will never print (and show the error above)
# and the num3 variable will - as it's currently written/positioned - never appear
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) #IndexError: list index out of range
print(boolean) #
fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'