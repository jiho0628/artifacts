import tkinter as tk 

def main():
    root = tk.Tk()
    root.geometry('800x300')


    global a
    a =tk.Entry(width =4)
    a.pack()


    button1=tk.Button(root,text="チェック",font=('',28,'bold'), command=lambda:ex())
    button1.place(relx=0.7,rely=0.15,width=120, height=50,anchor=tk.CENTER) 

    tk.mainloop()

def ex(): 
    b=a.get()
    print(b)


if __name__ == '__main__':
    main()




