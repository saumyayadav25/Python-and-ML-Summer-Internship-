value = input("enter the value:")
print(value)
print(type(value)) #by default input() function will only take string values

#typecasting
value2 = int(input("enter the int value:"))
print(value2)
print(type(value2))

print(1,2,3,4,sep="#")

# samplefile is a file object opened for writing
samplefile = open('/Users/Desktop/Python and ML Internship/Basics Of Python/demo.txt', 'w')
print(1,2,3,4,sep="%", file = samplefile)

str=int(input("enter the number of audience in class to greet "))
print("Hello all {} people in class".format(str))

str1 = "hello "
str2 = "welcome"
str3 = str1 + str2
print(str3)
i = 10
j = 20
print(i+j)

#datatypes
num1 = 10
print("the num is :", num1, "The type is: ", type(num1))
num1 = 10.12
print("the num is :", num1, "The type is: ", type(num1))
num1 = 10+5j
print("the num is :", num1, "The type is: ", type(num1))

# number systems
# binary base 2: for using binary numbers-> prefix 0b or 0B
print(0b101)
print(0B1011)
# octal base 8: for using octal numbers-> prefix 0o or 0O
print(0o156)
# hexadecimal : prefix 0x or 0X
print(0xAFB)

# typecasting in numbers is implicit
# implicit: smaller data can be converted to bigger datatype automatically
print(100 + 15.67)
# explicit: convert a bigger data into smaller data forcefully
num1 = int(15.77)
print(num1)
val = int(-55.88)
print(val)
val1 = complex("10+3j")
print(val1)

# number based modules: random and math modules
# RANDOM MODULE
import random
print(random.randrange(20,50))
print(random.random())
#use random to pick a value randomly from any sequence
list1 =["Hello", "How", "are", "you"]
print(random.choice(list1)) 
random.shuffle(list1)
print(list1)

# MATH MODULE
# Aliases: nick-names
import math as mt #mt is alias name for math
print(mt.factorial(5))
print(mt.pi)
print(mt.log10(1000000))
print(mt.pow(2,3)) #2^3

# sequence data->list, string and tuple
#LIST: very flexible sequence of data as it allows all sorts if modifications
# Characteristics of list: ordered by position, mutable, duplicate values are allowed
list1 = [1,2,3,"Hello", 'hi', 12.22, True]
print("First element of list1: ",list1[0])
print("Last element of list1: ",list1[-1])

# TUPLE: immutable
tup1=("Hello",1,2,3,'bye', True, 12.77)
print("First element of tup1: ",tup1[0])
print("Last element of tup1: ",tup1[-1])

list1[-1]='False'
print(list1)

# Collections type data that do not have any index or position: dictionary and set
# DICTIONARY
dict1={'Name': "Saumya", "Age": 19, "Marks": 19} #keys must be unique, values can be duplicate
print(dict1["Age"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["Age"] = 20
dict1["degree"]="B.tech"
print(dict1)

#SET: has no duplicate elements, unordered
set1={1,2,3,3,1,1,3,4,5,5,"Hello",7}
print(set1)
