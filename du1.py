from math import sin, tan, pi, e, log

z = input("Jaké zobrazení: ")

# osetreni korektniho zobrazeni
if z != "A" and z != "L" and z != "B" and z != "M":
    print("Toto zobrazení neznám, prosím zkus to znovu.")
    exit()

m = int(input("Jaké měřítko: "))

# osetreni korektniho meritka
if m <= 0:
    print("špatný formát měřítka, zkus to prosím znova")
    exit()

r = float(input("Zadáš i poloměr?: "))

# osetreni korektniho polomeru
if r == 0:
    r = 6371.11
if r < 0:
    print("špatný formát poloměru, zkus to prosím znova")
    exit()

# prazdne seznamy rovnobezek a poledniku
rovnobezky = []
poledniky = []

# vypocet vzdalensti poledniku pro vsechna zobrazeni stejna
for i in range(37):
    x = r * ((-180 + (i * 10)) * pi / 180)
    x = x * 100000 / m
    x = round(x, 1)
    if x > 100 or x < -100:
        # pokud vzdalenost presahne jeden metr, zapise se do seznamu pomlcka
        poledniky.append('-')
    else:
        poledniky.append(x)

# vypocet vzdalenosti rovnobezek pro jednotliva zobrazeni
if z == 'A':
    # Marinovo zobrazeni
    for j in range(19):
        y = r * ((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovnobezky.append('-')
        else:
            rovnobezky.append(y)

elif z == 'L':
    # Lambertovo zobrazeni
    for j in range(19):
        y = r * sin((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovnobezky.append('-')
        else:
            rovnobezky.append(y)

elif z == 'B':
    # Braunovo zobrazeni
    for j in range(19):
        y = 2 * r * tan((-90 + (j * 10)) * pi / 360)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovnobezky.append('-')
        else:
            rovnobezky.append(y)

elif z == 'M':
    # Mercatorovo zobrazeni
    for j in range(19):
        if j == 0 or j == 18:
            y = 200
        elif j < 9:
            y = r * log(1 / tan((90 - (90 - (j * 10))) * pi / 360), e)
            y = y * 100000 / m
            y = round(-y, 1)
        else:
            y = r * log(1 / tan((90 - (- 90 + (j * 10))) * pi / 360), e)
            y = y * 100000 / m
            y = round(y, 1)
        if y > 100 or y < -100:
            rovnobezky.append('-')
        else:
            rovnobezky.append(y)

# vypsani vzdalenosti rovnobezek a poledniku
print("Rovnoběžky: ", rovnobezky)
print("Poledníky: ", poledniky)
