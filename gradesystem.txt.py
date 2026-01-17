sub1t=float(input("enter maximum marks for subject 1= "))
sub1o=float(input("enter marks obtained for subject 1= "))
sub2t=float(input("enter maximum marks for subject 2= "))
sub2o=float(input("enter marks obtained for subject 2= "))
sub3t=float(input("enter maximum marks for subject 3= "))
sub3o=float(input("enter marks obtained for subject 3= "))
sub4t=float(input("enter maximum marks for subject 4= "))
sub4o=float(input("enter marks obtained for subject 4= "))
sub5t=float(input("enter maximum marks for subject 5= "))
sub5o=float(input("enter marks obtained for subject 5= "))
t=sub1t+sub2t+sub3t+sub4t+sub5t
print("total marks are",t)
o=sub1o+sub2o+sub3o+sub4o+sub5o
print("marks obtained are",o)
p=(o/t)*100
print("your percentage is",p,"%")
if p>=90:
   print("grade A1")
elif 80<=p<90:
   print("grade A2")
elif 70<=p<80:
   print("grade B1")
elif 60<=p<70:
   print("grade B2")
elif 50<=p<60:
   print("grade C1")
elif 40<=p<50:
   print("grade C2")
else:
   print("FAIL")