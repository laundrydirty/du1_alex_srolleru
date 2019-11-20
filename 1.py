from math import sin, tan, pi, e, log

z = input("Jaké zobrazení: ")
m = int(input("Jaké měřítko: "))

# osetreni meritka
if m <= 0:
    print("špatný formát měřítka, zkus to prosím znova")
    exit()
# volitelny polomer
r = float(input("Zadáš i poloměr?:"))

# pokud uzviatel zada 0, bude pouzit prednastaveny polomer
if r == 0:
    r = 6371.11

# pokud uzivatel zada kladne cislo, bude pouzit jeho vstup
elif r > 0:
    r = r

# pokud uzivatel zada neco jineho, vyskoci chybova hlaska
else:
    print("špatný formát poloměru, zkus to prosím znova")
    exit()

# seznamy rovnobezek a poledniku, kam budou ukladany hodnoty
rovno = []
pole = []

# poledniky pro vsechna zobrazeni stejna
for i in range(37):
    x = r * ((-180 + (i * 10)) * pi / 180)
    x = x * 100000 / m
    x = round(x, 1)
    if x > 100 or x < -100:
        pole.append('-')
    else:
        pole.append(x)

# rovnobezky pro zobrazeni
if z == 'A':
    for j in range(19):
        y = r * ((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'L':
    for j in range(19):
        y = r * sin((-90 + (j * 10)) * pi / 180)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'B':
    for j in range(19):
        y = 2 * r * tan((-90 + (j * 10)) * pi / 360)
        y = y * 100000 / m
        y = round(y, 1)
        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

elif z == 'M':
    for j in range(19):
        if j == 9:
            y = 200
        elif j < 9:
            y = r * log(1 / tan((90 - (j * 10)) * pi / 360), e)
            y = y * 100000 / m
            y = round(-y, 1)
        else:
            y = r * log(1 / tan((-90 + (j * 10)) * pi / 360), e)
            y = y * 100000 / m
            y = round(y, 1)

        if y > 100 or y < -100:
            rovno.append('-')
        else:
            rovno.append(y)

# pokud uzivatel zada neco jineho, vyskoci chybova hlaska
else:
    print("toto zobrazení neznám, prosím zkus to znovu")
    exit()

# vypise vysledek
print("Rovnoběžky: ", rovno)
print("Poledníky: ", pole)


