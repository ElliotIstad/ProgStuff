import random

elevliste = input("skriv ned noen navn - ")
elevliste = elevliste.split(" ")
print("\n", elevliste, "\n")

gruppestørrelse = int(input("Hvor lang skal gruppene være? - "))
sortedlist = []
GruppeMengde = len(elevliste)//gruppestørrelse

for x in range(GruppeMengde):
    for i in range(gruppestørrelse):
        rando = random.choice(elevliste)
        sortedlist.append(rando)
        elevliste.remove(rando)

def gruppene():
    abc = []
    for y in range(gruppestørrelse):
        abc.append(sortedlist[0])
        sortedlist.pop(0)
    return abc

for z in range(GruppeMengde):
    print(gruppene())