#Project Euler Problems

#Problem 4: Largest palindrome product

p1 = 100
p2 = 100
max_palindrome = 0

def check_palindrome(n):
	test = list(map(int, str(n)))
	i = 0
	while i < len(test) // 2:
		if test[i] != test[len(test) - 1 - i]:
			return False
		i += 1
	return True
	
while p1 < 1000:
	while p2 < 1000:
		if check_palindrome(p1 * p2) and p1 * p2 > max_palindrome:
			max_palindrome = p1 * p2
		p2 += 1
	p1 += 1
	p2 = 100

# print(str(max1) + " " + str(max2))
print (max_palindrome)