# name = "BHARAT"
# print(name)
# num1 = 40
# num2 = 50
# sum = num1 + num2
# print("sum of num1 and num2 is" ,sum)
# multi = num1 * num2
# print("Multiple of num1 and num2 is" ,multi)
# user = "bhrt"
# password = "bhrt1089"
# if ( user is "bhrt" )
#     and (password = "bhrt1089")
#     print ("We;lcome to my world")
# else:print ("get out")
# price = 100
# money = 50
# if (money>price):
#     print("i can buy pizza")
# else:
#     print("FEELING VERY BAD")
# Candy = 10
# pizza = 200
# money = 300
# if ( money > Candy or money > pizza):
#     a = money // Candy
#     b = money // pizza
#     print("I can buy", a, "candy or", b, "pizza")
# else:
#     print("I Have no money")
# while loop
# num = 1
# while (num<10):
#     print(num)
#     num += 1

# num = 1
# while (num<=100):
#     print(num)
#     num += 1

# num = 2
# while (num<=100):
#     print(num)
#     num += 2

# num = 1
# while (num<=100):
#     print(num)
#     num += 2

# num = 100
# while (num>=0):
#     if (num % 2 != 0):
#         print(num)
#     num -= 1

# sum = 0
# num = 1
# while (num<=10):
#     sum = sum + num
#     print(num)
#     num += 1
# print("total of numbers ",sum)

# for loop
# for i in range(1, 101):
#     print(i)

#even no
# for i in range(1, 101):
#     if (i % 2 == 0):
#         print(i)

# for i in range(1, 101):
#     if (i % 3 == 0):
#         print(i)

#reverse

# for i in range(100,0,-1):
#     print(i)

#even no

# for i in range(0, 101, +2):
#     print(i)

#odd no

# for i in range  (0, 101, +3):
#     print(i)

'''world = "rays indore"
for le in world:
    print(le)
'''

'''list = [1, 1.4, 'B', "BHRT"]
for le in list:
    print(le)
'''

#doubling is called nasted loop
'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
for le in matrix:
    for pe in le:
        print(pe)
'''
'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
for le in matrix:
    for pe in le:
        if pe % 2 == 0:
            print(pe)
'''
'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
for le in matrix:
    for pe in le:
        if pe % 2 != 0:
            print(pe)
'''

# input from user with if condition
'''num = int(input("enter any number "))
if num >= 0:
    print (num, "is a positive number")
else: print (num, "is a negative number")
'''

# user name and password
'''user = "Bharat"
password = "Bhrt123"
username = input("Usher Name ")

if username == user:
    passs = input("Enter Password ")
    if passs == password:
        print("Welcome To The Dashboard!")
    else:print("Please Enter Corrected Password")
else: print("User name not found please recheck or sing up!")
'''

#type casting conversion of data types
'''a = 20
b = 3
c = int(a / b)
d = float(c)
print(d)
'''

'''a = 123
b = str(a)
print(b)
print(type(b))
'''

#palindrome project
'''a = input("please enter ")
b = a [::-1]
if a == b:
    print("this is palindrome")
else: print("this is not palindrome")
'''

#prime no. define howmwork not completed

'''a = int(input("Please enter any no. "))
b = a % 2
c = a // a
if b == 0 or c == 0:
    print(a, "is a prime number")
else: print(a, "is not a prime number")
'''

# breake and continue

'''a = "Python"
for i in a:
    if i == 'o':
        break
    print(i)
'''

''''a = "Python"
for i in a:
    if i == 'o':
        continue
    print(i)
'''

'''I = ["ram", "shyam", 1,2,3,4,5]
for a in I:
    if a == 3:
        continue
    print(a)
'''

#date and time moduke

'''import datetime
x = datetime.datetime.now()
print(x)
y = datetime.datetime(2018, 2, 1)
print(y)
z = datetime.date(2018, 2 , 1)
print(z)
'''

# Example using break to search for an element in a list
'''number = [1,2,3,4,5,6,7,8,9,10]

search_for = 3
for num in number:
    if num == search_for:
        print("element found!")
        break
else:
    print("element not found")
'''

#example using break to exit a loop when a valid password entered
#home work
'''password = "Bhrt123"

Pas = input("Enter a Password ")
for C in password:
    if C == Pas:
        print("welcome to the dashboard!")
        break
'''

# if elfi conditions
'''num = int(input("enter any number "))
if num % 7 == 0 and num % 5 == 0:
    print("Divisible by both 7 and 5")
elif num % 7 == 0:
    print("Given no. Divisible by 7 but not by 5")
elif num % 5 == 0:
    print("Given no. divisible by 5 but not by 7")
else:
    print("Given no. is not divisible by both 7 and 5")
'''

#day print and month print

'''import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%B"))

print(x.strftime("%a"))
print(x.strftime("%b"))
'''

######## define our own funtion

'''def sum(a,b,c):
    D = a + b + c
    print("sum of a,b,c is", D)

sum(10,20,30)
'''

##### create calculator

'''def add(a,b):
    c = a + b
    print("sum of a an b is ", c)

def min(a,b):
    c = a - b
    print("minus of a and b is ", c)

def multi(a,b):
    c = a * b
    print("multiply of a and b is ", c)

def sub(a,b):
    if b == 0:
        print("Error! Division by zero!")
    else: c = a / b
    print("division of a and b is ", c)

def calculator():
    print("Welcome to the calculator")
    print("1 add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")

    choice = int(input("choice (1,2,3 or 4): "))
    if choice == 1:
         a = int(input(print("value of a = ")))
         b = int(input(print("value of b = ")))
         print(add(a, b))
    else: print("123")

calculator()
'''

#########github command cmd in a folder

## git init
# git clone "(reprosatory code)"

#########cmd
# git add .
# git commit -am"done"
# git push
