import random

def veletlen():
    szam = random.randint(1,90)
    return szam

def parameter(x):
    szamok = []
    for i in range(x):
        szamok.append(veletlen())
    return szamok

def elvalasztas(szamok):
    for i in range(len(szamok)):
        if i == len(szamok) -1:
            print(szamok[i], end="")
        else: 
            print(szamok[i], end="?")

#MIN/MAX tétel 
def legnagyobb(lista):
    max_hely = lista[0]
    for i in range(len(lista)):
        if lista[i] > max_hely:
            max_hely = lista[i]
    return print(f"Legnagyobb:{max_hely}")

#Megszámlálás tétel
def megszamlalas(szamok):
    db = 0
    for i in szamok:
        if i > 70:
            db +=1
    return print(f"70-nél nagyobb:{db}")

def teljes(x):
    szamok = parameter(x)
    elvalasztas(szamok)
    print()
    legnagyobb(szamok)
    megszamlalas(szamok)