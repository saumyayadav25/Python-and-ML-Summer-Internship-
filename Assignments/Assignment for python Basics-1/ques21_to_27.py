# QUESTION 21 : Write a python program that counts the occurrences of a specific element
def count_occurrences(list1, element):
    count = 0
    for i in list1:
        if i == element:
            count += 1
    return count
numbers = [10,20,30,40,10,20,100,10]
element = 10
occ = count_occurrences(numbers, element)
print(f"The element {element} occurs {occ} times in the list.")


# QUESTION 22 : Write a python program that returns the minimum and maximum values in a list of numbers
list1 = [-1,4,2,10,72,34]
print("minimum value in list:", min(list1) , "maximum value in list:", max(list1))


# QUESTION 23 : Write a program that converts the temperature from Celsius to Fahrenheit and vice versa based on user input
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit:.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:.2f}°C")
else:
    print("Invalid choice")


# QUESTION 24 : Write a program that acts as a simple calculator. It should take two numbers and an operator(+,-,*,/) as input and print the result
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print("1. + \n2. - \n3. * \n4. /")
choice = input("which operation do you want to perform (1-4) ")
if choice == '1':
    print(num1+num2)
elif choice == '2':
    print(num1-num2)
elif choice == '3':
    print(num1*num2)
elif choice == '4':
    if num2 == 0:
        print("please give valid denominator")
    else:
        print(num1/num2)
else:
    print("choose valid operation")


# QUESTION 25 : Write a program that copies the contents of one text file to another
with open("ques5.txt", "r") as source_file:
    content = source_file.read()
with open("ques25.txt", "w") as destination_file:
    destination_file.write(content)
print("Contents of 'ques5.txt' have been copied to 'ques25.txt'.")


# QUESTION 26 : Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
str="hello eveyone, welcome to coding space"
prefix = "hello"
print(str.startswith(prefix))
print(str.endswith('ace'))


# QUESTION 27 : Write a program in python that converts a string into a list of its characters
str1 = "hello"
char_list = list(str1)
print(char_list)