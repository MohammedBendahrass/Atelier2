def Diviser_Inverser(liste):
    taille = len(liste)
    if taille % 3 != 0:
        return None
    taille_1 = taille // 3
    liste1 = [liste[i : i + taille_1] for i in range(0, taille, taille_1)]
    Inverse_Liste1 = [liste_Inv[::-1] for liste_Inv in liste1]

    return Inverse_Liste1


liste = [11, 45, 8, 23, 14, 12, 78, 45, 8]

liste1 = Diviser_Inverser(liste)
print(liste)

if liste1 is not None:
    print(liste1)
else:
    print("La liste is vide !!")
