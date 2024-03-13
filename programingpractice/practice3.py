import tkinter as tk

window = tk.Tk()

window.title('MY tkinter')

# add widgets here

# make button

def button_clicked():
    lable.configure(text='Next text:')


lable = tk.Label(window, text='Enter some text:', font='Times 25')

lable.grid(row=0, column=0)

button = tk.Button(window, text='Click me', 
                    width=20, height= 10, command = button_clicked)

button.grid(row=0, column=0)



window.mainloop()
