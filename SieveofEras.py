import numpy as np

class PrimeSieve:
	def __init__(self, limit):
		self.limit = np.ones(limit, dtype = int)
		self.markPrimes()

	def markPrimes(self):
		self.limit[0], self.limit[1] = 0, 0
		for i in range(2, int(len(self.limit) ** 0.5)):
			for j in range(2, int(len(self.limit)/i)):
				self.limit[j * i] = 0
	
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