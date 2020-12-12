companies= [
    {"name": "Company One", "category": "Finance", "start": 1981, "end": 2004},
    {"name": "Company Two", "category": "Retail", "start": 1992, "end": 2008},
    {"name": "Company Three", "category": "Auto", "start": 1999, "end": 2007},
    {"name": "Company Four", "category": "Retail", "start": 1989, "end": 2010},
    {"name": "Company Five", "category": "Technology", "start": 2009, "end": 2014},
    {"name": "Company Six", "category": "Finance", "start": 1987, "end": 2010},
    {"name": "Company Seven", "category": "Auto", "start": 1986, "end": 1996},
    {"name": "Company Eight", "category": "Technology", "start": 2011, "end": 2016},
    {"name": "Company Nine", "category": "Retail", "start": 1981, "end": 1989}
  ]
  
ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32]

# -------------------- Pregunta 1
# Imprime las companias usando for
# for company in companies:
#     print(company)


# -------------------- Pregunta 2
# Imprime las companias usando while
# i = 0
# while i < len(companies):
#     print(companies[i])
#     i = i + 1


# -------------------- Pregunta 3
# Imprime mayor o igual a 21 años con for y filter
mayor20 = list(filter(lambda a: a>=21, ages))

nuevoAges = []
for age in ages:
    if age >= 21:
        nuevoAges.append(age)

#print(mayor20)
#print(nuevoAges)


# -------------------- Pregunta 4
# Imprime las companias de retail
retail = list(filter(lambda company: company.get('category') == 'Retail', companies))
#print(retail)


# -------------------- Pregunta 5
# Obtiene todas las empresas de los años 80
ages80 = list(filter(lambda company: company.get('start') >= 1980 and company.get('start') <= 1989, companies))
#print(ages80)


# -------------------- Pregunta 6
# Imprima las companias que duraron 10 años o mas
ages10 = list(filter(lambda compania: compania.get('end') - compania.get('start') >= 10, companies))
#print(ages10)


# -------------------- Pregunta 7
# Crea un array solo con nombre de la compania
companyName = list(map(lambda company: company.get('name'), companies))
#print(companyName)


# -------------------- Pregunta 8
# Eleva al cuadrado las edades
edadCuadrado = list(map(lambda edad: edad * edad, ages))
#print(edadCuadrado)


# -------------------- Pregunta 9
import math
edadRaiz = list(map(lambda edad: math.sqrt(edad), ages))
#print(edadRaiz)


# -------------------- Pregunta 10
# Ordena el arreglo por la fecha de la creacion de la empresa
ordenFechaCreacion = sorted(companies, key=lambda company: company.get('start'))
#print(ordenFechaCreacion)


# -------------------- Pregunta 11
# Ordena las edades de menor a mayor
ordenEdad = sorted(ages, key=lambda edad: edad)
#print(ordenEdad)


# -------------------- Pregunta 12
# Suma toda las edades
from functools import reduce
sumaEdad = reduce(lambda a,b: a+b, ages)
#print(sumaEdad)

# Usando for
suma = 0
for edad in ages:
  suma = suma + edad

#print(suma)


# -------------------- Pregunta 13
# Obtener la suma total de los años de la compania
sumatotal = 0

for company in companies:
  sumatotal = sumatotal + (company.get('end') - company.get('start'))

print(sumatotal)