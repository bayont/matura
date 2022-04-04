import math

f = open("../punkty.txt", "r") # otwieramy plik metodą open, pierwszy parametr to ścieżka do pliku, a drugi parametr to sposób dostępu. W tym przypadku wybieramy "r", czyli read, bo potrzebujemy tylko dostępu do odczytu z pliku.
wynik = open("wyniki4.txt", "w", encoding="utf-8") # tak jak wyżej, tylko używamy sposobu dostępu "w", czyli write, ponieważ będziemy zapisywać wyniki do tego pliku. Używamy również parametru encoding, aby nasz program otworzył plik z kodowaniem utf-8, żeby obsłużyć polskie znaki.

wyniki = []

punkty = [] # tworzymy tablicę w której umieścimy odpowiednio zmodyfikowane dane z pliku

# przygotowujemy dane wejściowe, aby łatwiej nam się wykonywało zadania
for line in f: #dla każdego wiersza w pliku
    bezBialychZnakow = line.strip() #usuwamy 
    podzielony_wiersz = bezBialychZnakow.split(" ")
    x = int(podzielony_wiersz[0])
    y = int(podzielony_wiersz[1])
    punkty.append([x, y])
# nasza struktura wygląda tak punkty = [[wsp_x_punktu, wsp_y_punktu], ...]

#
# Zadanie 1
#

# Musimy policzyć punkty, których obie współrzędne są liczbami pierwszymi. Liczba pierwsza to jak wiecie liczba która dzieli się tylko przez jeden i przez samą siebie. Więc stworzymy prostą funkcję, którą każdy da radę zbudować.

def czy_pierwsza(liczba):
    for n in range(2, liczba):
        if liczba % n == 0:
            return False
    return True


licz_pierwsze = 0
for punkt in punkty:
    if czy_pierwsza(punkt[0]) and czy_pierwsza(punkt[1]):
        licz_pierwsze += 1

wyniki.append("Wynik 4.1: "+ str(licz_pierwsze) + "\n")

#
# Zadanie 2
#

# W tym zadaniu musimy policzyć punkty, których współrzędne są cyfropodobne według siebie, to znaczy, że te liczby muszą składać się dokładnie z tych samych cyfr. Najmniej czasochłonnym sposobem będzie wrzucenie do listy wszystkich cyfr osobno i porównanie tej listy z drugą współrzędną punktu.

ile_cyfropodobnych = 0
for punkt in punkty:
    cyfry = []
    for cyfra in str(punkt[0]):
        if not cyfra in cyfry:
            cyfry.append(cyfra)
    cyfry_2 = []
    for cyfra in str(punkt[1]):
        if not cyfra in cyfry_2:
            cyfry_2.append(cyfra)
    if len(cyfry) == len(cyfry_2):
        cyfropodobna = True
        cyfry.sort()
        cyfry_2.sort()
        for i in range(len(cyfry)):
            if cyfry[i] != cyfry_2[i]:
                cyfropodobna = False
                break
        if cyfropodobna == True:
            ile_cyfropodobnych += 1

wyniki.append("Wynik 4.2: "+ str(ile_cyfropodobnych) + "\n")

#
# Zadanie 3
#

# W tym zadaniu musimy podać współrzędne punktów, które są najbardziej oddalonymi od siebie punktami względem reszty. W tym zadaniu mamy podany wzór na odległość punktów na płaszczyźnie i z niego skorzystamy. Musimy sprawdzić każdy punkt z każdym, żeby określić która para jest najdalej. Trzeba pamiętać że odległość ma być zaokrąglona do liczby całkowitej.

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

wyniki.append(f"Wynik 4.3: Najdalej położone od siebie punkty: {max_para[0]} {max_para[1]}, a odległość między nimi to {max_odleglosc}\n")


#
# Zadanie 4
#

# W tym zadaniu musimy wyobrazić sobie kwadrat którego środkiem jest początek układu współrzędnych gdzie leżą nasze punkty, a boki tej figury są równoległe do osi układu. Szukamy takich punktów które znajdują się: a) wewnątrz kwadratu (bez tych leżących na bokach) b) na bokach kwadratu c) na zewnątrz kwadratu. Czyli wierzchołki kwadratu leżą na +/- 5000 x i y

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

wyniki.append(f"Wynik 4.4: a) punkty leżące wewnątrz kwadratu: {punkty_a} b) punkty leżące na krawędziach kwadratu {punkty_b} c) punkty leżące poza kwadratem {punkty_c}\n")


#
# Zapisywanie wyników do pliku
#

wynik.writelines(wyniki) # Zapisujemy wcześniej przygotowaną listę z wynikami

f.close() # zamykamy strumień związany z czytaniem pliku, żeby zwolnić zajęte miejsce w pamięci ulotnej
wynik.close() # tak jak wyżej