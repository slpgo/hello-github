# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox

# 變數初始化
win_width = 320
win_height = 200
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
root.resizable(0,0)
# 設定主視窗永遠顯示在最上層
root.attributes("-topmost", True)



# 設定主視窗訊息迴圈
root.mainloop()