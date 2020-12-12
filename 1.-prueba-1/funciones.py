# upper() => Convierte en Mayuscula.
# lower() => Convierte en Minuscula.
# capitalize() => Pone las primeras letras en mayusculas.
# str() => Convierte un numero a string.
# int() => Convierte un string a numero.
# list() => Convierte un cadena a un arreglo.

# append() => permite ingresar datos a un arreglo
# insert() => Ingresa un dato a un arreglo mediante un indice.
# extend() => Ingresa varios datos a un array.

# ---------------- Funcion de Join -------------------------------------
# Permite unir un arreglo a una cadena
# Formula => 'Separador'.join(paises)
paises = ['Argentina', 'Uruguay', 'Chile', 'Paraguay', 'Brasil', 'Bolivia', 'Peru']
paisesCadena = ','.join(paises)
#print(paisesCadena)


# ---------------- Funcion de Split -------------------------------------
# Convierte una cadena a una lista o arreglo
# formula => nombreString.split()
nombreString = 'Mi nombre es Eung'
nombreLista = nombreString.split()

nombresSeparados = ''' Eung
Nikone
Brehn'''
nombreLista2 = nombresSeparados.split(sep='\n')

nombre = 'Nikone'
nombreLista3 = list(nombre)
#print(nombreLista3)


# ---------------- Funcion de Reverse -------------------------------------
# Invierte los elementos de la lista (OJO No retorna nada)
sistemas = ['Windows', 'macOS', 'Linux']
sistemas.reverse()

frutas = ['Mango', 'Platano', 'Papaya', 'Sandia']
frutasInvertida = frutas[::-1]

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
# for dia in reversed(dias):
#     print(dia)


# ---------------- Funcion de Sort y Sorted -------------------------------------
# El metodo sort() ordena los elementos de una lista determinada en un orden ascendente o descendente
vocales = ['e', 'a', 'u', 'o', 'i']
vocales.sort()

ordenado = sorted(vocales)

vocales2 = ['e', 'a', 'u', 'o', 'i']
vocales2.sort(reverse=True)

descendiente = sorted(vocales2, reverse=True)

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

# sort by name (Ascending order)
#employees.sort(key=get_name)
#print(employees, end='\n\n')

# sort by Age (Ascending order)
ordenAscendenteAge = sorted(employees, key=get_age)
#print(ordenAscendenteAge, end='\n\n')

# sort by salary (Descending order)
#employees.sort(key=get_salary, reverse=True)
#print(employees, end='\n\n')


employees2 = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
#employees2.sort(key=lambda x: x.get('Name'))
#print(employees2, end='\n\n')

# sort by Age (Ascending order)
#employees2.sort(key=lambda x: x.get('age'))
#print(employees2, end='\n\n')

# sort by salary (Descending order)
#employees2.sort(key=lambda x: x.get('salary'), reverse=True)
#print(employees2, end='\n\n')


# ---------------- Funcion de Reduce -------------------------------------
from functools import reduce

arregloNumeros = [1,5,3,2,6]

def reduce_array(a,b):
    return a+b

suma = reduce(reduce_array, arregloNumeros)
#print(suma)



# ---------------- Funcion de Filter -------------------------------------
array = [1,5,3,2,6]
def filter_array(number):
  return number > 3
filtered_array = list(filter(filter_array, array))
#print(filtered_array)

arregloNumeros2 = [2, 5, 10, 23, 50, 33]

def multiple(numero):
    if numero % 5 == 0:
        return True

resultado = list(filter(multiple, arregloNumeros2))
#print(resultado)

# Usando lambda
resultado2 = list(filter(lambda numero: numero%5 == 0, arregloNumeros2))
#print(resultado2)


# ---------------- Funcion de Slice -------------------------------------
# arreglo[2,4] => la primera lo incluye y la segunda los excluye
arregloVocales = ['a', 'e', 'i', 'o', 'u']
resultado3 = arregloVocales[2:4]
resultado4 = arregloVocales[0:5]
# vocales[:3] => vocales[0:3]
# vocales[:] => trae toda la lista
# vocales[3:] => trae del indice tres hasta el final
#print(resultado3)


# ---------------- Funcion de Map -------------------------------------
arregloNumeros3 = [11, 25, 34, 100, 23]

def add_five(x):
    return x + 5

resultado5 = list(map(add_five, arregloNumeros3))
#print(resultado5)

# usando map y lambda
resultado6 = list(map(lambda x: x+5, arregloNumeros3))
#print(resultado6)


# ---------------- Funcion de Lambda -------------------------------------
# Son funciones anonimas
sumaNumeros = lambda x,y : x+y
#print(sumaNumeros(4 , 5))

raizCuadrado = lambda x : x**2
#print(raizCuadrado(5))


# ---------------- Funcion de Substring -------------------------------------
# primer indice esta incluido y el segundo no
cadena = 'aeiou'
ini = 1 # Posicion inicial de la subcadena
fin = 3 # Posicion final de la subcadena (excluida)
subcadena = cadena[ini:fin]
#print(subcadena)

cadena2 = 'esta es nuestra cadena'

# Obtenemos la subcadena desde el principio hasta la posicion 10
subcadena2 = cadena2[:10]

# Obtenemos la subcadena desde la posicion 10 hasta el final
subcadena3 = cadena2[10:]

# Obtenemos los ultimos 10 caracteres de la cadena
subcadena4 = cadena2[-10:]

#print(subcadena4)


cadena3 = 'abcdefghijklmnopqrstuvwxyz'

indice_c = cadena3.index('c') #obtenemos la posición del carácter c
indice_h = cadena3.index('h') #obtenemos la posición del carácter h

subcadena5 = cadena3[indice_c:indice_h]
#print(subcadena5)

#si queremos incluir en la subcadena el elemento de la posición 
#indice_h basta con sumar 1 a esa posición

subcadena6 = cadena3[indice_c:indice_h + 1]
#print(subcadena6)


# ---------------- Funcion de Find -------------------------------------
# devuelve la posicion de la busqueda, en caso que no encuentre devuelve -1
# Parametros
# sub => substring a buscar
# start => (opcional) comienzo del bloque en el que se va realizar la busqueda
# end => (opcional) final del bloque en que realizara la busqueda

cadena4 = "Python for Data Science"
resultado7 = cadena4.find("Da")
#print(resultado7) # devuelve posicion 11

resultado8 = cadena4.find("da")
#print(resultado8) # devuelve -1

resultado9 = cadena4.find("Data", 0,7)
# print(resultado9) # devuelve -1


# ---------------- Funcion de Count -------------------------------------
# metodo => find("str", posicionIniciar, posicionFinal)

cadena5 = "Bienvenido a mi aplicacion"
resultado10 = cadena5.count('a')
#print(resultado10) # retorna 3


# ---------------- Funcion de Replace -------------------------------------
# Parametros: string.replace(oldvalue, newValue, count)
# oldvalue => Requiere la cadena a buscar
# newvalue => Requiere la cadena para reemplazar en valor anterior
# count => Opcional un numero que especifica cuantas ocurrencias del valor anterior
#           desea reemplazar, el valor predeterminado son todas las apariciones
texto = "one one was a race horse, two two was one too."
nuevoTexto = texto.replace("one", "three")
#print(nuevoTexto)
# salida => three three was a race horse, two two was three too."

nuevoTexto2 = texto.replace("one", "three", 2)
#print(nuevoTexto2)
# salida => three three was a race horse, two two was one too.