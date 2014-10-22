#Project Euler Problems

#Problem 1: Multiples of 3 and 5

x = 0
for i in range (1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		x += i

#print (list1)
print(x)