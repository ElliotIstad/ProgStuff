import time as t

#this script is meant to be a converter. It basically converts one unit to another unit, like grams to ounces or celcius to fahrenheit
print("Welcome to the converter. What would you like to convert?")

while True:
    plip = int(input("1 for time, 2 for liquid amounts, 3 for temperature, 4 for weight : "))
    if plip == 1:
        convert = input("S seconds, M for minutes and H for hours : ").upper()

        print("What would you like to convert it too? : ")

        convert2 = input("S for seconds, M for minutes and H for hours : ").upper()
        #I use these variables a lot in the code so you'll see them repeating often

        if convert == "S":
            if convert2 == "S":
                print("Really? S to S? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "M":
                answer = float(input("How many seconds do you want to convert? : "))
                print("that is", answer/60, "minutes")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "H":
                answer = float(input("How many seconds do you want to convert? : "))
                print("that is", answer/3600, "hours")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use S, M or H")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
    #i used this format of manually creating an answer for every possible case. I think there is a better way to do this, but i dont know how just yet

        elif convert == "M":
            if convert2 == "S":
                answer = float(input("How many minutes do you want to convert? : "))
                print("that is", answer*60, "seconds")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "M":
                print("Really? M to M? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "H":
                answer = float(input("How many minutes do you want to convert? : "))
                print("that is", answer/60, "hours")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use S, M or H")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break

        elif convert == "H":
            if convert2 == "S":
                answer = float(input("How many hours do you want to convert? : "))
                print("that is", answer*3600, "seconds")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "M":
                answer = float(input("How many hours do you want to convert? : "))
                print("that is", answer*60, "minutes")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "H":
                print("Really? H to H? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use S, M or H")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        else:
            print("Wrong prefix, please use S, M or H")
            ReTry = str(input("do you want to do another conversion? : ").upper())
            if ReTry == "YES":
                print("ok")
            elif ReTry == "JA":
                print("ok")
            else:
                break
            #Just incase someone i show the code to doesn't understand that you have to write s, m or h (in this case) is have this Wrong prefix notification on all branches of the code. I hope?
    if plip == 2:
        convert = input("ML for milliliter, L for Liter, CL for centiliter, DL for deciliter, FLOZ for US flow ounce, G for gallon : ").upper()

        print("What do you want to convert it too?")

        MLtoL = 1000
        MLtoDL = 100
        MLtoCL = 10
        MLtoOZ = 29.574
        MLtoG = 3785
        LtoG = 3.785
        LtoCL = 100
        LtoDL = 10
        LtoOZ = 33.814
        CLtoDL = 10
        CLtoOZ = 2.957
        CLtoG = 378.5
        DLtoOZ = 3.381
        DLtoG = 37.854
        OZtoG = 128
    #   i saved these variables so i wouldnt have to type them in every situation. I did not use variable on the other unit-types because they were a lot simpler than these.

        answer = ""

        convert2 = input("ML for milliliter, L for Liter, CL for centiliter, DL for deciliter, FLOZ for US flow ounce, G for gallon : ").upper()

        if convert == "ML":
            if convert2 == "ML":
                print("Really? ML to ML? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                answer = float(input("How many ML do you want to convert? : "))
                print(answer/MLtoL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                answer = float(input("How many ML do you want to convert? : "))
                print(answer/MLtoCL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                answer = float(input("How many ML do you want to convert? : "))
                print(answer/MLtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                answer = float(input("How many ML do you want to convert? : "))
                print(answer/MLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many ML do you want to convert? : "))
                print(answer/MLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
                #here you can see how i used the variables i talked about a little earlier. 
                #For example, here i used the input/MLtoCL for the converting of Milliliters to centiliters. In the part of the code where i take The opposite:
                #centiliters to milliliters, i multiply them instead of dividing them, since multiplication is the opposite of division


        elif convert == "L":
            if convert2 == "ML":
                answer = float(input("How many L do you want to convert? : "))
                print(answer*MLtoL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                print("Really? L to L? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                answer = float(input("How many L do you want to convert? : "))
                print(answer*LtoCL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                answer = float(input("How many L do you want to convert? : "))
                print(answer*LtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                answer = float(input("How many L do you want to convert? : "))
                print(answer*LtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many L do you want to convert? : "))
                print(answer/LtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break

        elif convert == "CL":
            if convert2 == "ML":
                answer = float(input("How many CL do you want to convert? : "))
                print(answer*MLtoCL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                answer = float(input("How many CL do you want to convert? : "))
                print(answer/LtoCL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                print("Really? CL to CL? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                answer = float(input("How many CL do you want to convert? : "))
                print(answer/CLtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                answer = float(input("How many CL do you want to convert? : "))
                print(answer/CLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many CL do you want to convert? : "))
                print(answer/CLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break

        elif convert == "DL":
            if convert2 == "ML":
                answer = float(input("How many DL do you want to convert? : "))
                print(answer*MLtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                answer = float(input("How many DL do you want to convert? : "))
                print(answer/LtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                answer = float(input("How many DL do you want to convert? : "))
                print(answer*CLtoDL)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                print("Really? DL to DL? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                answer = float(input("How many DL do you want to convert? : "))
                print(answer*DLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many DL do you want to convert? : "))
                print(answer/DLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break

        elif convert == "FLOZ":
            if convert2 == "ML":
                answer = float(input("How many FLOZ do you want to convert? : "))
                print(answer*MLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                answer = float(input("How many FLOZ do you want to convert? : "))
                print(answer/LtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                answer = float(input("How many FLOZ do you want to convert? : "))
                print(answer/CLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                answer = float(input("How many FLOZ do you want to convert? : "))
                print(answer/DLtoOZ)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                print("Really? FLOZ to FLOZ? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many FLOZ do you want to convert? : "))
                print(answer/OZtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "G":
            if convert2 == "ML":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*MLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "L":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*LtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "CL":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*CLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DL":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*DLtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "FLOZ":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*OZtoG)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                print("Really? G to G? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use ML, L, CL, DL, FLOZ or G")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
    if plip == 3:
        convert = input("F for fahrenheit, C for celcius or K for kelvin : ").upper()

        print("What do you want to convert it too?")

        convert2 = input("F for fahrenheit, C for celcius or K for kelvin : ").upper()
        #i always add ".upper" in these input functions, so it doesnt matter if the user wrote upper or lowercase
        

        if convert == "F":
            if convert2 == "F":
                print("Really? F to F? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "C":
                answer = float(input("How many F do you want to convert? : "))
                print((answer - 32) * 5/9)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "K":
                answer = float(input("How many F do you want to convert? : "))
                print(((answer - 32) * 5/9)+273.15)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use K, F or C")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "C":
            if convert2 == "F":
                answer = float(input("How many C do you want to convert? : "))
                print((1.8*answer)+32)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "C":
                print("Really? C to C? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "K":
                answer = float(input("How many C do you want to convert? : "))
                print(answer+273.15)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use K, F or C")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "K":
            if convert2 == "F":
                answer = float(input("How many K do you want to convert? : "))
                answer = answer-273.15
                print((1.8*answer)+32)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "C":
                answer = float(input("How many K do you want to convert? : "))
                print(answer-273.15)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "K":
                print("Really? K to K? That is just 1X1. You can do that in your head, right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use K, F or C")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        else:
            print("Wrong prefix, please use K, F or C")
            ReTry = str(input("do you want to do another conversion? : ").upper())
            if ReTry == "YES":
                print("ok")
            elif ReTry == "JA":
                print("ok")
            else:
                break
    if plip == 4:
        convert = input("MG for milligrams, DG for decigrams, G for grams, HG for hectograms, KG for kilograms, T for tonnes, OZ for Ounce or LB for pound: ").upper()

        print("What do you want to convert it too?")

        convert2 = input("MG for milligrams, DG for decigrams, G for grams, HG for hectograms, KG for kilograms, T for tonnes, OZ for Ounce or LB for pound : ").upper()

        if convert == "MG":
            if convert2 == "MG":
                print("Really? Mg to Mg? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/100)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/100000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/1000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/1000000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/28350)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many MG do you want to convert? : "))
                print(answer/453600)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "DG":
            if convert2 == "MG":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer*100)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                print("Really? Dg to Dg? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer/10)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer/1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer/10000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer/10000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer*0.0035273962)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many DG do you want to convert? : "))
                print(answer*0.0002204623)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "G":
            if convert2 == "MG":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many G do you want to convert? : "))
                print(answer*10)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                print("Really? G to G? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many G do you want to convert? : "))
                print(answer/100)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many G do you want to convert? : "))
                print(answer/1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many G do you want to convert? : "))
                print(answer/1000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many G do you want to convert? : "))
                print(answer/28.35)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many G do you want to convert? : "))
                print(answer/453.6)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "HG":
            if convert2 == "MG":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer*100000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer*1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer*100)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                print("Really? Hg to Hg? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer/10)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer/10000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer*3.527396195)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many HG do you want to convert? : "))
                print(answer*0.2204622622)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "KG":
            if convert2 == "MG":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*1000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*10000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*10)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                print("Really? Kg to Kg? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer/1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*35.274)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many KG do you want to convert? : "))
                print(answer*2.205)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "T":
            if convert2 == "MG":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*1000000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*10000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*1000000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*10000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*1000)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                print("Really? T to T? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*35270)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many T do you want to convert? : "))
                print(answer*2205)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "OZ":
            if convert2 == "MG":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer*28350)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer*283.5)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "G":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer*28.35)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer*0.2834952313)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer/35.274)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer/35270)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                print("Really? OZ to OZ? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                answer = float(input("How many OZ do you want to convert? : "))
                print(answer/16)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
        elif convert == "LB":
            if convert2 == "MG":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer*453600)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "DG":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer*4536)
                t.sleep(1000)
            elif convert2 == "G":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer*453.6)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "HG":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer*4.5359237)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "KG":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer/2.205)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "T":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer/2205)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "OZ":
                answer = float(input("How many LB do you want to convert? : "))
                print(answer*16)
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            elif convert2 == "LB":
                print("Really? LB to LB? That is just 1X1. You can do that in your head right?")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
            else:
                print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
                ReTry = str(input("do you want to do another conversion? : ").upper())
                if ReTry == "YES":
                    print("ok")
                elif ReTry == "JA":
                    print("ok")
                else:
                    break
    else:
        print("Wrong prefix, please use MG, DG, G, HG, KG, T, OZ or LB")
        ReTry = str(input("do you want to do another conversion? : ").upper())
        if ReTry == "YES":
            print("ok")
        elif ReTry == "JA":
            print("ok")
        else:
            break