# --------------------- Prueba 1
# Programe una funcion que cuente el numero de caracteres de una cadena de texto.
# Ejm miFuncion("Hola Mundo") devolvera 10.
def Pregunta1(texto):
    longitud = len(texto)
    print(longitud)

#Pregunta1("Hola Mundo")


# --------------------- Prueba 2
# Programe una funcion que te devuelva el texto recortando segun el numero de caracteres indicados
# miFuncion("Hola Mundo", 4) devolvera "Hola"
def Pregunta2(texto, numero):
    nuevoTexto = texto[0:numero]
    print(nuevoTexto)

#Pregunta2("Hola Mundo", 4)


# --------------------- Prueba 3
# Programe una funcion que dada una string te devuelva un Array de textos separados por cierto caracter
# Ejm miFuncion("hola que tal", " ") devolvera ['hola', 'que', 'tal']
def Pregunta3(texto):
    nuevoTexto = texto.split()
    print(nuevoTexto)

#Pregunta3("hola que tal")


# --------------------- Prueba 4
# Programe una funcion que repita un texto x veces
# Ejm miFuncion("Hola Mundo", 3) devolvera Hola Mundo Hola Mundo Hola Mundo
def Pregunta4(texto, numero):
    i = 1
    while i <= numero:
        print(texto)
        i = i + 1
    
#Pregunta4("Hola Mundo", 3)


# --------------------- Prueba 5
# Programe una funcion que invierta las palabras de una cadena
# Ejm miFuncion("Hola Mundo") devolvera "odnuM aloH"
def pregunta5(texto):
    inversa = texto[::-1]
    #print(inversa)

    nuevoArreglo = ''
    for char in texto:
        nuevoArreglo = char + nuevoArreglo
    #print(nuevoArreglo)

pregunta5("Hola Mundo")


# --------------------- Prueba 6
# Programe una funcion para contar el numero de veces que se repite una palabra en un texto largo
# Ejm miFuncion("hola mundo adios mundo", "mundo") devolvera 2
def pregunta6(cadena, texto):
    cadena = cadena.lower()
    texto = texto.lower()

    cantidad = cadena.count(texto)
    print(cantidad)

#pregunta6("Hola Mundo adios mundo", "Mundo")



# --------------------- Prueba 7
# Programe una funcion que valide si una palabra o frase dada, es un polidromo
# Que se lee igual en un sentido que en otro
# Ejm miFuncion("Salas") devolvera true
def Pregunta7(texto):
    texto = texto.lower()
    inversa = texto[::-1]
    #print(inversa == texto)

    nuevoTexto = ''
    for char in texto:
        nuevoTexto = char + nuevoTexto
    print(nuevoTexto == texto)

#Pregunta7("Salas")


# --------------------- Prueba 8
# Programe una funcion que elimine cierto patron de caracteres de un texto dado.
# Ejm miFuncion("xyz1, xyz2, xyz3, xyz4 y xyz5", "xyz") devolvera "1,2,3,4,5"
def pregunta8(cadena, letra):
    texto = cadena.replace(letra, '')
    print(texto)

#pregunta8("xyz1, xyz2, xyz3, xyz4, xyz5", "xyz")


# --------------------- Prueba 9
# Programe una funcion que permite obtener numero aleatorio entre 501 y 600
from random import randint, random

numeroAleatorio = randint(501,600)
#print(numeroAleatorio)

numeroAleatorio2 = int(random() * (600 - 501) + 501)
#print(numeroAleatorio2)


# --------------------- Prueba 10
# Programe una funcion que reciba un numero y evalue si es capicua o no
# ejm miFuncion(2002) devuelvera true
def pregunta10(numero):
    letra = str(numero)
    sinSigno = letra.replace("-","")
    invertir = sinSigno[::-1]
    num = int(invertir)
    number = 0
    if(numero >= 0):
        number = num * 1
    else:
        number = num * -1

    print(number == numero)

#pregunta10(-202)


# --------------------- Prueba 11
# Programe una funcion que calcule el factorial de una numero
# El factorial de un entero positivo n, se define como el producto de todos los numeros
# enteros positivos donde 1 hasta n
# miFuncion(5) devolvera 120
def pregunta11(numero):
    i = 1
    total = 1

    while i <= numero:
        total = total * i
        i = i + 1

    print(total)

#pregunta11(5)


# --------------------- Prueba 12
# Programe una funcion que determine si un numero es primo
# (aquel que solo es divisible por si mismo y 1) o no.
# Ejm miFuncion(7) devolver true.
def pregunta12(numero):
    primo = True
    i = 2

    while i < numero:
        if numero%i == 0:
            primo = False
            break
        i = i + 1

    print(primo)

#pregunta12(33)


# --------------------- Prueba 13
# Programe una funcion que determine si un numero es par o impar
# ejm miFuncion(29) devolvera impar
def pregunta12(numero):

    if numero%2 == 0:
        print("El numero es Par")
    else:
        print("El numero es Impar")

#pregunta12(29)


# --------------------- Prueba 14
# Programe una funcion para convertir grados celsius a fahrenheit y viceversa
# Ejm miFuncion(0,"C") devolvera 32 °F
def pregunta14(temperatura, grado):
    grado = grado.upper()

    if grado == "C":
        print(f"{(temperatura * 9/5) + 32} °F")
    elif grado == "F":
        print(f"{(temperatura - 32) * 5/9} °C")
    else:
        print("Solo ingrese C o F")

#pregunta14(0, "F")


# --------------------- Prueba 16
# Programe una funcion que devuelva el monto final despues de aplicar un descuento a una cantidad dada
# Ejm miFuncion(1000, 20) devolvera 800
def pregunta16(numero, descuento):
    
    monto = numero - (numero * descuento)/100
    print(monto)

#pregunta16(1000, 20)


# --------------------- Prueba 18
# programe una funcion que dada una cadena de texto cuente el numero de vocales y consonantes
# Ejm miFuncion("Hola Mundo") devuelve vocales: 4, Consonantes: 5


# --------------------- Prueba 21
# Programe una funcion que dado un array numerico devuelve otro array
# con los numeros elevados al cuadrado
# mifuncion([1,4,5]) devolvera [1,16,25];
def pregunta21(arreglo):
    resultado = list(map(lambda x: x*x, arreglo))
    print(resultado)

#pregunta21([1,4,5])


# --------------------- Prueba 22
# Programe una funcion que dado un array devuelva el numero mas alto y el mas bajo de dicho array
# miFuncion([1,4,5,99,-60]) deolvera [99,-60]
def pregunta22(arreglo):
    mayor = 0
    menor = arreglo[0]

    i = 0
    while i < len(arreglo):
        if(arreglo[i] > mayor):
            mayor = arreglo[i]
        elif(arreglo[i] < menor):
            menor = arreglo[i]
        i = i +1

    print([mayor, menor])

#pregunta22([1,4,5,99,-60])


# --------------------- Prueba 23
# programe una funcion que dado un arreglo de numeros devuelva un objeto con 2 arreglos
# en el primero almacena los numeros pares y en el segundo los impares
# miFuncion([1,2,3,4,5,6,7,8,9,0]) devolvera {pares: [2,4,6,8,0], impares: [1,3,5,7,9]}
def pregunta23(arreglo):
    pares = list(filter(lambda x: x%2==0, arreglo))
    impares = list(filter(lambda x: x%2==1, arreglo))
    print({"pares" : pares, "impares": impares})

#pregunta23([1,2,3,4,5,6,7,8,9,0])


# --------------------- Prueba 24
# Programe una funcion que dado un arreglo de numeros devuelva un objeto con dos arreglos,
# el primero tendra los numeros ordenados en forma ascendente y el segundo en forma descendiente
# ejm miFuncion([7,5,7,8,6]) devolvera {asc: [5,6,7,7,8]}, desc: [8,7,7,6,5]}
def pregunta24(arreglo):
    asc = sorted(arreglo)
    desc = sorted(arreglo, reverse=True)
    objeto = {"asc": asc, "desc": desc}
    print(objeto)

#pregunta24([7,5,7,8,6])