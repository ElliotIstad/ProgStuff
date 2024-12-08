import webbrowser as wb

print("This is a webbrowser based calculator")

print("please select your desired method:")
DesiredMethod = (input("M for multiplication, D for dividing, A for addition, S for subtraction : "))

answer1 = (input("Please state your first number : "))
answer2 = (input("Please state your second number : "))
googleurl =  "https://www.google.no/search?q="

if DesiredMethod == ("M"):
    wb.open(answer1, "x", answer2)

if DesiredMethod == ("D"):
    wb.open(answer1, "/", answer2)

if DesiredMethod == ("A"):
    wb.open(answer1, "+", answer2)

if DesiredMethod ==("S"):
    wb.open(answer1, "-", answer2)