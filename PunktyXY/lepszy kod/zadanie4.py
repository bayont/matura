import math


dane = open("../punkty.txt", "r") 
wynik = open("wyniki4.txt", "w", encoding="utf-8")
wyniki,punkty = [],[]

for line in dane:
    podzielony_wiersz = line.strip().split(" ")
    punkty.append([int(podzielony_wiersz[0]), int(podzielony_wiersz[1])])

#
# Zadanie 1
#

def czy_pierwsza(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

punktyPierwsze=0
for punkt in punkty:
    punktyPierwsze += all([czy_pierwsza(punkt[0]),czy_pierwsza(punkt[1])]) and 1 or 0


wynik.write(f"Zadanie 1: {punktyPierwsze}\n")


#
# Zadanie 2
#

cyfropodobne = 0
for punkt in punkty:
    cyfropodobne += sorted(set(str(punkt[0]))) == sorted(set(str(punkt[1]))) and 1 or 0


wynik.write(f"Zadanie 2: {cyfropodobne}\n")

#
# Zadanie 3
#
max_odleglosc = 0
max_para = []
for i in range(len(punkty)):
    for j in range(i+1, len(punkty)):
        p1 = punkty[i]
        p2 = punkty[j]
        odleglosc = round(math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
        if odleglosc > max_odleglosc:
            max_odleglosc = odleglosc
            max_para = [p1, p2]
wynik.write(f"Zadanie 3: Para: [{max_para[0]}] i [{max_para[1]}] | Dystans: {max_odleglosc}\n")

#
# Zadanie 4
#
punkty_a = 0
punkty_b = 0
punkty_c = 0

for punkt in punkty:
    punkt_bezwzgledny = [abs(punkt[0]), abs(punkt[1])]
    if ((punkt_bezwzgledny[0] < 5000) and (punkt_bezwzgledny[1] < 5000)):
        punkty_a += 1
    elif punkt_bezwzgledny[0] == 5000 or punkt_bezwzgledny[1] == 5000:
        punkty_b += 1
    else:
        punkty_c += 1


wynik.write(f"Zadanie 4:\na) punkty leżące wewnątrz kwadratu: {punkty_a}\nb) punkty leżące na krawędziach kwadratu {punkty_b}\nc) punkty leżące poza kwadratem {punkty_c}\n")



dane.close()
wynik.close()