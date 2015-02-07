#Project Euler Problems

#Problem 6: Sum Square Difference

import array
import sys

def sum_of_squares(n): # sum of 1^2 + 2^2 + ... (n - 1)^2 + n^2
	a = array.array('i', range(1, n + 1))
	for idx, val in enumerate(a):
		a[idx] = val ** 2
	
	return sum(a)
	
def square_of_sum(n): # square of (1 + 2 + ... + (n - 1) + n)
	b = array.array('i', range(1, n + 1))
	return sum(b) ** 2


x = int(sys.argv[1])
x = int(sys.argv[1])
print(square_of_sum(x) - sum_of_squares(x))


