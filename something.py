streng = (input("-"))
strengList = list((streng))
listLen = len(strengList)
numba = 0
for x in range(listLen):
    numba+=int(strengList[x])
print(numba/listLen)