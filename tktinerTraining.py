#denne koden er min testing og utforskning av modulen tKinter. 
#Det er en GUI modul som lar meg lage GUIs og vinduer
#Det kommer mer etter hvert, men jeg har kommentert på det som er ferdig, og det som er implementert
#Koden er ikke den mest optimiserte tingen i verden, og jeg kommer til å gjøre den "bedre" etter hvert

import tkinter as tk, webbrowser as wb, subprocess, ctypes, sympy as sy, random, time
#importerer ulike moduler som jeg kommer til å bruke litt rundt omkring i koden

#definerer ulike variabler som blir brukt senere (med GLOBAL)
window = tk.Tk()
emptystring = ''
answertext = emptystring
RollImage = -1
delay = 300
up_delay = 11
outcome = 0
score = 0
totalTurns = 0
whowon = ''
winningLabel = tk.Button()
def emptycommand():
    exit()

#dette her er kommandoene som vil bli kjørt når du trykker på visse knapper i hovedvinduet
def on_button_pressed1():
    #denne knappen bruker website modulen til å åpne ulike programmer på pc-en min som jeg bruker ofte
    #veldig artig å ha etter en shutdown siden jeg ikke bruker startupp apps
    wb.open(r"C:\Users\elisa003\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    wb.open(r"C:\Users\elisa003\AppData\Local\Discord\app-1.0.9161\Discord.exe")
    wb.open(r"C:\Users\elisa003\AppData\Local\Programs\Opera\opera.exe")
    wb.open(r"C:\Program Files\WindowsApps\MSTeams_24231.512.3106.6573_x64__8wekyb3d8bbwe\ms-teams.exe")

def on_button_pressed2():
    #Med mindre du har noe på pc-en som er åpent og ikke savet, restarter denne kommandoen pc-en din.
    subprocess.call(["shutdown", "-r", "-t", "0"])

def on_button_pressed3():
    #Denne endrer bakgrunnen på pc-en din. (til du restartet/shutdowner)
    def on_tinybutton_pressed():
        path = TinyEntry.get()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    TinyWin = tk.Toplevel()
    TinyLabel = tk.Label(
        TinyWin, 
        text='↓ ↓ ↓ ↓ ↓ ↓ enter the image path ↓ ↓ ↓ ↓ ↓ ↓',
        )
    TinyEntry = tk.Entry(
        TinyWin,
        width=50,
        )
    TinyButton = tk.Button(
        TinyWin,
        width=4,
        height=2,
        text='ok',
        command=on_tinybutton_pressed
        )
    #her plasserer jeg alt på vinduet etter å ha laget de over her ^^^^
    TinyLabel.pack(pady=3)
    TinyEntry.pack(pady=10)
    TinyButton.pack()

def restartConfirmation():
    def funkyfunc():
        if AYS.cget("bg") == "white":
            AYS.config(bg="red")
        else:
            AYS.config(bg="white")
        AYS.after(200, funkyfunc)
    confirmationWin = tk.Toplevel()
    AYS = tk.Button(
        master=confirmationWin,
        width=20,
        height=4,
        bg="white",
        text='are you sure?',
        command=on_button_pressed2
    )
    AYS.pack()
    funkyfunc()
    #warning greie med flashing lights

def on_button_pressed4():
    #denne følgene kommandoen er ganske stor. Det er en kalkulator
    CalcWin = tk.Toplevel()
    AnswerBox = tk.Label(
        master=CalcWin,
        text=answertext,
        width=32,
        height=2,
        relief='raised'
    )
    #denne funksjonen under her, fikser errorer visst det står ting i svarboksen som ikke kan regnes ut. 
    #NAN står for Not-a-number og ZOO står for "Complex Infinity (i)"
    def on_button_pressed_calc(x):
        global answertext
        if answertext == ('Invalid syntax, please try again'):
            answertext = x
        elif answertext == ('zoo'):
            answertext = x
        elif answertext == ('nan'):
            answertext = x
        else:
            answertext=answertext+x
        AnswerBox.config(text=answertext)
    def ClearBox():
        global answertext
        answertext=emptystring
        AnswerBox.config(text=answertext)
    def SolveEquationProcess():
        #denne funksjonen bruker modulen SymPy til å gjøre om en string til et regnestykke.
        #Ganske fancy, spør du meg
        global answertext
        try:
            SolvedEquation = sy.sympify(answertext)
            answertext = str(SolvedEquation)
            AnswerBox.config(text=answertext)
        except sy.SympifyError:
            AnswerBox.config(text='Invalid syntax, please try again')
            answertext=emptystring
    

    #denne her er litt helvete å se på, sorry for det.
    #det er her jeg definerer alle de ulike knappene på kalkulatoren. 
    #"Master =" er hvilket vindu den tilhører, "text" sier litt seg selv, same med width, height og command.
    #I command bruker jeg en "lambda" funksjon. en lambda funksjon er basically en mini funksjon på én linje.
    cButton1 = tk.Button(master=CalcWin, text='1', width=8, height=4, command=lambda: on_button_pressed_calc('1'))
    cButton2 = tk.Button(master=CalcWin, text='2', width=8, height=4, command=lambda: on_button_pressed_calc('2'))
    cButton3 = tk.Button(master=CalcWin, text='3', width=8, height=4, command=lambda: on_button_pressed_calc('3'))
    cButton4 = tk.Button(master=CalcWin, text='4', width=8, height=4, command=lambda: on_button_pressed_calc('4'))
    cButton5 = tk.Button(master=CalcWin, text='5', width=8, height=4, command=lambda: on_button_pressed_calc('5'))
    cButton6 = tk.Button(master=CalcWin, text='6', width=8, height=4, command=lambda: on_button_pressed_calc('6'))
    cButton7 = tk.Button(master=CalcWin, text='7', width=8, height=4, command=lambda: on_button_pressed_calc('7'))
    cButton8 = tk.Button(master=CalcWin, text='8', width=8, height=4, command=lambda: on_button_pressed_calc('8'))
    cButton9 = tk.Button(master=CalcWin, text='9', width=8, height=4, command=lambda: on_button_pressed_calc('9'))
    cButton0 = tk.Button(master=CalcWin, text='0', width=8, height=4, command=lambda: on_button_pressed_calc('0'))
    cButtonPLUS = tk.Button(master=CalcWin, text='+', width=8, height=4, command=lambda: on_button_pressed_calc(' + '))
    cButtonMINUS = tk.Button(master=CalcWin, text='-', width=8, height=4, command=lambda: on_button_pressed_calc(' - '))
    cButtonMULTIPLY = tk.Button(master=CalcWin, text='*', width=8, height=4, command=lambda: on_button_pressed_calc(' * '))
    cButtonDIVIDE = tk.Button(master=CalcWin, text='/', width=8, height=4, command=lambda: on_button_pressed_calc(' / '))
    cButtonEQUALS = tk.Button(master=CalcWin, text='=', width=8, height=4, command=SolveEquationProcess)
    cButtonCLEAR = tk.Button(master=CalcWin, text='clear', width=8, height=4, command=ClearBox)
    
    #her plasserer jeg knappene. Ganske self-explanatory, den plasserer den på en grid med rader og søyler(jeg vet ikke helt hva det er på norsk ngl)
    AnswerBox.grid(row=0, column=0, columnspan=4)
    cButton1.grid(row=1, column=0)
    cButton2.grid(row=1, column=1)
    cButton3.grid(row=1, column=2)
    cButton4.grid(row=2, column=0)
    cButton5.grid(row=2, column=1)
    cButton6.grid(row=2, column=2)
    cButton7.grid(row=3, column=0)
    cButton8.grid(row=3, column=1)
    cButton9.grid(row=3, column=2)
    cButton0.grid(row=4, column=1)
    cButtonPLUS.grid(row=1, column=3)
    cButtonMINUS.grid(row=2, column=3)
    cButtonMULTIPLY.grid(row=3, column=3)
    cButtonDIVIDE.grid(row=4, column=3)
    cButtonEQUALS.grid(row=4, column=2)
    cButtonCLEAR.grid(row=4, column=0)

def on_button_pressed5():
    #enda en stor en her, rock paper scissors
    rpsWin = tk.Toplevel(
        width=500,
        height=300,
    )
    #her importerer jeg noen bilder som jeg vil bruke senere.
    global score
    score = 0
    rock = tk.PhotoImage(file="rock.png")
    paper = tk.PhotoImage(file="paper.png")
    scissors = tk.PhotoImage(file="scissors.png")
    default = tk.PhotoImage(file="default.png")
    rpsImages = [rock, paper, scissors]
    choices = ['rock', 'paper', 'scissors']
    OutcomeText='--Result--'
    
    PlayerActiveChoice = tk.Label(master = rpsWin, image = default,)
    PlayerActiveChoice.grid(row=0, column=0, pady=10, padx=10)

    AiActiveChoice = tk.Label(master = rpsWin, image=default,)
    AiActiveChoice.grid(row=0, column=2, pady=10, padx=10)
    score=0
    scorecounter = tk.Label(text=f"score = {score}", master=rpsWin,)
    scorecounter.grid(row=0, column=1)
    
    
    resultlabel = tk.Label(master=rpsWin, text=OutcomeText,)
    resultlabel.grid(row=1, column=1, padx=10, pady=10)
    
    def CalculateResult(PlayerChoice):
        #denne funksjonen kjøres hver gang en knapp blir trykket på. Den generer AI'en sitt valg og finner ut om du vant eller ikke. 
        global score
        AiChoice=random.randint(1,3)
        if PlayerChoice == 1:
            if AiChoice == 1:
                AiActiveImage = rock
                OutcomeText = "It's a tie!"
            elif AiChoice == 2:
                AiActiveImage = paper
                OutcomeText = "You lost..."
            elif AiChoice == 3:
                AiActiveImage = scissors
                OutcomeText = "You win!!!"
                score+=1
        elif PlayerChoice == 2:
            if AiChoice == 1:
                AiActiveImage = rock
                OutcomeText = "You win!!!"
                score+=1
            elif AiChoice == 2:
                AiActiveImage = paper
                OutcomeText = "It's a tie!"
            elif AiChoice == 3:
                AiActiveImage = scissors
                OutcomeText = "You lost..."
        elif PlayerChoice == 3:
            if AiChoice == 1:
                AiActiveImage = rock
                OutcomeText = "You lost..."
            elif AiChoice == 2:
                AiActiveImage = paper
                OutcomeText = "You won!!!"
                score+=1
            elif AiChoice == 3:
                AiActiveImage = scissors
                OutcomeText = "It's a tie!"
        #du ser nok denne en god del i koden. ".config" gjør at en ting blir oppdatert i realtime.
        #Så denne oppdaterer basically bare bildene og tekstene i vinduet
        resultlabel.config(text=OutcomeText)
        AiActiveChoice.config(image=AiActiveImage)
    
    def on_rock_button_pressed():
        #dette er funksjonene til spillerens knapper. Den endrer bildet, også kjører calculate result funksjonen med stein/saks/papir som argument
        PlayerActiveImage = rock
        PlayerActiveChoice.config(image=PlayerActiveImage)
        CalculateResult(1)
        scorecounter.config(text=f"score = {score}")
    
    def on_paper_button_pressed():
        PlayerActiveImage = paper
        PlayerActiveChoice.config(image=PlayerActiveImage)
        CalculateResult(2)
        scorecounter.config(text=f"score = {score}")
    
    def on_scissors_button_pressed():
        PlayerActiveImage = scissors
        PlayerActiveChoice.config(image=PlayerActiveImage)
        CalculateResult(3)
        scorecounter.config(text=f"score = {score}")
    
    #Her plasseres og defineres knappene
    PaperButton = tk.Button(master=rpsWin, height=3, width=10, text=choices[1], command=on_paper_button_pressed)
    PaperButton.grid(row=2, column=1, padx=10, pady=10)
    RockButton = tk.Button(master=rpsWin, height=3, width=10, text=choices[0], command=on_rock_button_pressed)
    RockButton.grid(row=2, column=0, padx=10, pady=10)
    ScissorsButton = tk.Button(master=rpsWin, height=3, width=10, text=choices[2], command=on_scissors_button_pressed)
    ScissorsButton.grid(row=2, column=2, padx=10, pady=10)
    
def on_button_pressed6():
    #denne her er fortsatt work in progress så det er ikke kommentarer her.
    global crossimage, circleimage, emptyimage
    crossimage = tk.PhotoImage(file=r"cross_image1.png")
    circleimage = tk.PhotoImage(file=r"hollow_ring_image.png")
    emptyimage = tk.PhotoImage(file=r"plain_white_image.png")
    pictureList = [crossimage, circleimage]
    tttSLOTS = {}
    tttWin = tk.Toplevel()
    tttWin.geometry("200x100")

    def endre_bilde(x, y):
        activeimage = y
        tttSLOTS[f"slot{x}"].config(image=y)
    
    def win_checker():
        winningstreaks = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        global whowon
        whowon = None
        for x in range(8):
            if (tttSLOTS[f"slot{winningstreaks[x][0]+1}"].cget('image') == str(crossimage) and
                tttSLOTS[f"slot{winningstreaks[x][1]+1}"].cget('image') == str(crossimage) and
                tttSLOTS[f"slot{winningstreaks[x][2]+1}"].cget('image') == str(crossimage)):
                whowon = "cross"
                for x in range(9):
                    tttSLOTS[f"slot{x+1}"].config(command=None)
            elif (tttSLOTS[f"slot{winningstreaks[x][0]+1}"].cget('image') == str(circleimage) and
                tttSLOTS[f"slot{winningstreaks[x][1]+1}"].cget('image') == str(circleimage) and
                tttSLOTS[f"slot{winningstreaks[x][2]+1}"].cget('image') == str(circleimage)):
                whowon = "circle"
                for x in range(9):
                    tttSLOTS[f"slot{x+1}"].config(command=None)
        
        if whowon == "cross" or whowon == "circle":
            winningLabel = tk.Label(text=f"{whowon} wins!", master=tttWin)
            winningLabel.grid(row=1, column=4)
    
    def on_ttt_icon_pressed(x):
        global totalTurns
        endre_bilde(x, pictureList[totalTurns % 2])
        win_checker()
        totalTurns += 1

    for i in range(9):
        row = i // 3  
        col = i % 3
        tttSLOTS[f"slot{i+1}"] = tk.Button(master=tttWin, image=emptyimage, command=lambda i=i:on_ttt_icon_pressed(i+1))
        tttSLOTS[f"slot{i+1}"].grid(row=row, column=col)
    def resetIcons():
        for x in range(9):
            tttSLOTS[f"slot{x+1}"].config(image=emptyimage, command=lambda i=i:on_ttt_icon_pressed(i+1))
        winningLabel.config(text="")
        global totalTurns
        totalTurns = 0
    resetButton = tk.Button(master=tttWin, text="reset", command=resetIcons)
    resetButton.grid(row=2, column=4)

#dette her er sentral-vinduet hvor alle knappene til de ulike tingene i programmet ligger. RPS, calc, WP osv
button1 = tk.Button(
    text='Useful applications',
    width=32,
    height=4,
    bg='white',
    fg="blue",
    command=on_button_pressed1,
)
button2 = tk.Button(
    text='restart',
    width=32,
    height=4,
    bg='red',
    fg='white',
    command=restartConfirmation,
)
button3 = tk.Button(
    text='Wallpaper Picker',
    width=32,
    height=4,
    bg='white',
    fg='orange',
    command=on_button_pressed3,
)
button4 = tk.Button(
    text='calculator',
    width=32,
    height=4,
    bg='white',
    command=on_button_pressed4,
)
button5 = tk.Button(
    text='Rock Paper Scissors',
    width=32,
    height=4,
    fg='lime',
    bg='white',
    command=on_button_pressed5,
)
button6 = tk.Button(
    text='tick tack toe',
    width=32,
    height=4,
    fg='turquoise',
    bg='white',
    command=on_button_pressed6
)


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()

#her lages hovedvinduet
window.mainloop()


#The End