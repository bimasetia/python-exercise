from math import pi
def liquid(h, r=10):
    lv = ((4*pi*r**3) / 3) - ((pi*(h**2)*(3*r-h)) / 3)
    return lv

print(liquid(2))
