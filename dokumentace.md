# du1.py

Program du1.py pro zvolené válcové tečné zobrazení, měřítko a poloměr Země vypočítá souřadnice rovnoběžek a poledníku po 10 stupních.  


### Popis 
Po spuštění programu je uživatel dotázán na zvolené válcové tečné zobrazení. Zadáním "A" bude počítáno Marinovo zobrazení, "L" pro Lambertovo zobrazeni, "B" pro Braunovo zobrazení, "M" pro Mercatorovo zobrazení. 

Dalším vstupním paramtetrem je meřítko. Měřítko se zadává v formátu 1:"vstup" a musí být celočíselné.

Uživatel následně může zadat volitelný poloměr Země v kilometrech. Nemusí se jednat o celé číslo. Zadáním hodnoty "0" bude pro výpočet použit přednsatavený poloměr Země 6371.11 km.

Po korektním zadáním všech vstupů dojde k výpočtu.

Výstupem jsou dva seznamy rovnoběžek <-90;90> a poledníku <-180;180>, kde jsou po deseti stupních vypsány souřadnice v centimetrech. Pokud hodnota přesahuje jeden metr, je místo ní vypsána "-". 


### Ukázka běhu programu
```
Jaké zobrazení: B  
Jaké měřítko: 60000000  
Zadáš i poloměr?: 0    
Rovnoběžky:  [-21.2, -17.8, -14.9, -12.3, -9.9, -7.7, -5.7, -3.7, -1.9, 0.0, 1.9, 3.7, 5.7, 7.7, 9.9, 12.3, 14.9, 17.8, 21.2]  
Poledníky:  [-33.4, -31.5, -29.7, -27.8, -25.9, -24.1, -22.2, -20.4, -18.5, -16.7, -14.8, -13.0, -11.1, -9.3, -7.4, -5.6, -3.7, -1.9, 0.0, 1.9, 3.7, 5.6, 7.4, 9.3, 11.1, 13.0, 14.8, 16.7, 18.5, 20.4, 22.2, 24.1, 25.9, 27.8, 29.7, 31.5, 33.4]
```
