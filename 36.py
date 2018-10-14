

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translate():
    user = input("Enter Word:").lower()
    try:
        return d[f"{user}"]
    except KeyError:
        print("We can't find the word")

print(translate())
