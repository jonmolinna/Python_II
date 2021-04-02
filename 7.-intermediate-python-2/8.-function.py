# Function arguments in detail
#   - The difference between arguments and parameters
#   - Positional and keyword arguments
#   - Default arguments
#   - Variable-length arguments (*args and **kwargs)
#   - Container unpacking into function arguments
#   - Local vs global arguments
#   - Parameter passing (by value or by refenece?)

def print_name(name):
    print(name)

#print_name('Brehn')

def foo(a, b, c, d=4):
    print(a, b, c, d)

#foo(1, 2, 3, 7)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

#foo(1, 2, 3, 4, 5, six=6, seven=7)

def moo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
#moo(*my_list)

def doo(a, b, c):
    print(a, b, c)

my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
#doo(**my_dict)

def foo():
    x = number
    print('number inside function:', x)

number = 5
#foo()

def goo(a_list):
    a_list += [200, 300, 400]

my_list2 = [1, 2, 3]
goo(my_list2)
print(my_list2)