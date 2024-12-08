import random
import time

print("Hello there user!")

time.sleep(2)

amount = (int(input("How many codes do you want generated? : ")))

prefix = (str(input("Do you want 'http://discord.gift/' in front of your code? yes or no : ")))

print("Very well!")

time.sleep(1.4)

url = "http://discord.gift/"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

if prefix == ("yes"):
    for x in range (amount):
        char1 = random.choice(chars)
        char2 = random.choice(chars)
        char3 = random.choice(chars)
        char4 = random.choice(chars)
        char5 = random.choice(chars)
        char6 = random.choice(chars)
        char7 = random.choice(chars)
        char8 = random.choice(chars)
        char9 = random.choice(chars)
        char10 = random.choice(chars)
        char11 = random.choice(chars)
        char12 = random.choice(chars)
        char13 = random.choice(chars)
        char14 = random.choice(chars)
        char15 = random.choice(chars)
        char16 = random.choice(chars)
        string = f"{char1}{char2}{char3}{char4}{char5}{char6}{char7}{char8}{char9}{char10}{char11}{char12}{char13}{char14}{char15}{char16}"
        print(f"{url}{string}")
    time.sleep(1000000)

elif prefix == ("no"):
    for x in range (amount):
        char1 = random.choice(chars)
        char2 = random.choice(chars)
        char3 = random.choice(chars)
        char4 = random.choice(chars)
        char5 = random.choice(chars)
        char6 = random.choice(chars)
        char7 = random.choice(chars)
        char8 = random.choice(chars)
        char9 = random.choice(chars)
        char10 = random.choice(chars)
        char11 = random.choice(chars)
        char12 = random.choice(chars)
        char13 = random.choice(chars)
        char14 = random.choice(chars)
        char15 = random.choice(chars)
        char16 = random.choice(chars)
        string = f"{char1}{char2}{char3}{char4}{char5}{char6}{char7}{char8}{char9}{char10}{char11}{char12}{char13}{char14}{char15}{char16}"
        print(string)
    time.sleep(1000000)

else:
    print("Whoops! it seems like you have used a wrong prefix. Please write 'yes' or 'no' all lowercase instead")
    time.sleep(1000000)
