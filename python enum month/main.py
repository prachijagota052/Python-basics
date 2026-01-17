from enum import Enum
class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

x=int(input("enter:")) 
if(x>0 and x<13):
    print(Month(x).name)
else:
    print("Enter integer between 1-12")