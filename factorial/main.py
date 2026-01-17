def factorial(n):
    if(n<=0):
        return 1
    return n*factorial(n-1)
    
x=int(input("enter number:"))
print("factoral of {0} is {1}".format(x,factorial(x)))