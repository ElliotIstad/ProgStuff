import time as t

count = float(0)
Plus = float(1)

for x in range (1000000000000000000):
    t.sleep(1)
    count = float(count + Plus)
    print(float(count))