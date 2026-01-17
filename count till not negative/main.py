l=[]
count=0
countodd=0
sum=0
sumodd=0
while(True):
    n=int(input("enter number:"))
    if(n<0):
        break
    else:
        count=count+1
        sum=sum+n
        if(n%2!=0):
            countodd=countodd+1
            sumodd=sumodd+1
print("Total count:",count) 
print("Total sum:",sum)
print("ODD count:",countodd)
print("ODD sum:",sumodd)
if(countodd!=0):
    average=(sumodd/countodd)
    print("ODD average:",average)