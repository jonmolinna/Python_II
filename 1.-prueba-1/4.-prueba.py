# CHALLENGE 1: LONGEST WORD
# Return the longest word of a string
# if more than one longest word, put into an array
# ex. longestWord('Hello, my name is brad') == 'hello'
# ex. longestWord('Hello there, my name is Brad') == ['hello, there']



# CHALLENGE 2: ARRAY CHUNKING
# Split an array into chunked arrays of a specific length
# ex. chunkArray([1,2,3,4,5,6,7], 3) === [[1,2,3], [4,5,6], [7]]
# ex. chunkArray([1,2,3,4,5,6,7], 2) === [[1,2],[3,4],[5,6],[7]]
def pregunta2(arreglo, numero):
    i = 0
    arr = []

    while i < len(arreglo):
        arr.append(arreglo[i:i+numero])
        i = i + numero
    print(arr)

#pregunta2([1,2,3,4,5,6,7], 3)


# CHALLENGE 3: FLATTEN ARRAY
# Take an array of arrays and flatten to a single array
# ex. [[1,2], [3,4], [5,6], [7]] = [1,2,3,4,5,6,7]
from functools import reduce

def pregunta3(arreglo):
    nuevo = reduce(lambda a,b: a+b, arreglo)
    print(nuevo)

#pregunta3([[1,2], [3,4], [5,6], [7]])


# CHALLENGE 4: ANAGRAM
# Return true if anagram and false if not
# ex. 'elbow' === 'below'
# ex. 'Dormitory' === 'dirty room##'