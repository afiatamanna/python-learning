on= True
def add():
    print(" operation is add")
    a= int(input("the 1st number is: "))
    b= int(input("the 2nd number is: "))
    z=a+b
    print("Result is = {}".format(z))


def sub():
    print(" operation is sub")
    a= int(input("the 1st number is ="))
    b= int(input("the 2nd number is ="))
    z = a - b
    print("Result is = {}".format(z))

def mult():
    print(" operation is multiply")
    a= int(input("the 1st number is ="))
    b= int(input("the 2nd number is ="))
    z = a * b
    print("Result is = {}".format(z))

def div():
    print("operation is div")
    a= int(input("the 1st number is ="))
    b= int(input("the 2nd number is ="))
    z = a /b
    print("Result is = {}".format(z))

while on:
    opt=input("type any operator like + - * and / OR Q(for quit):")
    if opt== "+":
        add()
    elif opt== "-":
        sub()
    elif opt== "*":
        mult()
    elif opt== "/":
        div()
    elif opt== "Q":
        print("quit this calculator")
        on = False
    else:
        print("invalid")

