#Project Euler Problems

#Problem 7: 10001st prime

import sys

def prime_factors(n):
	i = 2
	while i < n:
		if n % i == 0: 
			factors = list(range(2, i + 1))
			factors += prime_factors(n // i)
			return factors
		i += 1
	return set([n])


input = int(sys.argv[1])
test = 2
nth_prime = 0

while nth_prime < input:
	if len(prime_factors(test)) == 1:
		nth_prime += 1
		test = 
	else:
		test += 1

print(test)