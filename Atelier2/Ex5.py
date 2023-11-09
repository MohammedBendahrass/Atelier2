ma_liste = [47, 64, 69, 37, 76, 83, 95, 97]
mon_Dict = {"Yassine": 47, "Imane": 69, "Mohammed": 76, "Abir": 97}

Nouvelle_liste = ma_liste.copy()

for element in Nouvelle_liste:
    if element not in mon_Dict.values():
        ma_liste.remove(element)

print(ma_liste)
