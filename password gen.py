import random
import string

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

Break = 1

while Break < 2:
    password_len = int(input("what would you like your password length to be : "))
    password_count = int(input("how many passwords do you want : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password    = password + password_char
        print("here is your password : ", password)
        Break = 3