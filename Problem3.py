#Project Euler Problems

#Problem 3: Largest prime factor

#y = 600851475143
y = 24

def prime_factors(n):
	i = 1
	while i <= n:
		if n % i == 0 and i > 1:
			return i
		i += 1