l=[]
x=int(input("enter:"))
l.append(x)
y=int(input("enter:"))
l.append(y)
z=int(input("enter:"))
l.append(z)
if(x==y and y==z):
    print("All are equal")
max=l[0]
for i in l:
    if(i>max):
        max=i
print("largest number is",max)