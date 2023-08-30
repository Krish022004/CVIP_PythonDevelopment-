import math
def add(x, y):
    return x + y
def sub(x, y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def sqr(x):
    return math.sqrt(x)
def power(x,y):
    return math.pow(x,y)


print("Select opertion")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square root")
print("6.Power")
while True:
    choice = input("enter choice (1/2/3/4):")
    if choice in ('1','2','3','4'):
        try:
            num1=int(input("Enter first number:"))
            num2 =int(input("Enter second number:"))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        if choice == '2':
            print(num1,"-",num2,"=",sub(num1,num2))
        if choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        if choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
    if choice == '5':
        try:
            num = int(input("Enter a number:"))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        print(num," square root =",sqr(num))
    if choice== '6':
        try:
            num = int(input("Enter base number:"))
            exp=int(input("enter exponentiation"))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        print(num,"^",exp,"=",power(num,exp))
    next=input("let's do next calculation?(yes/no):")
    if next == "no":
        break
    else:
        print("Invalid input")