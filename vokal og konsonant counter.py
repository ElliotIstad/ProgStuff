streng = (input("-"))
strengList = list((streng))
strenglen = len(strengList)
vokaler = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]
vokalmengde = 0
tall = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
TallMengde = 0
konsonantMengde = 0
for i in range(strenglen):
    if strengList[i] in vokaler:
        vokalmengde = vokalmengde+1
    elif strengList[i] in tall:
        TallMengde = TallMengde+1
    elif strengList[i] != " ":
        konsonantMengde = konsonantMengde+1
        
print("det er", vokalmengde, "vokaler,", TallMengde, "tall og", konsonantMengde, "konsonanter")