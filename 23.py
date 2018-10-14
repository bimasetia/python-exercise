import string

with open("2.txt", 'w+') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
        file.read()
