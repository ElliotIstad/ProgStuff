with open("regnestykker.txt", "r") as file:
    for line in file:
        eval(f"print({line})")