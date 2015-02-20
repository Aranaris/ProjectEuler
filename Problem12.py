from itertools import combinations
from functools import reduce
import sys

def findprimefactors(num):
    i = 2
    while i < num:
        if num % i == 0:
            factors = [i]
            factors.extend(findprimefactors(num // i))
            return factors
        i += 1
    return [num]

def finddivisors(num):
    it = findprimefactors(num)
    factors = set(it + [1, num])
    for i in range(2, len(it)):
        for j in combinations(it, i):
            factors |= set([reduce(lambda x, y: x * y, j)])
    return factors

def trinum(num):
    return reduce(lambda x, y: x + y, range(1, num + 1))

def numdivisors(num):
    return len(finddivisors(trinum(num)))

def findfirsttrinum(target):
    start = 1
    while numdivisors(start) < target:
        start += 1
    return trinum(start)

print(findfirsttrinum(int(sys.argv[1])))
