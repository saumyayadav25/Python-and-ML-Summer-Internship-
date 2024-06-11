# QUESTION 11 : Write a python that generates the first n numbers in the Fibonacci sequence
def fib(n):
    fib_sequence = []
    if n <= 0:
        return fib_sequence
    elif n == 1:
        fib_sequence.append(0)
        return fib_sequence
    # Start the sequence with the first two numbers: 0 and 1
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    return fib_sequence
n = 10
print(f"The first {n} numbers in the Fibonacci sequence are: {fib(n)}")


# QUESTION 12 : Write a python program that calculates the sum of the digits of a given number
number = 12345
sumOfDigits=0
for digit in str(number):
    sumOfDigits += int(digit)
print("sum of digits of given number is", sumOfDigits) 


# QUESTION 13 : Write a program that asks the user for their birth year and calculates their age
import datetime
year=int(input("enter your birth year: "))
current_date = datetime.datetime.now()
current_year = current_date.year
age = current_year - year
print("Your age is: ", age)


# QUESTION 14 : Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
lines = []
while True:
    line = input("Enter the input line: ")
    if line == "":
        break  
    lines.append(line)
for line in lines:
    print(line)


# QUESTION 15 : Write a program that reads data from a CSV file and prints it to the console
with open("ques15.csv" , "r") as file:
    content = file.read()
    lines = content.split("\n")
    for line in lines:
        print(line)


# QUESTION 16 : Write a program in python that counts the frequency of each character in a string
str = "hello world"
character_freq = {}
for char in str:
    if char in character_freq:
        character_freq[char] +=1
    else:
        character_freq[char] = 1
# print(character_freq)     #output as dictionary
for char, freq in character_freq.items():
    print(f"Character '{char}' appears {freq} times.")


# QUESTION 17 : Write a program in python that converts a given string to title case(first letter of each word capitalized)
str1 = "hello everyone"
print(str1.title())


# QUESTION 18 : Write a python program that checks if two strings are anagrams of each other
def are_anagrams(str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)
word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")


# QUESTION 19 : Write a python program that removes all punctuation from a given string
punc_string = "Hello, everyone! How are you doing"
import string 
without_punc_string = ""
# print(string.punctuation)   #returns all punctuations present in string which we imported
for char in punc_string:
    if char not in string.punctuation:  
        without_punc_string += char
print(without_punc_string)


# QUESTION 20 : Write a python program that takes a list of numbers and returns their sum
list1 =[1,2,3,4,5]
sum = 0
for i in list1:
    sum += i
print(sum)