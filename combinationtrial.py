'''
n=int(input("enter number "))
m=[n]
for i in m:
    for j in m.remove(i):
        for k in m.remove(j):
            if i!=j and j!=k and i!=k:
                    print(m[i],m[j],m[k])
'''
n=str(input("enter"))
for char in n:
    for j in n:
        for k in n:
            if char!=j and j!=k and char!=k:
                    print(char,j,k)



