def Creer_Troisieme_Liste(Liste1, Liste2):
    Liste3 = []
    for i in range(1, len(Liste1), 2):
        Liste3.append(Liste1[i])
    for j in range(0, len(Liste2), 2):
        Liste3.append(Liste2[j])
    return Liste3


Liste1 = [3, 6, 9, 12, 15, 18, 21]
Liste2 = [4, 8, 12, 16, 20, 24, 28]

Liste3 = Creer_Troisieme_Liste(Liste1, Liste2)
print(Liste1)
print(Liste2)
print(f"Le toisieme liste est egale : {Liste3}")
