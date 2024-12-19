with open("regnestykker.txt", "r") as file:
    for line in file:
        print(eval(line))