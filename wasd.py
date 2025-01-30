en=0
to=0
tre=0
fire=0
fem=0
seks=0
karakter=0


while karakter > -1:
    karakter = int(input('skriv en karakter : '))
    if karakter == 1:
        en = en + 1
    elif karakter == 2:
        to = to + 1
    elif karakter == 3:
        tre = tre + 1
    elif karakter == 4:
        fire = fire + 1
    elif karakter == 5:
        fem = fem + 1
    elif karakter == 6:
        seks = seks + 1

antall = en+to+tre+fire+fem+seks

print('antall enere er : ', en, en/antall*100, "i prosent")
print('antall toere er : ', to, to/antall*100, "i prosent")
print('antall treere er : ', tre, tre/antall*100, "i prosent")
print('antall fireere er : ', fire, fire/antall*100, "i prosent")
print('antall femere er : ', fem, fem/antall*100, "i prosent")
print('antall seksere er : ', seks, seks/antall*100, "i prosent")
print((en*1+to*2+tre*3+fire*4+fem*5+seks*6)/antall, "i prosent")
print(antall)