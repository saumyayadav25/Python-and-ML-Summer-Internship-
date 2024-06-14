# function Demo
def printOutput(str1):
    print("The paramter given to function:",str1)
    return
# call this function for execution
input1=input("enter username: ")
printOutput(input1)

# function without parameter
def print_output():
    input1=input("enter username:")
    print("the parameter given to function:", input1)

print_output()

# arguments in python are passed by reference
def func1(mylist):
    print("the values inside the function before changes:", mylist)
    mylist[2]=50
    print("the values inside the function after changes:", mylist)
    return
mylist=[10,20,30]
func1(mylist)
print("values outside the function:", mylist)

# sum of 2numbers
def sum(a,b):
    result=a+b
    return result
print(sum(5,7))

# default arguments
# in case user fails to give necessary argument default values of arguments will be taken
def sum1(num1,num2=10):    #we can give default argument right to left
    total=num1+num2
    print("the sum is:", total)
    return total
result=sum1(10,25)
print("the sum is:", result)

# dynamically passing any number of arguments: **args
def func2(**args):     #**args will by default act as a dictionary with key value pairs
    for key, value in args.items():
        print("the key is:", key, ".the value is:", value)
func2(name="saumya", age=19, salary=100000,degree=["B.tech","MBA"])
# keyword arguments

# dynamically give many simple arguments not in form of key value pairs
# *args
def func3(*val):
    sum=0
    for i in val:
        sum=sum+i
    print("the sum is:",sum)

func3(1,2)
func3(1,2,3,4,5,6,7,8,9,10)

