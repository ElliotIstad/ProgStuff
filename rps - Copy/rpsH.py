#rock paper scissors
import rpsVar as V
import random as r
import time as t
                                             
options = ["rock", "paper", "scissors"]
score = int(0)


while 1:
    ComputerChoice = r.choice(options)
    
    PlayerChoice = input(str("type 'rock' to select rock, 'paper' to select paper, 'scissors' to select scissors and 'score' to see your current score : ").lower())
    
    if ComputerChoice == "rock" and PlayerChoice == "rock":
        print("ComputerChoice: \n", V.RockHand, "\n PlayerChoice: \n", V.RockHand)
        print(V.DrawText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "rock" and PlayerChoice == "paper":
        print("ComputerChoice: \n", V.RockHand, "\n PlayerChoice: \n", V.PaperHand)
        print(V.YouWinText, "\n")
        score = score+1
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "rock" and PlayerChoice == "scissors":
        print("ComputerChoice: \n", V.RockHand, "\n PlayerChoice: \n", V.ScissorHand)
        print(V.YouLoseText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "paper" and PlayerChoice == "rock":
        print("ComputerChoice: \n", V.PaperHand, "\n PlayerChoice: \n", V.RockHand)
        print(V.YouLoseText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "paper" and PlayerChoice == "paper":
        print("ComputerChoice: \n", V.PaperHand, "\n PlayerChoice: \n", V.PaperHand)
        print(V.DrawText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "paper" and PlayerChoice == "scissors":
        print("ComputerChoice: \n", V.PaperHand, "\n PlayerChoice: \n", V.ScissorHand)
        print(V.YouWinText, "\n")
        score = score+1
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "scissors" and PlayerChoice == "rock":
        print("ComputerChoice: \n", V.ScissorHand, "\n PlayerChoice: \n", V.RockHand)
        print(V.YouWinText, "\n")
        score = score+1
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "scissors" and PlayerChoice == "paper":
        print("ComputerChoice: \n", V.ScissorHand, "\n PlayerChoice: \n", V.PaperHand)
        print(V.YouLoseText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif ComputerChoice == "scissors" and PlayerChoice == "scissors":
        print("ComputerChoice: \n", V.ScissorHand, "\n PlayerChoice: \n", V.ScissorHand)
        print(V.DrawText, "\n")
        tryAgain = input(str("Want to try again? : "))
        if tryAgain == "yes":
            print("ok")
        elif tryAgain == "no":
            break
    
    elif PlayerChoice == "score":
        if score == (1):
            print("\n Your current score is: \n", V.One, "\n")
        if score == (2):
            print("\n Your current score is: \n", V.two, "\n")
        if score == (3):
            print("\n Your current score is: \n", V.three, "\n")
        if score == (4):
            print("\n Your current score is: \n", V.four, "\n")
        if score == (5):
            print("\n Your current score is: \n", V.five, "\n")
        if score == (6):
            print("\n Your current score is: \n", V.six, "\n")
        if score == (7):
            print("\n Your current score is: \n", V.seven, "\n")
        if score == (8):
            print("\n Your current score is: \n", V.eight, "\n")
        if score == (9):
            print("\n Your current score is: \n", V.nine, "\n")
        if score == (10):
            print("\n Your current score is: \n", V.ten, "\n")
        if score == (11):
            print("\n Your current score is: \n", V.eleven, "\n")
        if score == (12):
            print("\n Your current score is: \n", V.twelve, "\n")
        if score == (13):
            print("\n Your current score is: \n", V.thirteen, "\n")
        if score == (14):
            print("\n Your current score is: \n", V.fourteen, "\n")
        if score == (15):
            print("\n Your current score is: \n", V.fiftheen, "\n")
    else:
        print("\n Wrong input \n ")   

#the end