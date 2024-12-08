import cowsaytingelingVARS as v


def printthing():
    v.bubble("hola, como estas tu hablas español?")
    print(v.FINAL)
    print(v.line)
    print(v.cow)
    newfile = open("newfile.txt", "w")
    newfile.write(str(v.bubble("hola, como estas tu hablas español?")))
    newfile.write(v.line)
    newfile.write(v.cow)
    newfile.close()


printthing()