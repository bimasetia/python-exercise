
file = open("user_data.txt", 'a+')

while True:
    line = input("Enter Values:")

    if line == "CLOSE":
        file.close()
        break
    elif line == "SAVE":
        file.close()
        file = open("user_data.txt", 'a+')
        continue
    else:
        file.write(line + "\n")
