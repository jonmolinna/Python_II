#******************** CHALLENGE 1 *************************** */
# CHALLENGE 1: REVERSE A STRING
# Return a string in reverse
# ex. reverseString('hello') === 'olleh'
def pregunta1(cadena):
    inversa = cadena[::-1]
    print(inversa)

#pregunta1("hello")


#******************** CHALLENGE 2 *************************** */
# CHALLENGE 2: VALIDATE A PALINDROME
# Return true if palindrome and false if not
# ex. isPalindrome('racecar', 'oso') === 'true', isPalindrome ('hello') == false
def pregunta2(cadena):
    cadena = cadena.lower()
    inversa = cadena[::-1]
    print(cadena == inversa)

#pregunta2('Racecar')


#******************** CHALLENGE 3 *************************** */
# CHALLENGE 3: REVERSE AN INTEGER
# Return an integer in reverse
# ex. reverseInt(521) === 125
def pregunta3(numero):
    cadena = str(numero)
    inversa = cadena[::-1]
    remplaza = inversa.replace('-','')
    number = int(remplaza)
    signo = 0
    if numero > 0:
        signo = number * 1
    else:
        signo = number * -1
    print(signo)

#pregunta3(-5021)


#******************** CHALLENGE 4 *************************** */
# CHALLENGE 4: CAPITALIZE LETTERS
# Return a string with the first letter of every word capitalized
# ex. capitalizeLetters('i love python') === 'I Love Python'
def pregunta4(cadena):
    cadena = cadena.lower()
    arreglo = cadena.split()
    nuevo = list(map(lambda char: char[0].upper() + char[1:], arreglo))
    unido = ' '.join(nuevo)

    print(unido)

#pregunta4('i LOVE python')
#---------------------------------------Hazlo tambien con expresiones regulares


#******************** CHALLENGE 5 *************************** */
# CHALLENGE 5: MAX CHARACTER
# Return the character tha is most common in a string
# ex. maxCharacter('javascripth) == 'a'
def pregunta5(cadena):
    cadena = cadena.lower()
    arreglo = list(cadena)

    i=0
    letra = ''
    count = 0
    while i < len(arreglo):
        if arreglo.count(arreglo[i]) > count:
            count = arreglo.count(arreglo[i])
            letra = arreglo[i]
        i = i + 1

    print(count, letra)

#pregunta5('javascripth')


#******************** CHALLENGE 6 *************************** */
# CHALLENGE 6: FIZZBUZZ
# Write a program that prints all the numbers fron 1 to 
# 100. For multiples of 3, instead of the number, print
# "Fizz", for multiples of 5 print "Buzz", for numbers
# which are multiples of both 3 and 5, print "FizzBuzz"
def pregunta6():
    i = 1
    while i <= 100:
        if i%15 == 0:
            print(i, "FizzBuzz")
        elif i%3 == 0:
            print(i, "Fizz")
        elif i%5 == 0:
            print(i, "Buzz")
        else:
            print(i)
        i = i + 1

#pregunta6()