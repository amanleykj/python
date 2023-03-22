"""
#Basic
for i in range(151):
    print(i)

#Multiples of Five
for i in range(5, 151, 5):
    print(i)

#Counting, the Dojo Way
for i in range(1, 100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
"""
#Woah, That Sucker's Huge
odd_numbers_range = 5000
odd_numbers_total = []

for i in range(1, odd_numbers_range+1):
        if i % 2 == 1 and i < odd_numbers_range:
            odd_numbers_total.append(i)
        else:
            print(sum(odd_numbers_total))

"""
#Countdown by Fours
start_number = 2022

for i in range(start_number):
    if start_number > 0:
        start_number = start_number - 4
        if start_number <= 0:
            break
        else:
            print(start_number)

#Flexible Counter
lowNum = 13
highNum = 125
mult = 7
mult_list = []

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        mult_list.append(i)

for x in range(len(mult_list)):
    print(mult_list[x])
"""