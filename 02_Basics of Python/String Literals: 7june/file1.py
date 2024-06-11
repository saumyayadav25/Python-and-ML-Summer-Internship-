# SINGLE-LINE STRINGS
str1 = 'Hello' #can use single or double quotes
print(str1)

# MULTI-LINE STRINGS
str2 = "hello " \
        "welcome to the class " \
        "session 3"
print(str2)
str3= '''Hello
all
welcome to session-3'''
print(str3)

# Strings are IMMUTABLE
# SLICING SYNTAX: str[start_index_pos : end_index_pos : number_of_jumps]
str = "Hello all"
print(str[0:9:2])
print(str[-9::2])
print(str[:])
print(str[1:4])
print(str[::-1])

# String Comparison: > , < , == , <= , >=
str1="hello"
str2="Hello"
print(str1==str2)
print(str1>str2)
# ASCII CODES:
# A-Z: 65 to 90    ;    a-z: 97 to 122
# ord(): gives ascii codes for characters
# chr(): gives corresponding characters for a given ascii code
print(ord('H'))
print(ord('h'))
print(chr(65))
print(chr(97))

# String repetition: *operator
str1="hello "
print(str1*5)

# Concatenation
str1="hello "
str2=" "
str3="everyone"
print(str1+str2+str3)

# Find length of characters in a string
print(len(str3))

# Test if a particular character of sub-string is present in a string or not: MEMBERSHIP TEST
s1 = "hello dear friends, welcome to the class"
print('friend' in s1)
print(',' in s1)
print('Hello' in s1)
print('...' not in s1)

# STRING METHODS
st1 = "HeLlo alL"
# To convert into upper case
print(st1.upper())
print(st1)
# To convert into lower case
print(st1.lower())
# Replace a particular sub-string inside a string to create a new string
st1="hello, all, students"
new_string = st1.replace('all', 'all the')
print(new_string)
# To find if a particular sub-str is present or not
# find(): returns the starting index of sub-string if present else returns -1
print(st1.find('people'))
print(st1.find('students'))
# index(): finds the index of substring. if substring is absent then it raises an ERROR
# print(st1.index('people')) -> gives error
print(st1.index('students'))
# split(): to slice or split or cut the string
# syntax: split('separator', max_number_of_splits)
print(st1.split())
print(st1.split(','))
print(st1.split(',',1))
# strip(): to remove spaces from text string specifically loading and trailing
s1="          Hello   all   welcome          "
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())
