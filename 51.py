checklist = ["Portugal","Germany","Spain"]
checklist = [i + "\n" for i in checklist]

with open("countries-missing.txt", "r") as file:
    content = file.readlines()

updated_list = sorted(content + checklist)

with open("countries-missing-fixed.txt", 'w') as file:
    for i in updated_list:
        file.write(i)
