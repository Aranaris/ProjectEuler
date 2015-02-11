#Project Euler Problems

#Problem 6: Sum Square Difference

import sys



def sum_of_squares(n): # sum of 1^2 + 2^2 + ... (n - 1)^2 + n^2
	sum1 = 0
	for x in range(n+1):
		sum1 += x * x	
	return sum1
	
def square_of_sum(n): # square of (1 + 2 + ... + (n - 1) + n)
	return sum(range(n+1)) ** 2
	


x = int(sys.argv[1])

print(square_of_sum(x) - sum_of_squares(x))


