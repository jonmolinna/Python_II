result = 5 * 7
print(result)

result2 = 2 ** 4
print(result2)

zeros = [0, 1] * 10
print(zeros)

numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
print(last)

dict_a = {'a' : 1, 'b' : 2}
dict_b = {'c' : 3, 'd' : 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)