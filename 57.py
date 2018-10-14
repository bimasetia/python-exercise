line = input("Enter Values:")
line_list = line.split(",")
with open("user_data.txt", 'a+') as file:
    for i in line_list:
        file.write(i + "\n")
