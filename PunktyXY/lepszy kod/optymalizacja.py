#Porównanie dwóch opcji w zadaniu 1

import math
import timeit

dane = open("../punkty.txt", "r") # otwieramy plik metodą open, pierwszy parametr to ścieżka do pliku, a drugi parametr to sposób dostępu. W tym przypadku wybieramy "r", czyli read, bo potrzebujemy tylko dostępu do odczytu z pliku.
wynik = open("wyniki4.txt", "w", encoding="utf-8") # tak jak wyżej, tylko używamy sposobu dostępu "w", czyli write, ponieważ będziemy zapisywać wyniki do tego pliku. Używamy również parametru encoding, aby nasz program otworzył plik z kodowaniem utf-8, żeby obsłużyć polskie znaki.

wyniki = []
punkty = [] # tworzymy tablicę w której umieścimy odpowiednio zmodyfikowane dane z pliku

# przygotowujemy dane wejściowe, aby łatwiej nam się wykonywało zadania
for line in dane: #dla każdego wiersza w pliku
    bezBialychZnakow = line.strip() #usuwamy biale znaki
    podzielony_wiersz = bezBialychZnakow.split(" ")
    x = int(podzielony_wiersz[0])
    y = int(podzielony_wiersz[1])
    punkty.append([x, y])

#
# Zadanie 1
#


# Sito - SZYBSZY
time1 = timeit.default_timer()


pierwsze = [True]*(10000+1)
for i in range(2, int(math.sqrt(10000))+1):
    if pierwsze[i] == True:
        for j in range(2*i, 10000, i):
            pierwsze[j] = False
punktyPierwsze = 0 
for punkt in punkty:
    if pierwsze[punkt[0]] and pierwsze[punkt[1]]:
        punktyPierwsze+=1


time2 = timeit.default_timer()
sito = time2 - time1 # Policzony czas dla wykonania sita

print(f"\nZadanie 1 - z użyciem Sita Erastotenesa: {punktyPierwsze} w czasie: {sito}\n")

#Bez Sita - WOLNIEJSZY

time1 = timeit.default_timer()

def czy_pierwsza(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

punktyPierwsze=0
for punkt in punkty:
    punktyPierwsze += all([czy_pierwsza(punkt[0]),czy_pierwsza(punkt[1])]) and 1 or 0

time2 = timeit.default_timer()
bezSita = time2 - time1 # Policzony czas dla wykonania sita

print(f"Zadanie 1 - bez użycia Sita Erastotenesa: {punktyPierwsze} w czasie: {bezSita}\n")
print(f"Czyli Sito Erastotenesa jest szybsze {round(bezSita/sito, 2)} razy!\n")


dane.close()