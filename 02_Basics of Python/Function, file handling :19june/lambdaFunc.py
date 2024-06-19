# Lambda Functions: Anonymous Functions-> small user-defined function codes that do not have a name
# We don't use def keyword to create lambda functions, rather we use lambda keyword and colon: operator
'''
Syntax:
variable=lambda argument(s): expression statements or calculations
To call lambda functiion:
variable()
'''
# Use lambda function for printing a message
message = lambda : print("Hello user!! This is first message")
# calling a lambda function
message()

# Use arguments in lambda function
message = lambda username : print(f"Hello user {username}!! This is first message")
# calling a lambda function
user=input("Enter your username: ")
message(user)

# Join lambda function with map() and filter() methods
# From a list of numbers we want to filter out only odd numbers and create a new list from it
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Syntax for filter method-> filter(any function to be used as filter ex. lambda, iterable)
odd_list = list(filter(lambda num: (num%2 != 0),list1))
print("the new odd list created is: ", odd_list)

even_list=list(filter(lambda num : (num%2==0),list1))
print("the new even list created is: ", even_list)

# Result of max between two numbers num1 and num2
result=lambda num1,num2: num1 if (num1>num2) else num2
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
print("the maximum number is", result(num1,num2))

# Check for age>=60 in a list and filter out those employees in a separate list
ages_list=[23,56,67,68,34,89,78,44,90,79,66,69]
senior_ages_list = list(filter(lambda ageval: ageval>=60,ages_list))
print("The separate senior list values:", senior_ages_list)

# map()->helps to apply a lambda function's calculation mapped to each element of iterable
# Syntax: map(lambda.., iterable)

list_salary=[1000,2400,4500,1100,1000,7800,3600]
# Add bonus of 500 Rs to all salaries and create a bonus list 
bonus_list=list(map(lambda sal: sal+500, list_salary))
print("After adding bonus, the salary list is: ", bonus_list)

list_emp=['Ajay','reema','riTu','sima','ramaN']
proc_list_emp=list(map(lambda emp: emp.upper(), list_emp))
print("the processed list:", proc_list_emp)