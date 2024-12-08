import subprocess
def retard():
    subprocess.call(["shutdown", "-r", "-t", "0"])

'''
import tkinter as tk

window = tk.Tk()
label1 = tk.Label(text="Hola mister")

button1 = tk.Button(
    text='Dont click me...',
    width=16,
    height=8,
    bg='white',
    fg="red",
)
button1.pack()




window.mainloop()
'''

import tkinter as tk
import tkintertraining2

window = tk.Tk()

label1 = tk.Label(text="Hola mister")

button1 = tk.Button(
    text='Dont click me...',
    width=16,
    height=8,
    bg='white',
    fg="red",
    command=tkintertraining2.retard
)
button1.pack()

window.mainloop()
