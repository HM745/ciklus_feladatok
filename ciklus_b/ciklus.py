import random

def veletlen_szam():
    szam = random.randint(1,6)
    return szam

def parametes(k):
    szamok = []
    for i in range(k):
        szamok.append(veletlen_szam())
    return szamok

def elvalasztas(szamok):
    for i in range(len(szamok)):
        if i == len(szamok) -1:
            print(szamok[i], end="") 
        else:
            print(szamok[i], end="!")
#Megszámlálás tétel
def megszamlalas(szamok):
    db = 0
    for i in szamok:
        if i == 4:
            db += 1
    return print(f"4-esek száma: {db}")
#lista = [5,2, 2,1,3,6]
#min/max tétel 
def legkisebb(lista): 
    min_hely = lista[0]
    for i in range(len(lista)):
        if lista[i] < min_hely:
            min_hely = lista[i]
    return print(f"Legkisebb szám: {min_hely}")
            
        
def teljes(x):
    szamok = parametes(x)
    elvalasztas(szamok)
    print()
    megszamlalas(szamok)
    legkisebb(szamok)