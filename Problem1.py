#Project Euler Problems

#Problem 1: Multiples of 3 and 5
i = 1
list1 = []
while i < 1000:
	if i % 3 == 0:
		if i % 15 != 0:
			list1.append(i)
	if i % 5 == 0:
		list1.append(i)

	i += 1

#print (list1)
print (sum(list1))