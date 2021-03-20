import random

a = random.uniform(1, 10)
b = random.randint(1, 20)
c = random.randrange(1, 5) # 1 - 4
d = random.normalvariate(0, 1) # cuadros estadisticos (-, +)

mylist = list("ABCDEFGH")
e = random.choice(mylist)
f = random.sample(mylist, 3)


import secrets

g = secrets.randbelow(10)
h = secrets.randbits(4)


print(h)