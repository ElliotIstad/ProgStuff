#fibonacci sekvens tingeling

a = 0
b = 1
c = 0

for x in range(10):
    print(a + b)
    c = b
    b = a + b
    a = c