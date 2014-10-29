#Project Euler Problems

#Problem 3: Largest prime factor

y = 600851475143
#y = 24
factors = []
def prime_factors(n):
	i = 2
	while i <= n:
		if n % i == 0: 
			factors.append(prime_factors(n // i))
			return i
		i += 1

prime_factors(y)
print(factors)