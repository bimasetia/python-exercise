def count_word(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        check = string.replace(',', ' ')
        return len(check.split())


print(count_word("/Users/dedisetyadi/Desktop/words2.txt"))
