import json

person = {
    "name" : "Kendra",
    "age" : 24,
    "city" : "New York",
    "hasChildren" : False,
    "title" : ["engineer", "programmer"]
}

personJson = json.dumps(person, indent=4, sort_keys=True)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

print(person)
print(personJson)