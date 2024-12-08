UserInput = str(input("random number : "))
Individual = list(UserInput)
UserinputLen = len(Individual)
answer = 0
listen = []
for x in range (UserinputLen):
    Final = int(UserInput[x])
    answer = Final+answer
print(answer)