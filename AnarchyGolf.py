"""
with open("regnestykker.txt", "r") as file:
    for line in file:
        eval(f"print({line})")
"""
import time
start_time = time.time()
f = open("regnestykker.txt", "r")
for x in f:
    eval(f"print({x})")
f.close()
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)