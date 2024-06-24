# Single inheritance: Single Parent -> Single Child
class Parent:
    value=10

    def __init__(self,num):
        self.value = num
        print("In Parent class Constructor, the value is:", self.value)
        print("The num argument is: ", num)
    def parentfunc1(self):
        print(f"This is parent class method parentfunc() and value is {Parent.value}")
        # Parent.value->create a temporary unnamed parent obj that will call Parent value
    def func1(self):
        print("This is func1() of parent class")

class Child(Parent):
    childvalue=20

    def __init__(self):
        print("Inside child class constructor")
        # We can call Parent class constructor from here
        super().__init__(self.value)
    def childfunc1(self):
        print(f"This is child class method childfunc() and value is {self.value}")
        print(f"This is child class method childfunc() and child value is {self.childvalue}")
    def func1(self):
        print("This is func1() of child class")
        super().func1()  #This will call func1() of parent class

obj1=Child()
obj1.childfunc1()
obj1.parentfunc1() #reusing the parent class method
obj1.func1()

# variable and method overriding

# check for subclass and superclass
print(issubclass(Child,Parent))
print(issubclass(Parent,Child))

# object checking
print(isinstance(obj1,Child))    #instance is another name for object
print(isinstance(obj1,Parent))
# obj2=Parent()
# print(isinstance(obj2,Child))  
# print(isinstance(obj2,Parent))

# super()-> super keyword is used to access the parent class constructor, method and variables from inside the child class.

# In python the order of resolving the call to constructors and methods of inherited class
# Method Resolution Order : MRO
# Single Inheritance Code
'''
class Parent1:
    def __init__(self):
        print("Inside the parent class constructor")

class Child1(Parent1):
    def __init__(self):
        print("Inside the child class constructor")
print("The MRO Order with __mro__ property is:", Child1.__mro__)
print("The MRO Order with mro() is:", Child1.mro())
'''

# Multiple Inheritance: 2 or more parent class and only 1 child class
class Parent1:
    def __init__(self):
        print("Inside the parent 1 class constructor")
class Parent2:
    def __init__(self):
        print("Inside the parent 2 class constructor")
        super().__init__()
    # pass
class Child1(Parent1,Parent2):
    def __init__(self):
        print("Inside the child class constructor")
        super().__init__()
obj1=Child1()
# MRO
print("The MRO Order with __mro__ property is:", Child1.__mro__)
print("The MRO Order with mro() is:", Child1.mro())

# Multilevel Inheritance
class GrandParent:
    def __init__(self):
        print("Inside GrandParent class Constructor")

class P1(GrandParent):
    def __init__(self):
        print("Inside the P 1 class constructor")
        super().__init__()
class P2():
    def __init__(self):
        print("Inside the P 2 class constructor")
        super().__init__()
class C1(P2,P1):
    def __init__(self):
        print("Inside the child class constructor")
        super().__init__()
obj1=C1()
print("The MRO Order with __mro__ property is:", C1.__mro__)
print("The MRO Order with mro() is:", C1.mro())

# Hierarchical Inheritance: only 1 parent class, multiple child classes
class Par1:
    def __init__(self):
        print("Inside Par1 Constructor")
class Ch1(Par1):
    def __init__(self):
        print("Inside Ch1 class constructor")
        super().__init__()
class Ch2(Par1):
    def __init__(self):
        print("Inside Ch2 class constructor")
        super().__init__()
print("......Creating Ch1 object......")
o1=Ch1()
print("......Creating Ch2 object......")
o2=Ch2()
print("The MRO Order with __mro__ property is:", Ch1.__mro__)
print("The MRO Order with mro() is:", Ch1.mro())
print("The MRO Order with __mro__ property is:", Ch2.__mro__)
print("The MRO Order with mro() is:", Ch2.mro())



# Diamond Problem
'''
       GrandParent
        /     \
    Parent1   Parent2
       \      /
       Child class
'''
class GP:
    def func1(self):
        print("inside grandparent func1()")

class Paren1(GP):
    def func1(self):
        print("Inside Paren1 class func1()")
        super().func1()
class Paren2(GP):
    def func1(self):
        print("Inside Paren2 class func1()")
        super().func1()
class Childd(Paren1,Paren2):
    pass
ob1= Childd()
ob1.func1()
print("The MRO Order with __mro__ property is:", Childd.__mro__)
print("The MRO Order with mro() is:", Childd.mro())












