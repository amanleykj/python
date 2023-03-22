# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name():
    print("What is your first name?")
    name1 = input()
    print("It's good to meet you, " + name1)
    print("How about your last name?")
    name2 = input()
    tot_name = name1 + name2
    print("It's good to know your full name, " + tot_name)
    return name1
    return name2
    return tot_name

full_name()


"""
print('Enter your first name:')
first_name = input()
print('Hello, ' + first_name)
print('What about your last name?')
last_name = input()
full_name = first_name + last_name
print("So, your full name is " + full_name". Is this correct?")

answer = input()
    if answer == "Yes":
        print("Great! Good to meet you, " + full_name)
    else:
        print("We fucked this one up. Sorry.")
"""
# Challenge 2: 
#   Call the function again using your own name and print the results!