##Project Euler Problems

#Problem 10: Summation of primes

import sys
from SieveofEras import PrimeSieve

def sumPrimes(n):
	sum = 0
	for i in range(len(n)):
		if n[i] == 1:
			sum += i
	return sum
	
p = PrimeSieve(int(sys.argv[1]))
print (sumPrimes(p.limit))