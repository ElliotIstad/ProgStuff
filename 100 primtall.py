"""
import math
count = 0
tall = 0
while count < 100:
    SquareRoot = math.sqrt(tall)
    if SquareRoot*tall == tall:
        print(tall)
        count = count+1
        tall = tall+1
    elif SquareRoot*tall < tall:
        tall = tall+1
    elif SquareRoot*tall > tall:
        tall = tall+1
"""




import sympy
tall = 0
count = 0

while count < 100:
    if sympy.isprime(tall):
        print(tall, "er et primtall")
        tall = tall+1
        count = count+1
    elif not sympy.isprime(tall):
        tall = tall+1

print("very cool :)")