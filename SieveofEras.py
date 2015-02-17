import numpy as np

class PrimeSieve:
	def __init__(self, limit):
		self.limit = np.ones(limit + 1, dtype = int)
		self.markPrimes()

	def markPrimes(self):
		self.limit[0], self.limit[1] = 0, 0
		for i in range(2, int(len(self.limit) ** 0.5) + 1):
			j = 2 * i
			while j < len(self.limit):
				self.limit[j] = 0
				j += i

	def isPrime(self, n):
		if self.limit[n] == 1:
			return True

	def nthPrime(self, n):
		i = 0
		checknum = 0
		while i < n:
			checknum += 1
			if self.isPrime(checknum):
				i += 1
		return checknum