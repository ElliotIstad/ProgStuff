from playsound import playsound


number1 = int(input("multiplication = 1, dividing = 2, addition = 3, subtraction = 4, exponents = 5 : "))

answer1 = int(input("Select your first number : "))
answer2 = int(input("Select your second number : "))
exponentanswer = pow(answer1,answer2)
while 1:
    if number1 == (1):
        print(answer1*answer2)
        playsound(r"C:\Users\elisa003\Downloads\y2mate.is - Audience Clapping Sound Effect-Gyu82WG_edM-192k-1697622077.mp3")

    if number1 == (2):
        print(answer1/answer2)
        playsound(r"C:\Users\elisa003\Downloads\y2mate.is - Audience Clapping Sound Effect-Gyu82WG_edM-192k-1697622077.mp3")

    if number1 == (3):
        print(answer1+answer2)
        playsound(r"C:\Users\elisa003\Downloads\y2mate.is - Audience Clapping Sound Effect-Gyu82WG_edM-192k-1697622077.mp3")

    if number1 ==(4):
        print(answer1-answer2)
        playsound(r"C:\Users\elisa003\Downloads\y2mate.is - Audience Clapping Sound Effect-Gyu82WG_edM-192k-1697622077.mp3")
    
    if number1 ==(5):
        print(exponentanswer)
        playsound(r"C:\Users\elisa003\Downloads\y2mate.is - Audience Clapping Sound Effect-Gyu82WG_edM-192k-1697622077.mp3")