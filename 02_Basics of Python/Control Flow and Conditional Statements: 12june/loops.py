# FOR LOOP
list1=[1,2,3,'hello',11.44,True,3+5j]
for i in list1:
    print(i)

# range()->it generates numbers in a given range
# syntax: range(start,stop,steps) by default start from 0, need to give stop value it's mandatory
values=range(10) #a stop parameter is given-> 0 to 9
list1=list(values)
print(list1)
for i in range(1,10,2):
    print(i+1)

for i in range(5,-5,-1):
    print(i)

# for loop with else
list1=['ajay','raman','mona','sita']
count = 0
for i in list1:
    print("the name of employe:", i)
    count=count+1
else:
    print("the total number of employees in company:", count)

list1=[1,2,3,4]
for _ in list1:
    print("loop working success!!")

# nested for loop
for i in range(5):
    for j in range(2):
        print("the value of i:", i, "value of j:",j)


# WHILE LOOP
# check if the user has entered correct password for login, else the user is asked to retry again
# the user can try infinite times
while True:
    user_name=input("enter your username:")
    password_input=input("enter your password:")
    if password_input=="Password":
        print(user_name, "!!Welcome to the website")
        break
    elif password_input=="Quit":
        print("You are exiting the system!")
        break
    else:
        print("either username or password is incorrect")

# calculate the sum of numbers till user enters 'Quit'
first_number = int(input("enter a number:"))
choice = input("you want to continue? type yes. else type Quit:")
sum = first_number
# taking input of other values to add to the number or enter 'Quit'
while True:
    if choice=='Quit':
        print("exiting the system")
        break
    elif choice.upper()=="YES":
        next_number=int(input("enter other number to add:"))
        sum = sum + next_number
        print("the sum is:", sum)
        choice=input("you want to continue? type yes. else type Quit:")
    else:
        print("enter valid choice")
        choice=input("you want to continue? type yes. else type Quit:")

# FLOW CONTROL STATEMENTS
# BREAK
for i in range(10):
    if i==6:
        print("limit to 6 reached!!")
        break
    print(i)
else:
    print("the loop has ended")

# CONTINUE
for i in range(10):
    if i==6:
        print("limit to 6 reached!!")
        continue
    print(i)
else:
    print("the loop has ended")

# PASS
for i in range(10):
    if i==7:
        print("limit to 7 reached!!")
        break
    elif i==5:
        print("limit to 5 reached!! Warning")
        pass
    print(i)
else:
    print("the loop has ended")


list1=['ajay','raman','mona','priya','manan']
salary=1000
# no appraisal for priya
for i in list1:
    if i=='priya':
        continue
    elif i=='ajay' or i=='manan':
        print("user!!", i)
    else:
        pass