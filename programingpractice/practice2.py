import tkinter as tk

window = tk.Tk()

window.title('MY tkinter')

# add widgets here

label1 = tk.Label(window, text = 'A', bg='red',fg='blue',
                 width = 20, height=10, font='Times 24')

label2 = tk.Label(window, text = 'B', bg='green',fg='white',
                 width = 20, height=10, font='Times 24')

label3 = tk.Label(window, text = 'C', bg='red',fg='blue',
                 width = 20, height=10, font='Times 24')

label4 = tk.Label(window, text = 'D', bg='green',fg='white',
                 width = 20, height=10, font='Times 24')

label5 = tk.Label(window, text = 'E', bg='green',fg='white',
                 width = 20, height=10, font='Times 24')


label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=0)
label5.grid(row=1, column=2)

window.mainloop()
