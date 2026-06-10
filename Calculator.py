def calc(a, b, operation):
    if operation == "+":
        print(a,"+",b,"=",a+b) 
    elif operation == "-":
        print(a,"-",b)
        return a - b
    elif operation == "*":
        print(a,"*",b, "=",a*b)
    elif operation == "/":
        if b != 0:
            print(a,"/",b, "=",a/b)
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


check = True
while check:

    num1 = float(input("Enter a: "))
    num2 = float(input("Enter b: "))
    op = input("Enter the operation (+, -, *, /): ")
    calc(num1, num2, op)
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() == "y":
        check = True
    else:
        check = False