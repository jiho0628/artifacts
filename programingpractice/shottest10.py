import tkinter as tk

# callback functions

def red_clicked():
    label.configure(bg='red')

def blue_clicked():
    label.configure(bg ='blue')

# create the window
window = tk.Tk()

window.title('Exercise 2')


# creating the widgets
label = tk.Label(window, text='Label', width=30)

button = tk.Button(window, text='Red', width=10,
                   height=5, command= red_clicked)

button2 = tk.Button(window, text='Blue', width=10,
                   height=5, command=blue_clicked)

 

# placing the widgets
label.grid(row=0, column=0, columnspan=2)
button.grid(row=1, column=0)
button2.grid(row=1, column=1)


window.mainloop()