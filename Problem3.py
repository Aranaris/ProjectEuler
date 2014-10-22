#Project Euler Problems

#Problem 3: Largest prime factor

x = 600851475143
i = 1

is_prime = 0
listf = []
max_prime = 0

while i <= x // 2:
	if x % i == 0 and i % 2 != 0:
		factor = x // i
		listf.append(factor)
		j = 2
		while j <= factor // 2:
			if factor % j == 0:
				break
			j += 1
		if j >= factor // 2:
			max_prime = factor
			break
	i += 1

# print(listf)

	
		# print(j)
print(max_prime)