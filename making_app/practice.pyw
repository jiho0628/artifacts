# import tkinter as tk

# def excute():
#     txt = "こんにちは"
#     lbl.configure(text=txt)

# root = tk.Tk()
# root.title("こんにちは")
# root.geometry("200x100")

# lbl = tk.Label(text="")
# btn = tk.Button(text="実行", command = excute)

# lbl.pack()
# btn.pack()
# tk.mainloop()

import PySimpleGUI as sg

layout = [[sg.T(k="txt")],[sg.B("実行", k="btn")]] 
win = sg.Window("konnichiwa test", layout, size=(200,100))

def excute():
    win["txt"].update("konnnichiwa")

while True:
    e, v = win.read()
    if e == "btn":
        excute()
    if e == None:
        break
win.close()