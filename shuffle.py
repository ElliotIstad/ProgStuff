"""
DetteErEnKulFunksjonsmaskin = "jeg er en kul funksjonsmaskin"

x = int(input(f"{DetteErEnKulFunksjonsmaskin} skriv in et tall og jeg skal løse det! :D funksjonen min er 2x btw - "))

def f(x):
    f = x * 2
    print(f)

f(x)
"""
y = input('skriv inn en funksjon av x : ')
x = input('skriv inn din ønskede verdi for x : ')
def customF(x, y):
    y = y.replace("x",f"*{x}")
    f = eval(y)
    print(f)

customF(x, y)