# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox

# 常用控件
# Button-widget
# Canvas-widget
# Checkbutton-widget
# Entry-widget
# Frame-widget
# LabelFrame-widget
# Label-widget
# Listbox-widget
# Menu-widget
# Menubutton-widget
# Message-widget
# messageBox-widget
# OptionMenu-widget
# PanedWindow-widget
# Radiobutton-widget
# Scale-widget
# Spinbox-widget
# Scrollbar-widget
# Text-widget
# Toplevel-widget


# 建立主視窗
root = tk.Tk()
# 設定主視窗標題
root.title("Wilson-tkinter練習")
# 設定主視窗圖標
root.iconbitmap("./my.ico")
# 設定主視窗大小
root.geometry("320x150+600+300")
# 取得電腦頻幕大小
screen_size = "Screen Size: %dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight())
# 取得目前的視窗大小，必須先刷新視窗
root.update()
window_size = "Window Size: %dx%d" % (root.winfo_width(), root.winfo_height())
# 鎖定主視窗大小
root.resizable(0,0)
# 設定主視窗永遠顯示在最上層
root.attributes("-topmost", True)


# Callback Function
def root_query_proc():
    if tk.messagebox.showwarning("警告", "準備關閉視窗"):
        root.destroy()

def btn_exit_proc():
    root.quit()

def btn_mini_proc():
    root.iconify()

def btn_hide_proc():
    root.withdraw()

def btn_show_proc():
    root.deiconify()

def btn_color_proc():
    msg_label.config(bg="blue", fg="yellow")

# 添加Label Widget
msg_label = tk.Label(root, text="Hello, tkinter")
msg_label.pack()
tk.Label(root, text=screen_size).pack()
tk.Label(root, text=window_size).pack()

# 添加Button Widget
# tk.Button(root, text="隱藏", command=btn_hide_proc).pack()
# tk.Button(root, text="顯示", command=btn_show_proc).pack()
tk.Button(root, text="著色", command=btn_color_proc).pack()
tk.Button(root, text="最小化", command=btn_mini_proc).pack()
tk.Button(root, text="離開", command=btn_exit_proc).pack()

# 使用主視窗的協議機制，呼叫指定的Callback Function
root.protocol('WM_DELETE_WINDOW', root_query_proc)

# 設定主視窗訊息迴圈
root.mainloop()