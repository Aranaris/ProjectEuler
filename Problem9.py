##Project Euler Problems

#Problem 9: Special Pythagorean triplet

import sys
import math
import itertools

def is_sum(a, b, c, n):
    if a + b + c == n:
        return True

def findtriplet(n):
    for i in range(1, int(n / 3)):
        for j in range(i, n - i):
            k = math.sqrt(i ** 2 + j ** 2 )
            if k.is_integer() and is_sum(i, j, k, n): 
                return [i, j, int(k)]

def prodlist(a):
    product = 1
    for i in a:
        product = product * i
    return product

print(prodlist(findtriplet(int(sys.argv[1]))))