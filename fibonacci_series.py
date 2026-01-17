'''
def fibonacci_series(a,b):
	return(a,b,a+b)
print(fibonacci_series(0,1))
''''''
'''

def fib(n):
	num1= 0
	num2= 1
	print(num1, num2, end=" ")
	next=1
	i=1
	while i<=n:
		print(next, end=" ")
		num1=num2
		num2=next
		next=num1+num2
		i=i+1

'''
n=int(input("enter position of fibonacci num till you want "))
def fibo(n):
	num1= 0
	num2= 1
	next=1
	i=1
	list=[0,1]
	while i<=n:
		newlist=[next]
		list.append(newlist)
		num1=num2
		num2=next
		next=num1+num2
		i=i+1
	print(list[-1])
print(fibo(n))
'''

