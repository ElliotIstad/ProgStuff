import time as t

print("""
 ________  ___  ___  ___  ________     
|\   __  \|\  \|\  \|\  \|\_____  \    
\ \  \|\  \ \  \\\  \ \  \\|___/  /|   
 \ \  \\\  \ \  \\\  \ \  \   /  / /   
  \ \  \\\  \ \  \\\  \ \  \ /  /_/__  
   \ \_____  \ \_______\ \__\\________
    \|___| \__\|_______|\|__|\|_______|
          \|__|                        

""")

score = int(0)

answer1 = str(input("what is the name of Njåls cockroach? : "))
if answer1.lower() == ("sveinung"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer is 'sveinung'")

answer2 = str(input("What color is the sky? : "))
if answer2 == ("¡Ay, mi amor! ¡Ay, mi amor!"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(") 
    t.sleep(1)
    print("the correct answer was ¡Ay, mi amor! ¡Ay, mi amor!")

answer3 = str(input("Who invented the Pythagorean Therum? : "))
if answer3.lower() == ("pythagoras"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer was pythagoras")

answer4 = input("what is 613+7-4-7-3-4-6-5+4+3+45+5+4+65545? = ")
if answer4 == ("66197"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer was 66197")

answer5 = str(input("""What is the name of Jonas' dog?  
 a) jordan
 b) balder
 c) lucy
 : """))
if answer5.lower() == ("a"):
    print("Correct!")
    t.sleep(1)
    score = score+1
elif answer5.lower() == ("b"):
    print("Correct")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the answers was a or b")

answer8 = input("""Which sport is Njål's favorite?
 a) bowling
 b) diving
 c) kickboing
 : """)
if answer8.lower() == ("b"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer was b")

answer9 = str(input("if, elif and : "))
if answer9.lower() == ("else"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer was else")

answer10 = input("Who killed Hitler? = ")
if answer10.lower() == ("hitler"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("That is wrong :(")
    t.sleep(1)
    print("the correct answer was hitler")

answer11 = input("""Which teacher did we have 11/22/2023?
 a) Amalie
 b) Eskil
 c) Morra til njål
 : """)
if answer11.lower() == ("a"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("Helt feil. Gå til skammekroken")
    print("the correct answer was a")

answer12 = input("What is 'boolean' in norwegian? : ")
if answer12.lower() == ("boolsk"):
    print("Correct!")
    t.sleep(1)
    score = score+1
else:
    print("Helt feil. Gå til skammekroken")
    print("the correct answer was boolsk")

print("You scored", score, "out of 10")
t.sleep(1000)