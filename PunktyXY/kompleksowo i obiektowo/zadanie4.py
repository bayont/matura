import math

class Sito:
    pierwsze = []
    def __init__(self, n):
        n=n+1
        self.pierwsze = [True]*(n)
        for i in range(2, int(math.sqrt(n))):
            if self.pierwsze[i] == True:
                for j in range(2*i, n, i):
                    self.pierwsze[j] = False
    def czyPierwsza(self, liczba):
        return self.pierwsze[liczba]


class Punkt:
    x=0
    y=0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def czyObieWspolrzednePierwsze(self):
        return sito.czyPierwsza(self.x) and sito.czyPierwsza(self.y)
    def czyCyfropodobny(self):
        return sorted(dict.fromkeys(str(self.x))) == sorted(dict.fromkeys(str(self.y)))
    def dajBezwzgledny(self):
        return Punkt(abs(self.x), abs(self.y))
    @staticmethod
    def dajDystans(p1, p2):
        return round(math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2))
    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

class Polozenie:
    wewnatrz=False
    w_srodku=False
    na_zewnatrz=False
    poz=-1
    def __init__(self, pozycja) -> None:
        if pozycja == 0:
            self.wewnatrz = True
        elif pozycja == 1:
            self.w_srodku = True
        else:
            self.na_zewnatrz = True
        self.poz = pozycja
    def __str__(self) -> str:
        return (self.wewnatrz and "wewnątrz") or (self.w_srodku and "na krawędzi") or (self.na_zewnatrz and "na zewnątrz")


class Kwadrat:
    srodek=0
    dlKrawedzi=0
    def __init__(self, srodek, dlKrawedzi):
        self.srodek = srodek
        self.dlKrawedzi = dlKrawedzi
    def dajPolozeniePunktu(self, punkt):
        bezwzgledny = punkt.dajBezwzgledny()
        if ((bezwzgledny.x < self.dlKrawedzi/2) and (bezwzgledny.y < self.dlKrawedzi/2)):
            return Polozenie(0)
        elif bezwzgledny.x == self.dlKrawedzi/2 or bezwzgledny.y == self.dlKrawedzi/2:
            return Polozenie(1)
        else:
            return Polozenie(2)
        
class Plik:
    f=None
    def __init__(self, sciezka, mode="r", encoding="utf-8") -> None:
        self.f = open(sciezka, mode, encoding=encoding)
    def pisz(self, linie):
        self.f.writelines(linie)

    def czytajWszystkoWPunktach(self):
        punkty = []
        for linia in self.f:
            linia = linia.strip()
            [x, y] = linia.split()
            punkty.append(Punkt(int(x), int(y)))
        return punkty
        

class Zadanie:
    nr=""
    odp=""
    def __init__(self) -> None:
        self.rozwiaz()
    def rozwiaz(self):
        pass
    def __str__(self) -> str:
        return f"Zadanie {self.nr} | {self.odp}"
    



sito = Sito(10000)
plik = Plik("../punkty.txt")
wynik = Plik("./wyniki4.txt", "w")
punkty = plik.czytajWszystkoWPunktach()


class Zadanie1(Zadanie):
    def __init__(self) -> None:
        super().__init__()
        self.nr="1"
    def rozwiaz(self):
        pierwsze = 0
        for p in punkty:
           if p.czyObieWspolrzednePierwsze():
               pierwsze += 1
        self.odp = pierwsze
        return super().rozwiaz()

class Zadanie2(Zadanie):
    def __init__(self) -> None:
        super().__init__()
        self.nr="2"
    def rozwiaz(self):
        cyfropodobne = 0
        for p in punkty:
           if p.czyCyfropodobny():
               cyfropodobne += 1
        self.odp = cyfropodobne
        return super().rozwiaz()

class Zadanie3(Zadanie):
    def __init__(self) -> None:
        super().__init__()
        self.nr="3"
    def rozwiaz(self):
        max_odleglosc = 0
        max_para = []
        for i in range(len(punkty)):
            for j in range(i+1, len(punkty)):
                p1 = punkty[i]
                p2 = punkty[j]
                dystans = Punkt.dajDystans(p1, p2)
                if dystans > max_odleglosc:
                    max_odleglosc = dystans
                    max_para = [p1, p2]
        self.odp = f"Te punkty to {max_para[0]} i {max_para[1]}, a dystans to {max_odleglosc}"
        return super().rozwiaz()


kwadrat = Kwadrat(Punkt(0, 0), 10000)
class Zadanie4(Zadanie):
    def __init__(self) -> None:
        super().__init__()
        self.nr="4"
    def rozwiaz(self):
        wewnatrz = 0
        srodek = 0
        zewnatrz = 0
        for p in punkty:
            poz = kwadrat.dajPolozeniePunktu(p).poz
            if poz == 0:
               wewnatrz += 1
            elif poz == 1:
                srodek += 1
            else:
                zewnatrz += 1 
            
        self.odp = f"Kwadrat o krawędzi {kwadrat.dlKrawedzi}, o srodku {kwadrat.srodek}, a wewnątrz jest: {wewnatrz} pkt., na krawędzi leżą {srodek} pkt., na zewnątrz jest {zewnatrz} pkt."
        return super().rozwiaz()

linie = [str(Zadanie1())+'\n', str(Zadanie2())+'\n', str(Zadanie3())+'\n', str(Zadanie4())+'\n']
wynik.pisz(linie)