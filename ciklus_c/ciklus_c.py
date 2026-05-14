def bekeres():
    szo = input("Adj meg A-val kezdődő szavakat!")
    while not szo.lower().startswith("a"):
        szo = input("Csak A-val kezdődő szót adhatsz meg, írd be újra!")
    return szo

def parameteres(x):
    szavak = []
    for i in range(x):
        szavak.append(bekeres())
    return szavak

def lista_kiir(szavak):
    for i in range(len(szavak)):
        if i == len(szavak) -1:
            print(szavak[i], end="")
        else: 
            print(szavak[i], end="%")

#Maximum
def leghosszabb(lista):
    max_hely = lista[0]
    for i in range((len(lista))):
        if len(lista[i]) > len(max_hely):
            max_hely = lista[i]
    return print(f"Leghosszabb szó {max_hely}")

def atlag(lista):
    ossz_karakter = 0
    for i in lista:
        ossz_karakter += len(i)
    return print(round(ossz_karakter /len(lista),1))

def teljes(x):
    szavak = parameteres(x)
    lista_kiir(szavak)
    print()
    leghosszabb(szavak)
    atlag(szavak)