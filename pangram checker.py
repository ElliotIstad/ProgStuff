import string

def pangramchecker(x):
    alphabet = string.ascii_uppercase
    for character in alphabet:
        if character not in x.upper():
            return False
        return True

streng = str(input("-"))
if pangramchecker(streng) == True:
    print("it is a pangram")
else:
    print("it is not a pangram")