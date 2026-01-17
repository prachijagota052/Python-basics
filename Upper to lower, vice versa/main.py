s=input("Enter: ")
for i in range(len(s)):
    ascii=ord(s[i])
    if(ascii>=65 and ascii<91):
        print(chr(ascii+32),end='')
    elif(ascii>=97 and ascii<123):
        print(chr(ascii-32),end='') 
    else:
        print(s[i],end='')   