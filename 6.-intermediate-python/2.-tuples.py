my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple.count('p')) # 2

print(my_tuple.index('p')) # indece 1


# Convertiendo una Tupla a un arreglo o viciversa
my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = numeros[::-1]

print(b)