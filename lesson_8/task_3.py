import json

base = {
    '111111': ('Maria', 6),
    '222222': ('Alex', 10),
    '333333': ('Mark', 15),
    '444444': ('Anna', 22),
    '555555': ('Max', 25)
}

with open('file_json.json', 'w') as file:
    json.dump(base, file, indent=4)
