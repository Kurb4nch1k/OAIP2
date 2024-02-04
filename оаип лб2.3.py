import json
with open('person.json', 'r') as file:
    data = json.load(file)
key = input("Поменять значение: ")
newValue = input("Новое значение: ")
data[key] = newValue
with open('data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False)
