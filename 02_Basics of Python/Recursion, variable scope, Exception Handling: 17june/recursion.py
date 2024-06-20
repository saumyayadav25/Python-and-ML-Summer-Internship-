# Recursion in Functions
# Re-currence of calling itself by function
'''
Syntax:
def func1(arg1, arg2):
    #statements
    func1(v1,v2)
'''

# Factorial of a number without using recursion
num=int(input("enter a number to calculate factorial without recursion: "))
fact=1
if num==0 or num==1:
    fact=1
elif num<0:
    print("cannot calculate factorial for negative numbers.")
    fact='Inf'
else:
    while(num>0):
        fact=fact*num 
        num=num-1
print("factorial of given number(without recursion) is:", fact)

# Factorial of a number using recursion
def fact_using_rec(num):
    if num==1 or num==0:
        return 1
    elif num<0:
        print("Cannot calculate factorial of negative numbers")
    else:
        return num * fact_using_rec(num-1)
num=int(input("enter a number to calculate factorial using recursion: "))
result=fact_using_rec(num)
print("The factorial of number using recursion is: ", result)

# Use recursion to calculate sum of n positive numbers
def func_sum(num):
    if num<=1:
        return num
    else:
        return num+func_sum(num-1)
n=int(input("enter the value of n: "))
if n<0:
    print("cannot calculate sum of negative numbers")
else:
    print(f"The sum of {n} positive numbers is: ", func_sum(n))