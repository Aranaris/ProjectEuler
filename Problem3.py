#Project Euler Problems

#Problem 3: Largest prime factor

x = 13195
i = 1

is_prime = 0
listf = []
max_prime = 0

while i <= x // 2:
	if x % i == 0 and i % 2 != 0:
		factor = x // i
		listf.append(factor)
	i += 1

# print(listf)
for a in listf:
	j = 2
	while j <= a // 2:
		if a % j == 0:
			break
		j += 1
	if j >= a // 2 and a > max_prime:
		max_prime = a
		# print(j)
print(max_prime)