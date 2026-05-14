def bekeres():
    szo = input("Adj meg A-val kezdődő szavakat!")
    if szo == "end":
        print("Vége a beírásnak")
        return "end"
    while not szo.lower().startswith("a"):
        szo = input("Csak A-val kezdődő szót adhatsz meg!")
    return szo

def parameteres():
    szavak = []
    szo = bekeres()
    while szo != "end":
        szavak.append(szo)
        szo = bekeres()
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

def teljes():
    szavak = parameteres()
    lista_kiir(szavak)
    print()
    leghosszabb(szavak)
    atlag(szavak)