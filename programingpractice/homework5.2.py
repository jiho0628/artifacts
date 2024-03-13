import tkinter as tk
from tkinter import ttk
 
# Define
BUTTON = [
    ['C', 'B', '', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]
 
SYMBOL = ['+', '-', '*', '/']
 
# 簡易的な電卓を作ってみた！
class CaluGui(object):
    def __init__(self, app=None):
        # Define
        self.calc_str = '' # 計算用の文字列
 
        # Window Setting
        app.title('電卓') 
        app.geometry('300x450')
 
        # Frame Setting
        calc_frame = ttk.Frame(app, width=300, height=100)
        calc_frame.propagate(False)
        calc_frame.pack(side=tk.TOP, padx=10, pady=20)
        button_frame = ttk.Frame(app, width=300, height=400)
        button_frame.propagate(False)
        button_frame.pack(side=tk.BOTTOM)
 
        # Parts Setting
        self.calc_var = tk.StringVar()
        self.ans_var = tk.StringVar()
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("",20))
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",15))
        calc_label.pack(anchor=tk.E)
        ans_label.pack(anchor=tk.E)
 
        for y, row in enumerate(BUTTON, 1):
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=6, height=3)
                button.grid(row=y, column=x)
                button.bind('<Button-1>', self.click_button)
    
    def click_button(self, event):
        check = event.widget['text']
 
        if check == '=':
            if self.calc_str[-1:] in SYMBOL:
                self.calc_str = self.calc_str[:-1]
 
            res = '= ' + str(eval(self.calc_str))
            self.ans_var.set(res)
        elif check == 'C':
            self.calc_str = ''
            self.ans_var.set('')
        elif check == 'B':
            self.calc_str = self.calc_str[:-1]
        elif check in SYMBOL:
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL:
                self.calc_str = self.calc_str[:-1] + check
        else:
            self.calc_str += check
 
        self.calc_var.set(self.calc_str)
    
 
 
def main():
    # Window Setting
    app = tk.Tk()
    # Window size non resizable
    app.resizable(width=False, height=False)
    CaluGui(app)
    # Display
    app.mainloop()
 
if __name__ == '__main__':
    main()
