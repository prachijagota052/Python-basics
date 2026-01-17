'''
n=int(input("enter number"))
d=2
ctr=0
if d<=n:
    if n%d==0:
        ctr=ctr+1
        d=d+1
if ctr!=0:
    print("it is not prime")
else:
    print("prime")
'''
'''
m=int(input("enter lower range"))
n=int(input("enter highest range"))
d=2
ctr=0
for i in range(m,(n+1)):
    if d<=i:
        if i%d==0:
            ctr=ctr+1
        d=d+1
    if ctr==0:
        print(i)
'''
m=int(input("enter lower range"))
n=int(input("enter highest range"))
for i in range(m,n+1):
    flag=0
    for d in range(2,i):
        if i%d==0:
            flag=1
    if flag==0:
        print(i) 




