
def sort(x):
    if(x[0]<=x[1] and x[1]<=x[2]):
        print("True")
    else:
        for j in range(2):
            for i in range(2):
                if(x[i]>x[i+1]):
                    temp=x[i]
                    x[i]=x[i+1]
                    x[i+1]=temp
        print("False")
        print(x)
x=list(input("Enter 3 integers as a,b,c: ").split(','))
sort(x)