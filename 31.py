import json



with open('data.json', 'r') as fp:
    data = json.load(fp)

print(json.dumps(data, indent=4, sort_keys=True))
