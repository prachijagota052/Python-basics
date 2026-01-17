n=input("Enter character:")
ascii=ord(n)
if(ascii>=48 and ascii<58):
    print(n,"is a digit")
elif(ascii>=65 and ascii<91):
    print(n,"is an alphabet in upper case")
elif(ascii>=97 and ascii<123):
    print(n,"is an alphabet in lower case")
else:
    print(n,"is not a digit/alphabet")