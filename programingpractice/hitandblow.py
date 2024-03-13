import tkinter as tk
import tkinter.messagebox as tmsg
from random import randint

#ボタンが押されたとき
def ButtonClick():
    #テキスト入力欄に入力された文字列を取得
    b=editbox1.get()
    
    isok=False
    if len(b)!=4:
                tmsg.showerror("エラー","４桁の数字を入力してくだちゃい。")
    else :
                    kazuok=True
                    for i in range(4):
                        if b[i]<"0" or b[i]>"9":
                                tmsg.showerror("エラー","数字ではありまちぇん")
                                kazuok=False
                                break
                    if kazuok :
                         isok=True

                               
    if isok :
        hit=0
        for i in range(4):
            if a[i]==int(b[i]):
                    hit=hit+1
  
        blow=0
        for j in range(4):
                for i in range(4):       
                    if int(b[j])==a[i] and a[i]!=int(b[i]) and a[j]!=int(b[j]):
                        blow=blow+1
                        break
   

        if hit==4:
            tmsg.showinfo("当たり","おめでとうございます")
    
        #終了
            root.destroy()
    
        else:
            rirekibox.insert(tk.END,b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
        
        
#メインのプログラム
#ランダムな４つの数を作成

a=[randint(0,9),randint(0,9),randint(0,9),randint(0,9)]

#print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

#ウィンドウを作る
root=tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")


#履歴表示のテキストボックス
rirekibox=tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0,width=200,height=400)





#ラベルをはる
label1=tk.Label(root,text="数を入力してね",font=("Helvetica",14))
label1.place(x=20,y=20)

#テキストボックスを作る
editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)

#ボタンを作る
button1=tk.Button(root,text="チェック",font=("Helbetica",14),command=ButtonClick)
button1.place(x=220,y=60)

#ウィンドウを表示する
root.mainloop()