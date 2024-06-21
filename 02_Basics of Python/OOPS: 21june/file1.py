# Class and instantiate the objects
# Define a new user-defined class: class keyword
class Employee:
    # define variables or attributes or properties of class
    # define a constructor: __init__() to initialize an object and this constructor will be called everytime we create a new object itself. We do not call init() separately.
    def __init__(self,id=1,sal=0.0,nam="Guest user"):
        self.emp_id = id
        self.emp_sal = sal
        self.emp_name = nam
    # emp_id = 0
    # emp_sal = 0.0
    # emp_name = ""

    # define methods of class
    # self parameter inside method suggests that this method can be only used with the current object of the related class
    def emp_details(self):
        print(f"The name is: {self.emp_name},The employee_id is {self.emp_id} and salary is {self.emp_sal}")

    def input_details(self):
        self.emp_name=input("Enter the employee name: ")
        self.emp_id=int(input("Eneter an employee id: "))
        self.emp_sal=int(input("Enter the salary for employee: "))

# out of the class
# instantiate the class or create the object of class
print("Creating first employee object.....")
emp_obj1=Employee(1,100,"User")
emp_obj1.emp_details() #call method emp details to print
emp_obj1.input_details() #call method input details
emp_obj1.emp_details() 
print("Creating second employee object.....")
emp_obj2=Employee()
emp_obj2.emp_details()
emp_obj2.input_details() 
emp_obj2.emp_details()
print("Creating third employee object.....")
emp_obj3=Employee()
emp_obj3.input_details() 
emp_obj3.emp_details()

# DATA ABSTRACTION


class Sample:
    # public variable
    var1 = "Public Variable"
    # protected variable
    _var2 = "Protected variable"
    # private variable
    __var3 = "Private variable"

    def __init__(self):
        self.var1="public variable in constr"
        self._var2="protected variable in constr"
        self.__var3="private variable in constr"

    def display(self):
        print(f"The public var is: {self.var1}")
        print(f"The protected var is: {self._var2}")
        print(f"The private var is: {self.__var3}")

obj1=Sample()
print("The public var initial val: ", obj1.var1)
obj1.var1="New value outside"
print("The public var new val: ", obj1.var1)
print("The initial protected var: ", obj1._var2)
obj1._var2="New value of protected var 20"
print("The new protected var: ", obj1._var2)
# print("The initial private var: ", obj1.__var3)
obj1.display()
