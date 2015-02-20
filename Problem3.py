#Project Euler Problems

#Problem 3: Largest prime factor


#y = 600851475143
#y = 24
y = 28

def prime_factors(n):
	i = 2
	while i < n:
		if n % i == 0: 
			factors = set([i])
			factors |= prime_factors(n // i)
			return factors
		i += 1
	return set([n])

print(prime_factors(y))