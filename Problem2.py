#Project Euler Problems

#Problem 2: Even Fibonacci numbers

f_num1 = 1
f_num2 = 2
f_next = f_num2
x = 0

while f_next <= 4000000:	
	if f_next % 2 == 0:
		x += f_next
	f_next = f_num1 + f_num2
	f_num1 = f_num2
	f_num2 = f_next

print(x)