##Project Euler Problems

#Problem 17: Number Letter Counts

import inflect

def lettercount(end):
    e = inflect.engine()
    return sum(len(e.number_to_words(i).replace(" ", "").replace("-", "")) for i in range(1, end + 1))

print(lettercount(1000))