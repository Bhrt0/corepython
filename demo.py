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

#date and time module

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

######## define our own function

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

# test print even numbers using while loop

'''num = 0
while (num<=100):
    print(num)
    num += 2
'''

'''T = input("enter anything: ")
Y = T [::-1]
if T == Y:
    print("this is a palindrome!")
else:print("this is not a palindrome")
'''

########## Variable arguments in a functions for auto_multiple variables

'''def sumNum(a, *varg):
    t = a
    for n in varg:
        t += n
    return t

total = sumNum(1,2,3,4,5,6)
print("total", total)

def my_fun(*argsh):
    for arg in argsh:
        print(arg)

my_fun(1,2,'B',"bhrt")
'''

########## variable arguments with key and values dectionary style
'''def my(**kward):
    for key, value in kward.items():
        print(f"{key}: {value}")


my(a=1,b=2)

n = input("enter your first name: ")
s = input("enter your last name: ")

my(Name=n, Lastname=s)
'''

'''def Double(*args, **kwargs):
    for d in args:
        print(d)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

Double(1,3,5,a=1,b=3)
'''

'''def Ne(**kwarf):
    for key, value in kwarf.items():
        print(f"{key}: {value}")  #F string use for messsage as well as variables do not need to use commas


N = input("Enter your First name: ")
S = input("Enter your Second name: ")


Ne(Name=N, Surname=S)
print("Welcome",N,S,"!")
'''

# class and OOB object oriented programming

'''class Person:
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

####self is refrence parameter

    def introduce(self):
        print(f"Hello, My name is {self.name}. I am {self.age} years old and {self.gender}.")

class Car_details:
    def car(self, color, company):
        self.color = color
        self.company = company

    def showinfocar(self):
        print(f"Hello this my color {self.color}. my car company name {self.company}.")


p = Person()
p.set_details("Jitu", 30, "Male")

#### p jo h object h class Person() ka
#######obj calling p = Person()
########p.lagakar app Person class k function & methods ko call kr skte ho

#calling methods on the person object

p.introduce()

a = Car_details()
a.car("Black", "Porche")
a.showinfocar()

b = Car_details()
b.car("Blue", "DC Avanti")
b.showinfocar()
'''

###home work mobile property class pending

'''class Mobile():
    def Apple(self, model, storage, colour):
        self.model = model
        self.storage = storage
        self.colour = colour




print("Select Your Favorite Brand: ")
print("1. Apple")
print("2. Samsung")
'''


########### constructor (we do not call func name it is direct inbluilt method)

'''class Account:
    def __init__(self, Account_holder, intial_balance=0):
        self.name = Account_holder
        self.balance = intial_balance

    def Add(self, Customer_name, intial_balace):
        self.newname = Customer_name
        self.intbal = intial_balace


def sata(*vars):
    for all in vars:
        return all

acc1 = Account("Bhrt", 10000)
print("Account Holder Name: ", acc1.name)
print("Account Balance: ", acc1.balance)
'''
######shop e-com invoicing
'''class Shop:
    def __init__(self):
        print("Welcome to the Shop!!")  ####default constructor


    def Customer(self):
        Cname = input("Enter your name: ")
        Cmob = input("Enter your mobile no: ")
        self.CName = Cname
        self.Mobile = Cmob
        print(f"Hi {self.CName}!!!")

    def Calsi(self, Atta, Daal, Chawal):
        self.A = Atta
        self.D = Daal
        self.C = Chawal
        return print("Total Invoice Value: ", (self.A * 60) + (self.D * 50) + (self.C * 40))

    def date(self,DT):
        print("Invoice Date: ", DT)

class Shop1(Shop):
    def Calsi1(self, Atta, Daal, Chawal, Sabudana):
        self.A = Atta
        self.D = Daal
        self.C = Chawal
        self.S = Sabudana
        return print("Total Invoice Value: ", (self.A * 60) + (self.D * 50) + (self.C * 40) + (self.S * 70))

    def Item_show(self):
        print("Add items to your cart: ")
        print("1. Atta, rate 60.00 per KG")
        print("2. Daal, rate 50.00 per KG")
        print("3. Chawal, rate 40.00 per KG")
        print("4. Sabudana, rate 70.00 per KG")
'''


'''B = Shop()
B.Customer()
print("Add items to your cart: ")
print("1. Atta, rate 60.00 per KG")
print("2. Daal, rate 50.00 per KG")
print("3. Chawal, rate 40.00 per KG")
select = input("Select item (1,2,3): ")
if select == '1':
    AQ = float(input("How much Atta do you want (KG): "))
    DQ = 0.00
    CQ = 0.00
    B.Calsi(AQ,DQ,CQ)
elif select == '2':
    DQ = float(input("How much Daal do you want (KG): "))
    AQ = 0.00
    CQ = 0.00
    B.Calsi(AQ, DQ, CQ)
elif select == '3':
    CQ = float(input("How much Chawal do you want (KG): "))
    AQ = 0.00
    DQ = 0.00
    B.Calsi(AQ, DQ, CQ)
elif select == '1' '2' or select == '2' '1':
    AQ = float(input("How much Atta do you want (KG): "))
    DQ = float(input("How much Daal do you want (KG): "))
    CQ = 0.00
    B.Calsi(AQ, DQ, CQ)
elif select == '1' '3' or select == '3' '1':
    AQ = float(input("How much Atta do you want (KG): "))
    CQ = float(input("How much Chawal do you want (KG): "))
    DQ = 0.00
    B.Calsi(AQ, DQ, CQ)
elif select == '2' '3' or select == '3' '2':
    AQ = 0.00
    DQ = float(input("How much Daal do you want (KG): "))
    CQ = float(input("How much Chawal do you want (KG): "))
    B.Calsi(AQ, DQ, CQ)
elif select == '1' '2' '3' or select == '1' '3' '2' or select == '3' '2' '1' or select == '2' '1' '3' or select == '3' '1' '2' or select == '2' '3' '1':
    AQ = float(input("How much Atta do you want (KG): "))
    DQ = float(input("How much Daal do you want (KG): "))
    CQ = float(input("How much Chawal do you want (KG): "))
    B.Calsi(AQ, DQ, CQ)
else:
    print("Please select valid options!")

import datetime
x = datetime.datetime.now()
B.date(x)

print("Thank You!")
'''

'''New = Shop1()
New.Customer()
New.Item_show()

select = input("Select item (1,2,3): ")
if select == '1':
    AQ = float(input("How much Atta do you want (KG): "))
    DQ = 0.00
    CQ = 0.00
    New.Calsi(AQ,DQ,CQ)
elif select == '2':
    DQ = float(input("How much Daal do you want (KG): "))
    AQ = 0.00
    CQ = 0.00
    New.Calsi(AQ, DQ, CQ)
elif select == '3':
    CQ = float(input("How much Chawal do you want (KG): "))
    AQ = 0.00
    DQ = 0.00
    New.Calsi(AQ, DQ, CQ)
elif select == '4':
    AQ = 0.00
    DQ = 0.00
    CQ = 0.00
    SQ = float(input("How much Sabudana do you want (KG): "))
    New.Calsi1(AQ, DQ, CQ, SQ)

else:
    print("Please select valid options!")

import datetime
x = datetime.datetime.now()
New.date(x)

print("Thank You!")
'''
##################### inherent classes (parent and child class)
'''class A:
    def Name_A(self):
        print("Hi! I am A")

class B(A):
    def Name_B(self):
        print("Hi! I am B")

class C(B):
    def Name_C(self):
        print("Hi! I am C")

D = C()

D.Name_A()
D.Name_B()
D.Name_C()
'''

'''user = int(input("enter mob: "))

ty = type(user)
if ty == int:
    print("Valid!")
else:
    print("Invalid Mobile number!")'''

################## how to valided mobile no.

'''def is_valid_integer(input_str):
    ### check if the input string represents an interger
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def main():
    user_input = input("Please enter a 10-digit number: ")

    # check if the input is a numeric string
    if is_valid_integer(user_input):
        # check if the input has exactly 10 digits
        if len(user_input) == 10:
            print("Valid input. You entered a 10-digit number:", user_input)
        else:
            print("Invalid input. Please enter a 10-digit number.")
    else:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
'''

########## inheritance with pass and super key-word

'''class Shape:
    def __init__(self, color):
        self.color = color

########## just for learn
    def area(self):
        pass



class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Reck(Shape):
    def __init__(self, color, lenght, width):
        super().__init__(color)
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

class Triagle(Shape):
    def __init__(self, color, Hight, Base):
        super().__init__(color)
        self.hight = Hight
        self.base = Base

    def area(self):
        return 1/2 * self.base * self.hight
'''

'''C = Circle("red", 5)
print("Circle Color: ", C.color)
print("Circle radius: ", C.radius)
print("Circle Area: ", C.area())
'''

'''R = Reck("Green", 4, 2)
print("Rectangle color: ", R.color)
print("Rectangle lenght: ", R.lenght)
print("Rectangle width: ", R.width)
print("Rerangle Area: ", R.area())
'''

'''T = Triagle("Blue", 12, 6)
print("Triangle color: ", T.color)
print("Triangle Hight: ", T.hight)
print("Triangle Base: ", T.base)
print("Triangle Area: ", T.area())

c = Circle("red",9)
print("CIrcle aree =",c.area())

r = Reck("black",2,3)
print(r.area())'''

