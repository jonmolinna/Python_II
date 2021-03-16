# Strings: ordered, inmutable, text representacion
my_string = "Hello World"
#substring = my_string[1:5]
substring = my_string[::-1]
print(substring) # ello

my_string2 = '   Hello World   '
my_string2 = my_string2.strip()
print(my_string2)

my_string3 = 'Hello World'
print(my_string3.find('lo')) # 3 indice
print(my_string3.find('pp')) # -1 no encuentra

print(my_string3.count('o')) # 2

my_string4 = 'how are you doing'
my_string4 = my_string4.split()
print(my_string4) # ['how', 'are', 'you', 'doing']

var = "Brehn"
my_string5 = "the variable is %s" % var
print(my_string5)

var2 = "Eung"
var3 = 24
my_string6 = f"the variable is {var2} and {var3}"
print(my_string6)