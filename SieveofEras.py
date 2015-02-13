
# coding: utf-8

# In[34]:

import numpy as np

class PrimeSieve:
    def __init__(self, limit):
        self.limit = np.ones(limit, dtype = int)
    
    def markPrimes(self):
        for idx, val in enumerate(self.limit):
            if idx < 2:
                self.limit[idx] = 0
            else:
                for i in np.arange(2 * idx, len(self.limit), idx):
                    self.limit[i] = 0
              
    def nthPrime(self, n):
        i = 0
        for idx, val in enumerate(self.limit):
            if val == 1:
                i += 1
                if i == n:
                    return idx
        return "not found"
            


# In[38]:

# p = PrimeSieve(1000000)
# p.markPrimes()
# a = p.limit
# print(p.nthPrime(10001))


# In[ ]:



