import tkinter as tk
from tkinter import colorchooser

class Application(tk.Frame):
    # 色を確認するための関数
    def checkColor(self):
        print(colorchooser.askcolor())
        # Windowを削除する。
        self.master.destroy()

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")
        self.checkColor()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()