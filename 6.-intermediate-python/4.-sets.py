# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print(myset) # {1,2 3, 4, 5}

myset2 = set([1, 2, 3, 4, 1, 2, 5, 6, 7])
print(myset2) # {1, 2, 3, 4, 5, 6, 7}

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(primes)
print(i) # {3, 5, 7}


setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()

setB.add(7)
print(setB)
print(setA)