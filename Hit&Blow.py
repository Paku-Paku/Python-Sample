# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg 

# Buttonがクリックされたときに実行する関数
def ButtonClick():
    # テキスト入力欄に入力された文字列を取得
    b = editbox1.get()
    # 入力チェック
    isok = False
    if len(b) != 4:
        tmsg.showerror("エラー", "4桁の数字を入力してください")
    else:
            kazuok = True
            for i in range(4):
                if (b[i] < "0") or (b[i] > "9"):
                    tmsg.showerror("エラー", "数字ではありません")
                    kazuok = False
                    break
            if kazuok == True:
                isok = True
    # 4桁の数字が入力されたとき、hit数とblow数を判定
    if isok == True:  
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit +1
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                    blow = blow + 1
                    break
    # hit数が4ならゲーム終了
        if hit == 4:
            tmsg.showinfo("当たり！！", "おめでとうございます。当たりです！")
            root.destroy()
        else:
            rirekibox.insert(tk.END, b + (" /H: " + str(hit) + " B: " + str(blow) + "\n"))

# メインのプログラム
# 4桁のランダムな整数を生成
a1 = random.randint(0,9)
a2 = random.randint(0,9)
a3 = random.randint(0,9)
a4 = random.randint(0,9)
a = [a1, a2, a3, a4]

# ウインドウを生成する
root = tk.Tk()
root.geometry("600x400")
root.title("Hit&Blowゲーム")

# 履歴表示のテキストボックスを生成する
rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x = 400, y = 0 ,width = 200, height = 400)

# ラベルを生成する
label1 = tk.Label(root, text = "数字を入力してください", font=("Helvetica", 14))
label1.place(x = 20, y = 20)

# テキストボックスを生成する
editbox1 = tk.Entry(width = 10, font=("Helvetica", 14))
editbox1.place(x = 40, y = 60)

# ボタンを生成する
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 10), command=ButtonClick)
button1.place(x = 160, y = 60)

# ウインドウを表示する    
root.mainloop()
