def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return (x/y)
def remainder(x,y):
    return x%y
def power(x,y):
    return x**y
def quotient(x,y):
    return x//y
def multiply(x,y):
    return x*y
    

    



x=int(input("""To:
    1.Add
    2.Subtact
    3.Divide
    4.Find Remainder
    5.Find Quotient
    6.Multiply
    7.Exponential
    Enter Choice:"""))
print("\n")
match x:
    case 1:
        y=int(input("enter first number:"))
        k=int(input("enter second number:"))
        print("{0}+{1}={2}".format(y,k,add(y,k)))
    case 2:
        y=int(input("enter first number:"))
        k=int(input("enter second number:"))
        print("{0}-{1}={2}".format(y,k,subtract(y,k)))
    case 3:
        y=int(input("enter dividend:"))
        k=int(input("enter divisor:"))
        print("{0}/{1}={2}".format(y,k,divide(y,k)))
    case 4:
        y=int(input("enter dividend:"))
        k=int(input("enter divisor:"))
        print("{0}%{1}={2}".format(y,k,remainder(y,k)))
    case 5:
        y=int(input("enter dividend:"))
        k=int(input("enter divisor:"))
        print("{0}//{1}={2}".format(y,k,quotient(y,k)))
    case 6:
        y=int(input("enter first number:"))
        k=int(input("enter second number:"))
        print("{0}*{1}={2}".format(y,k,multiply(y,k)))
    case 7:
        y=int(input("enter base:"))
        k=int(input("enter power:"))
        print("{0}**{1}={2}".format(y,k,power(y,k)))
    case _:
        print("Invalid Input")