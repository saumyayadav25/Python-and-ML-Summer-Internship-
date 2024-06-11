# QUESTION 1 : Write a program that takes two numbers as input and prints their sum 
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2
print(sum)


# QUESTION 2 : Write a python program that checks whether a given number is even or odd
num = int(input("enter the number you want to check: "))
if(num%2==0):
    print(num, "is even")
else:
    print(num, "is odd")


# QUESTION 3 : Write a python program that calculates the factorial of a given number
def fact(n):
    if n < 0:
        return "Please give positive numbers"
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
number = int(input("Enter number to calculate the factorial: "))
print(f"The factorial of {number} is: {fact(number)}")


# QUESTION 4 : Write a program that asks the user for their name and then prints a greeting message
name=input("enter your name: ")
print(f"hello {name} , welcome to this repository! ")


# QUESTION 5 : Write a program that takes a string input from the user and write it to a text file
usr = input("Enter a string to write to a text file: ")
with open("ques5.txt", "w") as file:
    file.write(usr)
print("The string has been written to 'ques5.txt'.")


# QUESTION 6 : Write a program that reads the content of a text file and prints it to the console
with open("ques5.txt" , "r") as file:
    content = file.read()
print(content)


# QUESTION 7 : Write a python program that takes a string as input and returns its length
str = input("enter a string input: ")
print("length of string input is",len(str))


# QUESTION 8 : Write a python program that concatenates two strings and returns the result
str1 = "hello "
str2 = "world"
result = str1 + str2
print(result)


# QUESTION 9 : Write a python program that checks if a substring is present in a given string
s1="hello everyone welcome to this repository"
print("repo" in s1)


# QUESTION 10 : Write a python program that converts a given string to uppercase
s2="welcome to this repository"
print(s2.upper())