import json
age = 0
people = 0
with open('personlist.json', 'r') as file:
   data = json.load(file)

for person_key,  person_data in data.items():
    if (person_data ['city'] == "Moscow"):
        print("name:", person_data['name'])
        print("age:", person_data['age'])
        people = people + 1
        age = age + person_data['age']



print(people)
print(age)
print("Average age:", age/people)