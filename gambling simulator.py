import random as r
import time as t
import BlackJackVARS

print(BlackJackVARS.greeting)
print("Welcome to my blackjack gambling simulator")

cash = int(input("How much cash of your bank account do you wish to gamble? - "))
print("Alright. That is your starting cash amount.")


while True:
    BettingAmount = int(input("How much do you want to bet? - "))
    total = 0
    Dtotal = 0

    while 1: 
        c1 = r.randint(1,10)
        total+=c1
        print("your card is:\n", c1)
        print("your total value is:", total)
        if total > 21:
            break
        yORn = input("do you wish to continue? - ").lower()
        if yORn == "yes":
            print("")
        else:
            break

    while 1:
        c1 = r.randint(1,10)
        Dtotal+=c1
        if Dtotal > 16:
            break
        else:
            print("")

    if Dtotal > 21:
        if total > 21:
            print("You lose :(")
            cash=cash-BettingAmount
            print("Your bank account is now at", cash,)
        elif total <= 21:
            print("ggs")
            cash=cash+BettingAmount
            print("dealers total was", Dtotal)
            print("Your bank account is now at", cash,)
    elif total > 21:
        print("you lose :(")
        cash=cash-BettingAmount
        print("dealers total was", Dtotal)
        print("Your bank account is now at", cash,)
    elif total < Dtotal:
        print("you lose :(")
        cash=cash-BettingAmount
        print("dealers total was", Dtotal)
        print("Your bank account is now at", cash,)
    elif Dtotal < total:
        print("ggs")
        cash=cash+BettingAmount
        print("dealers total was", Dtotal)
        print("Your bank account is now at", cash,)
        
        
        if cash <= 0:
            print("You've gone bankrupt...")
            t.time(3) # type: ignore
            break
        elif cash > 0: 
            continue1 = input("do you wish to keep your gambling addiction going? - ").lower()
            if continue1 == "yes":
                print("")
            else:
                break