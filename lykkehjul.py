import random

a=0

for i in range(1000):
    g=random.randint(1,6)
    if g==1 or g==2:
        a+=1

print(a/1000)