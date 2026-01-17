
def reverse(x):
    print("Reverse: ",end=" ")
    while(x>0):
        y=x%10
        print(y,end="")
        x=x//10
x=int(input("Enter number:"))
reverse(x)

    