def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()

#for i in g:
#    print(i)

#value = next(g)
#print(value)

#value = next(g)
#print(value)

#value = next(g)
#print(value)

#print(sorted(g))

#---------------------------------------------------------
def countdown(num):
    #print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
value = next(cd)

#print(value)
#print(next(cd))
#print(next(cd))


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

#print(firstn(10))
#print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


#print(sum(firstn(10)))
#print(sum(firstn_generator(10)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)