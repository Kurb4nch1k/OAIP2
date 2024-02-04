import json
person = {
            "Фамилия": "Курбанов",
            "Имя": "Илья",
            "Отчество": "Алексеевич",
            "Телефон": "+79638089662",
            "Год рождения": "2006",
            "Город рождения": "Благовещенск",
            "Место учёбы": "БГПУ"
            }
with open("person.json", "w") as file:
    json.dump(person, file, ensure_ascii=False)