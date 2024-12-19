import time
start_time = time.time()
with open("regnestykker.txt", "r") as file:
    for line in file:
        eval(f"print({line})")
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)