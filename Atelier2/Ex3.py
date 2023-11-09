def Compter_Occurences(liste):
    occurence = {}

    for element in liste:
        if element in occurence:
            occurence[element] += 1
        else:
            occurence[element] = 1
    return occurence


liste = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(liste)
result = Compter_Occurences(liste)
print(result)
