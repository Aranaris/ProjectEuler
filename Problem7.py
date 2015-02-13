#Project Euler Problems

#Problem 7: 10001st prime

import sys
from SieveofEras import PrimeSieve


p = PrimeSieve(1000000)
p.markPrimes()
print(p.nthPrime(int(sys.argv[1])))