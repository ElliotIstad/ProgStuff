import webbrowser as wb

print("This is a webbrowser-based calculator")

print("Please select your desired method:")
print("Remember to write with caps")
DesiredMethod = input("M for multiplication, D for division, A for addition, S for subtraction: ")

answer1 = input("Please state your first number: ")
answer2 = input("Please state your second number: ")

num1 = float(answer1)
num2 = float(answer2)

query = ""

if DesiredMethod == "M":
    query = f"{num1} * {num2}"
elif DesiredMethod == "D":
    query = f"{num1} / {num2}"
elif DesiredMethod == "A":
    query = f"{num1} + {num2}"
elif DesiredMethod == "S":
    query = f"{num1} - {num2}"
else:
    print("Invalid method selection. Please choose M, D, A, or S.")
    exit()

google_url = f"https://www.google.com/search?q={query}"

wb.open(google_url)
