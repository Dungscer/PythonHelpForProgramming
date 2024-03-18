# importáljuk a random nevű könyvtárat a használhathoz
import random;

# Mivel egy végtelen programot szeretnénk ezért csinálunk egy végtelen ciklust
# Persze a végtelen ciklusokat inkább kerüljük az életbe előfordulnak élethelyzetek 
# amikor használni kell

print("Melyik számra gondoltam")
probalkozasok = 10
random_szam = random.randint(0,100)
run = True

while run:
    felhaszanlo_valasz = int(input())
    if(probalkozasok > 0):
        if(random_szam == felhaszanlo_valasz):
            print("A válasz helyes győztél")
            run = False
        else:
            print("A válasz helytelen")
            probalkozasok -= 1
            print("Hátralévő probálkozások száma %s" % (probalkozasok+1))
    else:
        print("Elfogyott az összes probálkozásod")
        print("A helyes megoldás a %s volt" % (random_szam))
        random_szam = random.randint(0,100)
        probalkozasok += 10


    