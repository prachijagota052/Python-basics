#practice
'''class Student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(f"name:{self.name},roll:{self.roll}")
m=Student("alice",25)
m.display()

class Person(Student):
    def __init__(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def display(self):
        print(f"name:{self.name},roll:{self.roll},age:{self.age}")
'''
'''
def greet(name="student"):
    print(f"hello {name}")
greet("aly")
'''
"""def greet(name,age):
    print(f"{name}{age}")
greet(67,"poo")
greet(age=67, name="poo")
"""
'''
def add(a,b):
    """add is"""
    return a+b 
print(add.__doc__)
'''
'''def order(size,*toppings,**details):
    print(f"pizza is {size}. toppings are{toppings}. details are {details}")
order("large", "tomato","onion", delivery=True, inch=6)
'''
'''d={'name':'aru','age':9}
d['name']="roh"
d['age']=13
print(d)
print((type(d)))
x=d.get('age')
print(x)
d.update({"city":"mumbai"})
print(d)
d.pop('age')
print(d)
d.keys()
'''
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"{self.name}{self.age}")

class Student(Person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
    def display(self):
        super().display()
        print(f"{self.roll}")

m=Person("alice",16).display()
n=Student("alice",16,7).display()
'''
'''class Circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def area(self):
        return Circle.pi*self.r*self.r
c=Circle(7)
print(c.area())

hasattr(c,'r')
'''
