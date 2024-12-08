import sympy

tall = 0
count = 0

while count < 100:
    if sympy.isprime(tall) is True:
        print(tall)
        tall = tall+1
        count = count+1
    elif sympy.isprime(tall) is False:
        tall = tall+1