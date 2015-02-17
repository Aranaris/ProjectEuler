##Project Euler Problems

#Problem 9: Special Pythagorean triplet

import sys
import math
import functools

def findtriplet(n):
    for i in range(1, int(n / 3)):
        for j in range(i, n - i):
            k = math.sqrt(i ** 2 + j ** 2 )
            if k.is_integer() and i + j + k == n: 
                return [i, j, int(k)]

print (functools.reduce(lambda x, y: x * y, findtriplet(int(sys.argv[1]))))