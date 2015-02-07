#Project Euler Problems

#Problem 6: Sum Square Difference

import array
import sys



def sum_of_squares(n): # sum of 1^2 + 2^2 + ... (n - 1)^2 + n^2
	i = 1
	sum = 0
	while i <= n:
		sum += i ** 2
		i += 1
	
	return sum
	
def square_of_sum(n): # square of (1 + 2 + ... + (n - 1) + n)
	i = 1
	sum = 0
	while i <= n:
		sum += i
		i += 1
	return sum ** 2


x = int(sys.argv[1])
x = int(sys.argv[1])
print(square_of_sum(x) - sum_of_squares(x))


