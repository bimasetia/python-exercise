import requests


r = requests.get("http://www.pythonhow.com/data/universe.txt")
word = r.text
print(word.count('a'))
