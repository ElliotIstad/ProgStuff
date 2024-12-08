streng = input("-")
strengList = list((streng))
strenglength = len(strengList)
reverselist2 = list()
for x in range(1,strenglength+1):
    reverselist2.append(strengList[-x])
print(reverselist2)