streng = (input("-"))
strengList = list((streng))
listLen = len(strengList)
numba = 0
TomListe = []
for x in range(listLen):
    numba+=int(strengList[x])
gjennomsnitt = int(numba/listLen)
for i in range(listLen):
    a = int(strengList[i])
    if a > gjennomsnitt:
        a = str(a)
        TomListe.append(a)
print(TomListe)