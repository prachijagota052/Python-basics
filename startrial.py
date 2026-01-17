'''
n=5
for i in range(n,-1):
    print(i*'*')
'''

n=int(input("enter number of rows"))
for i in range(0,n):
    print(' '*(i) + '*'*(n-i))
'''
  *  
 *** 
*****
'''
'''
n=3
for i in range(0,n):
    print(i*' ' + '*'*(n-i+2) + i*' ')
'''