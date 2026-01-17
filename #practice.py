#practice
#10a
'''
punctuations="[]#$%^&*()-+_={};',./:""<>?@!"
n=str(input("enter"))
myp=" "
for char in n:
    if char not in punctuations:
        myp=myp+char
print(myp)
'''
#10b
'''
def reverse(n):
    k=n[::-1]
    return k
n=input("enter:")
print(reverse(n))
'''
'''
#11a
n=int(input("enter:"))
sum=0
while n>0:
    sum+=n%10
    n=n//10
print(sum)
'''
'''
#11b
n=int(input("enter:"))
def sumof(n):
    if n==0:
        return 0
    else:
        return n%10 + sumof(n//10)
    
print(sumof(n))
'''
'''
#3b
t=float(input("enter in celcius"))
f=(9/5)*t+32
print(f)
'''
'''
#4
s1=set(input("enter values").split(','))
c=int(input("choose 1.add 2.update 3.discard 4.union 5.difference 6.intersection 7. comparison"))
if c==1:
    add=int(input("enter values"))
    s1.add(add)
elif c==2:
    u=set(input("enter values").split(','))
    s1.update(u)
elif c==3:
    d=input("enter values")
    s1.discard(d)
    
elif c==4:
    un=set(input("enter values").split(','))
    s1.union(un)
    print(s1)
elif c==5:
    di=set(input("enter values").split(','))
    dif=s1-di
    print(dif)
elif c==6:
    i=set(input("enter values").split(','))
    inter=s1&i
    print(inter)
elif c==7:
    com=set(input("enter values").split(','))
    comp= s1==com
    print(comp)
else:
    print("invalid entry")
print(s1)
'''
'''
#5a
y=int(input("enter year"))
if y%4==0 & y%100!=0:
    print("leap year")
elif y%4==0 & y%100==0 & y%400==0:
    print("century ly")
else:
    print("not")
'''
'''
#6b
n=int(input("enter:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
'''
'''
#7a
n=int(input("enter rows"))
for i in range(0,n+1):
    print(' '*i+'*'*(n-i) )
'''
'''
#7b
n=str(input("enter:"))
for char in n:
    for j in n:
        for k in n:
            if char!=j and j!=k and k!=char:
                print(char,j,k)
'''
'''
#9b
s=str(input("enter: "))
if s==s[::-1]:
    print("palindrome")
else:
    print("not")
'''
'''
#13
k=int(input("enter range"))
n1=0
n2=1
next=n1+n2
print(n1,n2,next,end=' ')
for i in range(2,k):
    n1=n2
    n2=next
    next=n2+n1
    print(next,end=" ")
'''
'''
#14
class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,other):
        realpart=self.real+other.real
        imagpart=self.imag+other.imag 
        return f"{realpart}+{imagpart}i"
    def __str__(self):
        return f"{self.real}+{self.imag}i"
m=int(input("complex number 1 as realpart"))
n=int(input("complex number 1 imagpart"))
x=int(input("complex number 2 as realpart"))
y=int(input("complex number 2 as imagpart"))
c1=ComplexNumber(m,n)
c2=ComplexNumber(x,y)
result=c1.add(c2)
print(result)
s=c1.__str__()
print(s)
'''
'''
#8a
result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
a=[
    [5,6,7],
    [8,8,8],
    [5,7,3]
    ]
b=[
    [5,6,7],
    [8,8,8],
    [5,7,3]
    ]
rowsa= len(a)
colsa=len(a[0])
rowsb=len(b)
colsb=len(b[0])
if len(a[0])!=len(b):
        print("not compatible")
else:
        for i in range(len(a)):
            for j in range(colsb):
                for k in range(rowsb):
                    result[i][j] += a[i][k]*b[k][j]
        for r in result:
              print(r)
'''

#8b
m=int(input("lower:"))
n=int(input("highest:"))

for i in range(m,n+1):
    flag=0
    for d in range(2,i):
        if i%d==0:
            flag=1
        
    if flag==0:
        print(i)
'''
#12
phonebook={}
def __init__phonebook():
    global phonebook
    phonebook={}
    print("initialized")
print(__init__phonebook)
def add(name,phone):
    phonebook[name]=phone
    print(f"phone number for {name} added")
    add(joke,980765)
'''