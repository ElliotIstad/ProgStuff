import tkinter as tk

root = tk.Tk()

def painfulprocess(text):
    if text == 2009:
        return 10
    elif text == 2010:
        return 9
    elif text == 2011:
        return 8
    elif text == 2012:
        return 7
    elif text == 2013:
        return 6
    elif text == 2014:
        return 5
    elif text == 2015:
        return 4
    elif text == 2016:
        return 3
    elif text == 2017:
        return 2
    elif text == 2018:
        return 1

def get_info():
    text = int(entry1.get())
    if text <= 2008 or text >= 2019:
        Answer="Du går ikke på grunnskolen!"
    else:
        if text >= 2012:
            Answer=f"du går i {painfulprocess(text)} trinn, på barneskolen!"
        elif text <= 2012:
            Answer=f"du går i {painfulprocess(text)} trinn, på ungdomskolen!"
    suitethingy = tk.Toplevel(width=20, height=10)
    suiteText = tk.Label(master=suitethingy, text=Answer)
    suiteText.grid(row=1, column=1)
label1 = tk.Label(master=root, text="Velkommen! Hva er ditt fødselsår?")
entry1 = tk.Entry(master=root, width=5,)
button1 = tk.Button(master=root, width=10, height=3, command=get_info, text="OK")

label1.pack(pady=5, padx=5)
entry1.pack(pady=5, padx=5)
button1.pack(pady=5, padx=5)

root.mainloop()