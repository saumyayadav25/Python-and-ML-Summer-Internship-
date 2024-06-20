# Variable Scope: A variable scope is the region or area where the variable can be accessed and used
# Lifetime: Lifetie of the variable is the number of lines of code till that variable is used
'''
According to scope we have 3kinds of variables:
1. Local Variable
2. Global Variable
3. Nonlocal Variable
'''

# Local scope of variables
def func1():
    result="Final message inside function"
    print("The result is:", result)
    # Lifetime of variable 'result' is 2lines 12-13
func1() 
# print("The result is:", result)   :gives error as its not accesssible outside func1


# Global variables
result="Message outside any function scope"
def func2():
    result="message is inside function"
    print("The value of result inside func2: ", result)
func2()
print("Calling result outside func2: ", result)
# Lifetime of global variable 'result': 19-24


# Non local variables
# These variables are used in context of nested functions such that these variables cannot be assumed to be in local or global
def func_outer():
    result="Inside func_outer()"
    print("The result is: ", result)
    # Create a nested function
    def func_inner():
        nonlocal result
        result="Inside func_inner()"
        print("The result is: ", result)
    print("calling inner func()")
    func_inner()
    print("the result inside outer_func() and outside inner_func(): ", result)
print("calling outer func()")
func_outer()