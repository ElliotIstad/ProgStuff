numba = int(input("type a number to use in the collatz conjecture - "))
tries = 0
print("\n", numba)
while numba != 1:
    if numba % 2 == 0:
        numba = numba/2
        print(numba)
        tries = tries + 1
    elif numba == 1:
        print(numba)
        break
    else:
        numba = numba*3+1
        print(numba)
        tries = tries + 1
print(tries)