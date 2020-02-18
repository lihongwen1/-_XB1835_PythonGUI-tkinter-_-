# ch12_8.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_8")            # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0)             # 預設選擇第0個項目

root.mainloop()








