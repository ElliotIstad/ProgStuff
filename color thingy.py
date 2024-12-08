import webbrowser as wb
import time as t

color1 = input("What is you favorite color? write it here : ")
t.sleep(0.2)
color2 = input("Cool! What is your second favorite color? : ")
t.sleep(1.4)
print("Good choice!")

print("So if your favorite color is", color1, "and your second favorite color is", color2, "do you know what they are combined?")
t.sleep(1)
answer1 = ("Yes or No? : ")

if answer1 == ("Yes"):
    t.sleep(0.35)
    print("Awesome! I will just google it just to be sure you know")
    wb.open(color1, "mixed with", color2)
else:
    t.sleep(0.35)
    print("Damn. thats sad.")
    t.sleep(0.6)
    print("To ease your grief, let me just google it for you")
    wb.open(color1, "mixed with", color2)

print("Nice! Now you know.")
t.sleep(0.6)
print("Now for the actual task.")


print("Your favorite color is", color1, "and your second favorite color is", color2, "Do you have a third favorite color?")
t.sleep(0.8)
color3 = input("What is you third favorite color? : ")

print(color1, color2, color3, "are your top 3 favorite colors. Here is what they are combined")
t.sleep(3)
wb.open(color1, "mixed with", color2, "and", color3)