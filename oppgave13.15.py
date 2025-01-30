import random

m=0
k=0
r=10000
for i in range(r):
    a = random.randint(1,2)
    if a == 1:
        m+=1
    else:
        k+=1

print(f"{m} mange mynt og {k} mange kron")
print(f"{m/r} er myng og {k/r} er kron")