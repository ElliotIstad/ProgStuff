import time as t

print("Print funkjsonen skrives sånn her: print(). Det er viktig og få med anførselstegn og paranteser. Med tall trenger du ikke anførselstegn, men med tekst trenger du alltid og ta med alt.")
t.sleep(9)
print("Når du skriver det riktig blir teksten en annen farge")
t.sleep(5)
answer = input("Hvordan skriver man en print funksjon? : ")

if answer == ("print()"):
    print("Correct!")
    t.sleep(1.4)
else:
    print("Wrong")
    t.sleep(1)
    print("it is written as: print() ")
    t.sleep(1.4)

