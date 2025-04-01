
def add(num1,num2):
    print(num1+num2)

def subract(num1,num2):
    print(num1-num2)

def multiply(num1,num2):
    print(num1*num2)

def divide(num1,num2):
    print(num1/num2)

def calculator():
    while True:
        num1=int(input("Enter a number : "))
        operation=input("Enter any one operation (+,-,*,/) : ")
        num2=int(input("Enter a number : "))
        if operation=="+":
            add(num1,num2)
            break
        elif operation=="-":
            subract(num1,num2)
            break
        elif operation=="*":
            multiply(num1,num2)
            break
        elif operation=="/":
            divide(num1,num2)
            break
        else:
            print("Enter valid operation")
            continue
calculator()