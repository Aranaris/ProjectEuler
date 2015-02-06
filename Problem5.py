#Project Euler Problems

#Problem 5: Smallest Multiple

def min_mult(n):
	i = n

	test_list = []
	for a in range(1, n + 1, 1):
		for b in range(n // 2, n + 1, 1):
			if b % a == 0 and b != a:
				break
			elif b == n:
				test_list.append(a)
	while i > 0:
		for x in test_list:
			if i % x != 0:
				break
			elif x == n:
				return (i)
		i += n
		
print (min_mult(20))