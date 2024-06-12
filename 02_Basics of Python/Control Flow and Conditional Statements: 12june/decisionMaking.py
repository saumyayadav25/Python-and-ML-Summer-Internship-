# example of if-elif-else block
# check if the number is positive, negative or 0
number =int(input("enter any number :"))
if number>0:
    print(f"the number {number} is positive")
elif number<0:
    print(f"the number {number} is negative")
else:
    print(f"the number is zero")

# nested if's
number=int(input("enter any number:"))
if number>=0:
    if number==0:
        print("the number is zero")
    else:
        print("the number is positive")
else :
    print("the number is negative")