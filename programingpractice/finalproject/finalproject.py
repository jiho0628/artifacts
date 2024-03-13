import sys
import tkinter as tk
import tkinter.messagebox as tmsg
from random import randint
import pygame.mixer as pm
import time


#ランダムな４つの数を作成

a=[randint(0,9),randint(0,9),randint(0,9),randint(0,9)]
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

#タイトルの名前
name = 'ヒットアンドブロー'
#スクリーンの大きさ
screenwidth=600
screenheight=700
#遷移ボタンのサイズ
buttonwidth=120
buttonheight=50
#ホーム画面の名前
homename='ホームへ戻る'
#背景の色
bg1='#8388d8'
bg2='#dcdcdc'
bg3='#d35149'#player1
bg4='#6cdb82' #プレイや−２
#ルール説明
explain =   '1人プレイ\n予想した数字が位置も数字も正しければヒット（H）、\n位置は間違っていても数字が正しければブロー（B）と表現します。\n2人プレイ\n相手の4桁の数字を先に当てた人が勝ちとなります。\nまず、「自分の番号」を決めます。\nお互いが自分の番号を決めたら、順番に相手の番号を当てます。\nその番号の当たりとはずれの数が表示されます。\n一人ずつ順番に、相手の4桁の数字を予想します。'
#音の作成
sucsound = 'ラッパのファンファーレ.mp3'
sucsec = 1
clicksound= '決定ボタンを押す3.mp3'
clicksec =0.2
checksound ='決定ボタンを押す13.mp3'
checksec =0.25
failsound = '呪いの旋律.mp3'
failsec = 0.7
#back ground music
bgm ='/Users/jiho/OneDrive - Kyoto University/2回生後期/programingpractice/pleasant_stroll.mp3'

##scoreで得点管理、scorelistにscore履歴
score=0
scorelist=[]



def music(sound,sec):
    pm.music.set_volume(1)
    pm.music.load(sound)     # 音楽ファイルの読み込み
    pm.music.play(1)              # 音楽の再生回数(1回)
    time.sleep(sec)                         # 音楽の再生時間
    pm.music.fadeout(5) 

def clear(b):
    b.delete(0,tk.END)
    music(clicksound,clicksec)






def ButtonClick(b,rireki,text):
    #テキスト入力欄に入力された文字列を取得
        global score
        
        isok=False
        if len(b)!=4:
                    tmsg.showerror("エラー","半角で４桁の数字を入力してください。")
                    
        else :
                        
                        kazuok=True
                        for i in range(4):
                            if b[i]<"0" or b[i]>"9":
                                    tmsg.showerror("エラー","数字ではありません")
                                    kazuok=False
                                    
                                    break
                        if kazuok :
                            isok=True

                                
        if isok :
            score+=1
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
                music(sucsound,sucsec)
                tmsg.showinfo("当たり",text)
                scorelist.append(score)
                score=0
        
        
            else:
                music(checksound,checksec)
                rireki.insert(tk.END,b+"/H:"+str(hit)+"B:"+str(blow)+"  score="+str(score)+"\n")







#---------------------------------1人プレイのボタン----------------------------------------------
def transition1(widget):
    widget.place_forget() # canvas(widget)を隠す   

    music(clicksound,clicksec)


    canvas1 = tk.Canvas(background=bg1, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) # キャンバス 


    #ラベルをはる
    label1=tk.Label(canvas1,text="4桁の数を入力してね",bg=bg1,font=('',20))
    label1.place(relx=0.4,rely=0.1,anchor=tk.CENTER)

    #テキストボックスを作る
    editbox1=tk.Entry(width=7,font=('normal',50))
    editbox1.insert(0,'aaaaa')
    editbox1.place(relx=0.4,rely=0.2,anchor=tk.CENTER)

    #履歴表示のテキストボックス
    rirekibox=tk.Text(canvas1,background = bg2,font=("Helvetica",28))
    rirekibox.place(relx=0.5,rely=0.55,relwidth=0.8, relheight=0.4,anchor = tk.CENTER)

    #スクロールバーを設置
    yscroll = tk.Scrollbar(canvas1, orient=tk.VERTICAL, command=rirekibox.yview)
    yscroll.place(relx=0.9,rely=0.55,relheight=0.39,anchor= tk.E)
    rirekibox["yscrollcommand"] = yscroll.set

    #ボタンを作る
    button1=tk.Button(canvas1,text="チェック",font=('',28,'bold'), command=lambda:ButtonClick(editbox1.get(),rirekibox,'おめでとうございます'))
    button1.place(relx=0.7,rely=0.15,width=120, height=50,anchor=tk.CENTER) 

    button2=tk.Button(canvas1,text="クリア",font=('',28,'bold'), command=lambda:clear(editbox1))
    button2.place(relx=0.7,rely=0.25,width=120, height=50,anchor=tk.CENTER) 


    #home button
    home_button = tk.Button(canvas1, text=homename,command=lambda:transition_home(canvas1))   
    home_button.place(relx=0.5,rely=0.85, anchor = tk.CENTER) 

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

#-------------------------------２人プレイのボタン-------------------------------------------------------
rireki_list1 = []
rireki_list2 = []



# プレイヤー１の数字確定画面
def decide_number1(widget):
        widget.place_forget() # canvas(widget)を隠す    

        music(clicksound,clicksec)

        canvas1 = tk.Canvas(background=bg3, width=screenwidth, height=screenheight)
        canvas1.place(x=0, y=0) # キャンバス 

        #ラベルをはる
        label1=tk.Label(canvas1,text="プレイヤー1の番です 自分の4桁の数を入力してね",bg=bg3,font=('',20))
        label1.place(relx=0.4,rely=0.1,anchor=tk.CENTER)



        global editbox_number1
        editbox_number1=tk.Entry(width=7,font=('normal',14))
        editbox_number1.insert(0,'')
        editbox_number1.place(relx=0.4,rely=0.2,anchor=tk.CENTER)


        #ボタンを作る
        button1=tk.Button(canvas1,text="チェック",font=('',28,'bold'), command=lambda:decide_number2(canvas1))
        button1.place(relx=0.7,rely=0.2,width=120, height=50,anchor=tk.CENTER) 




# プレイヤー2の数字確定画面
def decide_number2(widget):
    
        widget.place_forget() # canvas(widget)を隠す    

        music(clicksound,clicksec)

        canvas1 = tk.Canvas(background=bg4, width=screenwidth, height=screenheight)
        canvas1.place(x=0, y=0) # キャンバス 

        #ラベルをはる
        label1=tk.Label(canvas1,text="プレイヤー2の番です 自分の4桁の数を入力してね",bg=bg4,font=('',20))
        label1.place(relx=0.4,rely=0.1,anchor=tk.CENTER)

        global editbox_number2
        editbox_number2=tk.Entry(width=7,font=('normal',14))
        editbox_number2.insert(0,'')
        editbox_number2.place(relx=0.4,rely=0.2,anchor=tk.CENTER)


        #ボタンを作る
        button1=tk.Button(canvas1,text="チェック",font=('',28,'bold'), command=lambda:transition_player1(canvas1))
        button1.place(relx=0.7,rely=0.2,width=120, height=50,anchor=tk.CENTER) 


    #プレイヤー1の画面に移動
def transition_player1(widget):
    widget.place_forget() # canvas(widget)を隠す    

    music(clicksound,clicksec)

    canvas1 = tk.Canvas(background=bg3, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) # キャンバス 


    #ラベルをはる
    label1=tk.Label(canvas1,text="プレイヤー1の番です 4桁の数を入力してね",bg=bg3,font=('',20))
    label1.place(relx=0.4,rely=0.05,anchor=tk.CENTER)

    #テキストボックスを作る
    editbox1=tk.Entry(width=7,font=('normal',14))
    editbox1.insert(0,'')
    editbox1.place(relx=0.4,rely=0.2,anchor=tk.CENTER)

    #プレイヤー1の履歴表示のテキストボックス
    rirekibox1=tk.Text(canvas1,background = bg2,font=("Helvetica",28))
    rirekibox1.place(relx=0.3,rely=0.55,relwidth=0.4, relheight=0.4,anchor = tk.CENTER)
    for rireki in rireki_list1:
        rirekibox1.insert(tk.END, rireki)
        
    #プレイヤー2の履歴表示のテキストボックス    
    rirekibox2=tk.Text(canvas1,background = bg2,font=("Helvetica",28))
    rirekibox2.place(relx=0.7,rely=0.55,relwidth=0.4, relheight=0.4,anchor = tk.CENTER)
    for rireki in rireki_list2:
        rirekibox2.insert(tk.END, rireki)
    #プレイヤー1のボタン処理
    def ButtonClick1(b,rireki):
        global rireki_list1
        global rireki_list2
        number2 =editbox_number2.get()
        isok=False
        if len(b)!=4:
                    tmsg.showerror("エラー","４桁の数字を入力してください。")
                    
        else :
                        
                        kazuok=True
                        for i in range(4):
                            if b[i]<"0" or b[i]>"9":
                                    tmsg.showerror("エラー","数字ではありません")
                                    kazuok=False
                                    
                                    break
                        if kazuok :
                            isok=True

                                
        if isok :

            hit=0
            
            for i in range(4):
                if int(number2[i]) == int(b[i]):
                        hit=hit+1
    
            blow=0
            for j in range(4):
                    for i in range(4):       
                        if int(b[j])==int(number2[i]) and int(number2[i])!=int(b[i]) and int(number2[j])!=int(b[j]):
                            blow=blow+1
                            break
    

            if hit==4:
                music(sucsound,sucsec)
                tmsg.showinfo("当たり","プレイヤー1の勝利です")
                rireki_list1 = []     
                rireki_list2 = []         
                transition_home2(canvas1)
            else:
                music(checksound,checksec)
                rireki.insert(tk.END,b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
                rireki_list1.append(b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
                transition_player2(canvas1)


                                    
 
    #ボタンを作る
    button1=tk.Button(canvas1,text="チェック",font=('',28,'bold'), command=lambda:ButtonClick1(editbox1.get(),rirekibox1))
    button1.place(relx=0.7,rely=0.15,width=120, height=50,anchor=tk.CENTER) 

    button2=tk.Button(canvas1,text="クリア",font=('',28,'bold'), command=lambda:clear(editbox1))
    button2.place(relx=0.7,rely=0.25,width=120, height=50,anchor=tk.CENTER) 


    #home button
    home_button = tk.Button(canvas1, text=homename,command=lambda:transition_home(canvas1))   
    home_button.place(relx=0.5,rely=0.85, anchor = tk.CENTER) 

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    #プレイヤー2の画面に移動
def transition_player2(widget):
    widget.place_forget() # canvas(widget)を隠す    

    music(clicksound,clicksec)

    canvas1 = tk.Canvas(background=bg4, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) # キャンバス 


    #ラベルをはる
    label1=tk.Label(canvas1,text="プレイヤー2の番です 4桁の数を入力してね",bg=bg4,font=('',20))
    label1.place(relx=0.4,rely=0.05,anchor=tk.CENTER)

    #テキストボックスを作る
    editbox1=tk.Entry(width=7,font=('normal',14))
    editbox1.insert(0,'')
    editbox1.place(relx=0.4,rely=0.2,anchor=tk.CENTER)

    #プレイヤー2の履歴表示のテキストボックス
    rirekibox1=tk.Text(canvas1,background = bg2,font=("Helvetica",28))
    rirekibox1.place(relx=0.7,rely=0.55,relwidth=0.4, relheight=0.4,anchor = tk.CENTER)
    for rireki in rireki_list2:
        rirekibox1.insert(tk.END, rireki)
    
    #プレイヤー1の履歴表示のテキストボックス    
    rirekibox2=tk.Text(canvas1,background = bg2,font=("Helvetica",28))
    rirekibox2.place(relx=0.3,rely=0.55,relwidth=0.4, relheight=0.4,anchor = tk.CENTER)
    for rireki in rireki_list1:
        rirekibox2.insert(tk.END, rireki)
    #プレイヤー2のボタン処理
    def ButtonClick2(b,rireki):
        global rireki_list1
        global rireki_list2
        number1 = editbox_number1.get()
        isok=False
        if len(b)!=4:
                    tmsg.showerror("エラー","４桁の数字を入力してください。")
                    
        else :
                        
                        kazuok=True
                        for i in range(4):
                            if b[i]<"0" or b[i]>"9":
                                    tmsg.showerror("エラー","数字ではありません")
                                    kazuok=False
                                    
                                    break
                        if kazuok :
                            isok=True

                                
        if isok :

            hit=0
            
            for i in range(4):
                if int(number1[i])==int(b[i]):
                        hit=hit+1
    
            blow=0
            for j in range(4):
                    for i in range(4):       
                        if int(b[j])==int(number1[i]) and int(number1[i])!=int(b[i]) and int(number1[j])!=int(b[j]):
                            blow=blow+1
                            break
    

            if hit==4:
                music(sucsound,sucsec)
                tmsg.showinfo("当たり","プレイヤー2の勝利です")
                rireki_list1 = []     
                rireki_list2 = []           
                transition_home2(canvas1)
            else:
                music(checksound,checksec)
                rireki.insert(tk.END,b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
                rireki_list2.append(b+"/H:"+str(hit)+"B:"+str(blow)+"\n")
                transition_player1(canvas1)


                                    
 
    #ボタンを作る
    button1=tk.Button(canvas1,text="チェック",font=('',28,'bold'), command=lambda:ButtonClick2(editbox1.get(),rirekibox1))
    button1.place(relx=0.7,rely=0.15,width=120, height=50,anchor=tk.CENTER) 

    button2=tk.Button(canvas1,text="クリア",font=('',28,'bold'), command=lambda:clear(editbox1))
    button2.place(relx=0.7,rely=0.25,width=120, height=50,anchor=tk.CENTER) 


    #home button
    home_button = tk.Button(canvas1, text=homename,command=lambda:transition_home(canvas1))   
    home_button.place(relx=0.5,rely=0.85, anchor = tk.CENTER) 

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)              

#---------------------------------------ゲーム中にホームに戻るボタン-----------------------------------------------------
def transition_home(widget):
    widget.place_forget() # canvas(widget)を隠す    

    music(clicksound,clicksec)

    #ホーム画面
    canvas1 = tk.Canvas(background=bg1, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) 

    label1 = tk.Label(canvas1, text = name, font=('',28),bg = '#3775ff', fg = 'black')
    label1.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.2, anchor = tk.CENTER)

    label2 = tk.Label(canvas1, text = explain, bg=bg1,font=('',20))
    label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    single_button = tk.Button(canvas1, text="1人プレイ用", command=lambda:transition1(canvas1)) # 遷移ボタン                                                
    single_button.place(relx=0.5, rely=0.6,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    battle_button = tk.Button(canvas1, text="2人プレイ用", command=lambda:transition_player1(canvas1)) # 遷移ボタン2                                            
    battle_button.place(relx=0.5, rely=0.7,width=buttonwidth,height=buttonheight, anchor= tk.CENTER)

    highscore_button = tk.Button(canvas1, text="ハイスコアリスト", command=lambda:transition_highscore(canvas1)) # 遷移ボタン３                                        
    highscore_button.place(relx=0.5, rely=0.8,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9,width=buttonwidth,height=buttonheight, anchor=tk.CENTER)
            

    #ウィンドウを表示する
    root.mainloop()
                      
#---------------------------------------ゲーム後にホームに戻るボタン-----------------------------------------------------
def transition_home2(widget):
    widget.place_forget() # canvas(widget)を隠す    

    music(clicksound,clicksec)

    #ホーム画面
    canvas1 = tk.Canvas(background=bg1, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) 

    label1 = tk.Label(canvas1, text = name, font=('',28),bg = '#3775ff', fg = 'black')
    label1.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.2, anchor = tk.CENTER)

    label2 = tk.Label(canvas1, text = explain, bg=bg1,font=('',20))
    label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    single_button = tk.Button(canvas1, text="1人プレイ用", command=lambda:transition1(canvas1)) # 遷移ボタン                                                
    single_button.place(relx=0.5, rely=0.6,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    battle_button = tk.Button(canvas1, text="2人プレイ用", command=lambda:decide_number1(canvas1)) # 遷移ボタン2                                            
    battle_button.place(relx=0.5, rely=0.7,width=buttonwidth,height=buttonheight, anchor= tk.CENTER)

    highscore_button = tk.Button(canvas1, text="ハイスコアリスト", command=lambda:transition_highscore(canvas1)) # 遷移ボタン３                                        
    highscore_button.place(relx=0.5, rely=0.8,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9,width=buttonwidth,height=buttonheight, anchor=tk.CENTER)
            

    #ウィンドウを表示する
    root.mainloop()
#---------------------------------------------ハイスコアリスト-----------------------------------------------------
def transition_highscore(widget):
    widget.place_forget() # canvas(widget)を隠す     

    music(clicksound,clicksec)
    
    scorelist.sort()
    highscore=""
    for i in scorelist:
        highscore+=str(i)+"\n"

    high_canvas = tk.Canvas(background=bg1, width=screenwidth, height=screenheight)
    high_canvas.place(x=0, y=0)

    label2 = tk.Label(high_canvas, text=highscore)
    label2.place(x=200, y=150, anchor=tk.CENTER)   
    #以下にハイスコアリストのプログラミングを書く





    #make home button
    home_button = tk.Button(high_canvas, text=homename,font=("Helbetica",14),command=lambda:transition_home(high_canvas))   
    home_button.place(relx=0.5,rely=0.85, anchor = tk.CENTER)  

    exit_button = tk.Button(high_canvas, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    
#-----------ゲームを辞めるボタン---------
def quit_button():
    sys.exit()






#------------------------------------------メイン-----------------------------------------------
def main():
    #ウィンドウを作る
    global root
    root=tk.Tk()
    root.geometry("600x700")
    root.title("ヒットアンドブロー")
    #root.attributes('-fullscreen', True)


    #ホーム画面
    canvas1 = tk.Canvas(background=bg1, width=screenwidth, height=screenheight)
    canvas1.place(x=0, y=0) 

    label1 = tk.Label(canvas1, text = name, font=('',28),bg = '#3775ff', fg = 'black')
    label1.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.2, anchor = tk.CENTER)

    label2 = tk.Label(canvas1, text = explain, bg=bg1,font=('',20))
    label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    single_button = tk.Button(canvas1, text="1人プレイ用", command=lambda:transition1(canvas1)) # 遷移ボタン                                                
    single_button.place(relx=0.5, rely=0.6,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    battle_button = tk.Button(canvas1, text="2人プレイ用", command=lambda:decide_number1(canvas1)) # 遷移ボタン2                                            
    battle_button.place(relx=0.5, rely=0.7,width=buttonwidth,height=buttonheight, anchor= tk.CENTER)

    highscore_button = tk.Button(canvas1, text="ハイスコアリスト", command=lambda:transition_highscore(canvas1)) # 遷移ボタン３                                        
    highscore_button.place(relx=0.5, rely=0.8,width=buttonwidth,height=buttonheight, anchor = tk.CENTER)

    exit_button = tk.Button(canvas1, text='ゲームを辞める', command=quit_button)
    exit_button.place(relx=0.5, rely=0.9,width=buttonwidth,height=buttonheight, anchor=tk.CENTER)
            

    #ウィンドウを表示する
    root.mainloop()


if __name__ =='__main__':
    pm.init()
    sd = pm.Sound(bgm)
    channel = sd.play(-1)
    channel.set_volume(0.1)
    main()