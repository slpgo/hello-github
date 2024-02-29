# -*- coding:utf-8 -*-
import tkinter as tk

# 變數初始化
win_width = 640
win_height = 480
screen_width = 0
screen_height = 0
size_geo = 0

# 建立主視窗
root = tk.Tk()
# 設定主視窗標題
root.title("Wilson-tkinter練習")
# 設定主視窗圖標
root.iconbitmap("./my.ico")
# 取得屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# 計算主視窗居中的參數字串
size_geo = '%dx%d+%d+%d' % (win_width, win_height, (screen_width-win_width)/2, (screen_height-win_height)/2)
# 設定主視窗大小與位置
root.geometry(size_geo)
# 鎖定主視窗大小
#root.resizable(0,0)
# 設定主視窗永遠顯示在最上層
root.attributes("-topmost", True)

# Label Widget 顯示文字範例
text_label = tk.Label(root,
text="Text Label 範例",
font=('Arial', 14, 'bold italic'),
bg="#CD7C7C",       # 指定背景顏色
fg="#FFFFCC",       # 指定前景顏色
width=20,
height=3,
padx=10, pady=15,   # 指定內容與邊框的水平與垂直的間距
borderwidth=2,      # 指定邊框寬度
relief='sunken',    # 指定邊框的樣式，默認是'flat'，其他參數有'groove'、'raised'、'ridge'、'solid'、'sunken'
state=tk.NORMAL,    # 指定Label的狀態，默認是tk.NORMAL，可選參數有tk.ACTIVE、tk.DISABLED
anchor='center',    # 指定內容在Label中顯示的位置，默認是'center'，其他參數有'n'、'ne'、'e'、'se'、's'、'sw'、'w'、'nw'
cursor="plus"       # 指定滑鼠停留在Label範圍中顯示的樣式，默認是'arrow'，其他參數有'circle'、'cross'、'plus'
)
text_label.pack()

text =  "這是文字第一行"\
        "這是文字第二行"\
        "這是最後一行\n呦"
tk.Label(root,
text=text,
fg='#7CCD7C',
font=('Arial', 14, 'bold italic'),
padx=10,
justify='left',     # 指定多行文本的對齊方式，參數值有'left'、'right'，'center'
wraplength=150      # 指定多行文本的每一行的長度，末任值為0
).pack(side='left')


# Label Widget 顯示圖片範例
photo = tk.PhotoImage(file="./myphoto.gif")

image_label = tk.Label(root,
width=270,
height=270,
padx=2, pady=2,
borderwidth=2,
image=photo,        # 指定Label顯示圖片，一般可以是PhotoImage或BitmapImage的物件
)
image_label.pack(side='right')

# Message Widget 可自動分行的Label
msg = "這是用來測試Message Widget自動斷行的機制"
tk.Message(root, text=msg, width=60, font=('Arial', 14, 'bold italic')).pack(side='bottom')

# 設定主視窗訊息迴圈
root.mainloop()