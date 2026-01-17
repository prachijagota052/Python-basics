"""
#jkhj
hkkhn
hhbmjuyg
# hkjn
"""
# print("hkk
#       kjhh")
#       jkl
# a="be you"
# print(a.isspace())

# while False:
#     for i in range(10,0, -2):
#         print(i)
#print(0%2)

# country=("india","pakistan")
# print(country)
# list1=list(country)
# list1.append(7)
# print(list1)
# country=tuple(list1)
# print(country)

#fibonacci series


def fibonacci(n):
    if(n==1):
        return 0
    elif(n==0):
        return 0
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter position:"))

print(fibonacci(n))