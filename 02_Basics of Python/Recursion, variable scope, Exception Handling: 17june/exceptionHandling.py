# How to view all built-in exceptions
print(dir(locals()['__builtins__']))

'''
Syntax:
try:
    statements
except Exception_name:
    This will handle for only Exception_name
except:
    This will be general except block for any Exception
else: 
    This statement will be executed if non of except statements are working
finally:
    This statement will work always after try-except-else have completed working
'''

# Arithmetic Error-> num/0=Inf
try:
    num1=int(input("Enter numerator: "))
    num2=int(input("Enter denominator: "))
    result=num1/num2
    print("the result is:", result)
    list1=[1,2,3,4,5]
    i=int(input("enter the index value you want to access in list:"))
    print(f"the element at index {i} in list is:", list1[i])
    print("The name of user is:", name)
except ZeroDivisionError:
    print("Cannot divide by zero.. Give valid input")
except IndexError:
    print("cannot access element beyond the length of list")
except:
    print("An exception occurred. Please check inputs again")
else:
    print("No exception occurred!! Successful execution.")
finally:
    print("Inside finally block..")
    username=input("Enter your name: ")
    print(f"Welcome to python programming {username}")


#  USER-DEFINED EXCEPTIONS
# Create a new user class which is derived from Exception class
# Create exception for retired senior citizen candidates
class InvalidAgeException(Exception):
    pass
age=int(input("Enter age for retired employee: "))
try:
    if age<60:
        raise InvalidAgeException
    else:
        print("Valid age inserted!!")
        print("The employee is eligible for pension scheme!!")
except InvalidAgeException:
    print("Exception occurred!! Only age>=60 is acceptable.")