def szobekero():
    szo = input("Adj meg egy minimum 3 karakteres szót!")
    while len(szo) < 3:
        szo = input("Hibás! Adj meg egy minimum 3 karakteres szót!")
    return szo

def param_szobekero():
    szavak = []
    szo = ""  
    while szo != "end":
        szo = szobekero()
        if szo != "end":
            szavak.append(szo)
        else: 
            szo == "end"
            print("Vége a szavak beírásnak!")
    return szavak 

def lista_kiir(szavak):
    for i in range(len(szavak)):
        if i == len(szavak) -1:
            print(szavak[i], end="")
        else:
            print(szavak[i], end="$")

def atlag_szohossz(lista):
    ossz_karakter = 0
    for i in lista:
        ossz_karakter += len(i)
    return print(f"Álag: {round(ossz_karakter / len(lista), 2)}")

def abc_elso_hely(lista):
    # Maximum/minimum kiválasztás
    min_hely = 0
    for i in range(len(lista)):
        if lista[i] < lista[min_hely]:
            min_hely = i
    return print(f"Az ABC sorrend szerinti első szó: {lista[min_hely]}")

def teljes():
    szavak = param_szobekero()
    lista_kiir(szavak)
    print()
    atlag_szohossz(szavak)
    abc_elso_hely(szavak)