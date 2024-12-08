streng = input("-")
strengList = list((streng))
strenglength = len(strengList)
reverselist = list()
for x in range(1,strenglength+1):
    reverselist.append(strengList[-x])

if reverselist == strengList:
    print("det er et palindrom")
else:
    print("det er ikke et palindrom")