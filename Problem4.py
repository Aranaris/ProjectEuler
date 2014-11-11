#Project Euler Problems

#Problem 4: Largest palindrome product




def check_palindrome(n):
	test = str(n)
	if test[0 : len(test) // 2] == test[: len(test) // 2 - 1 : -1]:
		return True
	return False

def max_palindrome(a, b):
	p1 = 100
	p2 = 100
	max_pal = 0
	while p1 <= a:
		while p2 <= b:
			if (p1 * p2) > max_pal and check_palindrome(p1 * p2): #and :
				max_pal = p1 * p2
			p2 += 1	
		p1 += 1
		p2 = 100
	return max_pal
# print(str(max1) + " " + str(max2))
print (max_palindrome(999, 999))


		