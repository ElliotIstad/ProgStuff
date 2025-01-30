def oppgave_1():
    x = float(input('Skriv et tall for x: '))
    print(x*2)

def oppgave_2():
    x = float(input('Skriv et tall for x: '))
    print((2*x+1)**2)

def oppgave_3():
    x = float(input('Skriv et tall for x: '))
    a = float(input('Skriv et tall for a: '))
    print(x**2+a**2)

def oppgave_4():
    x = float(input('Skriv et tall for x: '))
    a = float(input('Skriv et tall for a: '))
    b = float(input('Skriv et tall for b: '))
    print(2*x+1+a*b)

def andregradsformelen():
    from math import sqrt
    a = float(input('Skriv et tall for a: '))
    b = float(input('Skriv et tall for b: '))
    c = float(input('Skriv et tall for c: '))
    d = b**2-4*a*c
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    print(f"løsning 1 er {x1} og løsning 2 er {x2}")

oppgave_1()
oppgave_2()
oppgave_3()
oppgave_4()
andregradsformelen()