import time as t

max = int(input("when should the stopwatch automatically stop? : "))
count = float(0)
Plus = float(1)

for x in range (max):
    t.sleep(1)
    count = float(count + Plus)
    print(float(count))