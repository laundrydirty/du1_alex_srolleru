from math import sin, tan, pi, e, log

# vstupy zobrazeni a mertika
z = input("Jaké zobrazení: ")
m = int(input("Jaké měřítko: "))

if m <= 0:
    # pri meritku mensim nebo rovnem nule je vypsana chybova hlaska a program skonci
    print("špatný formát měřítka, zkus to prosím znova")
    exit()

# vstup volitelny polomer
r = float(input("Zadáš i poloměr?:"))

if r == 0:
    # pri zadani 0, je pouzit prednastaveny polomer
    r = 6371.11
elif r > 0:
    # pri polomeru vetsim nebo rovnem nule je pouzit vstup
    r = r
else:
    # pri spatnem vstupu polomeru je vypsana chybova hlaska a program skonci
    print("špatný formát poloměru, zkus to prosím znova")
    exit()

# prazdne seznamy rovnobezek a poledniku
rovno = []
pole = []

# vypocet vzdalensti poledniku pro vsechna zobrazeni stejna
for i in range(37):
    # vzorec pro vypocet vzdalenosti po 10 stupnich
    x = r * ((-180 + (i * 10)) * pi / 180)
    # prevod na centimetry a podeleni meritkem
    x = x * 100000 / m
    # zaokrouhleni na jedno desetinne misto
    x = round(x, 1)
    if x > 100 or x < -100:
        # pokud vzdalenost presahne jeden metr, zapise se do seznamu pomlcka
        pole.append('-')
    else:
        # jinak je vzdalenost zapsana do seznamu
        pole.append(x)

# vypocet vzdalenosti rovnobezek pro jednotliva zobrazeni
if z == 'A':
    # Marinovo zobrazeni
    for j in range(19):
        y = r * ((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'L':
    # Lambertovo zobrazeni
    for j in range(19):
        y = r * sin((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'B':
    # Braunovo zobrazeni
    for j in range(19):
        y = 2 * r * tan((-90 + (j * 10)) * pi / 360)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'M':
    # Mercatorovo zobrazeni
    for j in range(19):
        if j == 0 or j==18:
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
            rovno.append('-')
        else:
            rovno.append(y)
else:
    # pri spatnem vstupu zobrazeni je vypsana chybova hlaska a program skonci
    print("Toto zobrazení neznám, prosím zkus to znovu.")
    exit()

# vypsani vzdalenosti rovnobezek a poledniku
print("Rovnoběžky: ", rovno)
print("Poledníky: ", pole)

