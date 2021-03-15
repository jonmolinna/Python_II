mydict = {"name" : "Max", "age" : 28, "city" : "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

try:
    print(mydict["lastname"])
except:
    print("Error")

mydict_cpy = mydict.copy()

mydict_cpy["email"] = "tucorreo@gmail.com"
print(mydict_cpy)
print(mydict)


#----------- Actualizando un diccionario
mydict.update(mydict2)
print(mydict)
