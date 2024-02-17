######## my calculator
'''def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def calculator():
    print("Select Operation:")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")

    choice = input("Enter your choice (1,2,3 or 4): ")

    a = float(input("Enter First Value: "))
    b = float(input("Enter Second Value: "))

    if choice == '1':
        print("Result: ", add(a, b))
    elif choice == '2':
        print("Result: ", subtract(a, b))
    elif choice == '3':
        print("Result: ", multiplication(a, b))
    elif choice == '4':
        print("Result :", divide(a, b))
    else:
        print("Select the correct operation!")

calculator()'''