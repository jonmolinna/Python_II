# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
a = [1, 2]
b = [3, 4]
prod = product(a,b)
#print(list(prod))


c = [1, 2, 3]
perm = permutations(c, 2)
#print(list(perm))


d = [1, 2, 3, 4]
comb = combinations(d, 2)
#print(list(comb))

comb_wr = combinations_with_replacement(d, 2)
#print(list(comb_wr))


e = [1, 2, 3, 4]
acc = accumulate(e)
#print(list(acc))


def smaller_than_3(x):
    return x < 3

f = [1, 2, 3, 4]
group_obj = groupby(f, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))


for i in count(10):
    print(i)
    if i == 15:
        break