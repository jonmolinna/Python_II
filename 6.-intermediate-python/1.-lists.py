myList = ["banana", "cherry", "apple"]
number = [4, 3, 1, -1, -5, 10]

# item = myList[-1]
# print(item)

# Insertar dato a un arreglo
myList.append("lemon")

# Insertando por indice
myList.insert(1, "blueberry")

# eliminando elementos
item = myList.remove("cherry")

# Ivertiendo un Arreglo
# myList.reverse()


# Ordenando un Arreglo
new_list = sorted(number)
#print(new_list)


#----------------------------------
myList2 = [0] * 5
#print(myList2)

myList3 = [1, 2, 3, 4, 5]

nueva_lista = myList2 + myList3
#print(nueva_lista)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = numberList[1:5] #[2, 3, 4, 5]
#print(a)

numberList2 = [1, 2, 3, 4, 5, 6]
b = [x*x for x in numberList2]

print(b)