import json

with open('company1.json', 'r+') as file:
    d = json.loads(file.read())
    d["employees"].append({"firstName": "Arnold","lastName": "Swagger"})
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
