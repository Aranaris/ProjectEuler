##Project Euler Problems

#Problem 14: Longest Collatz Sequence
 

cache = {1: 1}
        
def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1

def seqlen1(x):
    count = 0
    y = x
    while y > 1:
        y = collatz(y)
        count += 1
        if y in cache:
            cache[x] = count + cache[y]
            return count + cache[y] 
    return count

[seqlen1(i) for i in range(1000000)]
print (max(cache.keys(), key=(lambda key: cache[key])))