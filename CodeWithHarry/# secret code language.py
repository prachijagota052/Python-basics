# secret code language
import random
import string

x=int(input("choose\n1.Code\n2.Decode\nenter number:"))
match x:
    
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string
    case 1:
        n=input("enter:")
        if len(n)<3:
            print(n[::-1])
        else:
            all_char=string.ascii_letters + string.digits + string.punctuation 
            t= random.choice(all_char) + random.choice(all_char) + random.choice(all_char) + n[1:] + n[:1]+random.choice(all_char)+random.choice(all_char)+random.choice(all_char)
            print(t)      


# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

    case 2:
        n=input("enter:")
        if len(n)<3:
            print(n[::-1])
        else:
            t= n[-4:-3]+n[3:-4]
            print(t)
    case _:
        print("invalid input")

        



