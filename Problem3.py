#Project Euler Problems

#Problem 3: Largest prime factor

y = 600851475143
#y = 24

def prime_factors(n):
	i = 2
	while i <= n:
		if n % i == 0: 
			factors = [i]
			factors += prime_factors(n // i)
			return factors
		i += 1
	if n != 1:	
		return [n]
	return []

a = prime_factors(y)
print(a)