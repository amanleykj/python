#1 Countdown
def countdown(num):
    num_list = []
    for i in range(num,-1,-1):
        num_list.append(i)
    return(num_list)
    
print(countdown(10))

#2 Print and Return
def print_and_return(a,b):
    num_list = [a,b]
    print("Give me a first number: ")
    a = input()
    print("Now, give me a second number: ")
    b = input()
    num_list = [a,b]
    print(num_list[0])
    print(num_list[1])

print_and_return(3,5)

#First Plus Length
def first_plus_length(a,b,c,d,e):
    num_list = []
    num_list.append(a)
    num_list.append(b)
    num_list.append(c)
    num_list.append(d)
    num_list.append(e)
    task_result = len(num_list) + num_list[0]
    print(task_result)

first_plus_length(7,9,13,233,245)

#Values Greater Than Second
def values_greater_than_second(a,b,c,d,e):
    list = []
    new_list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    list.append(e)
    if list[2] == False:
        print("False")
        return
    else:
        for i in list:
            if i > list[1]:
                new_list.append(i)
    print("The length of this list is: ")
    print(len(new_list))
    return(new_list)

values_greater_than_second(2,4,5,7,15)

#This Length, That Value
def length_and_value(size,value):
    end_result = []
    for i in range(0, size):
        end_result.append(value)
    return(end_result)

print(length_and_value(5,3))
print(length_and_value(6,10))