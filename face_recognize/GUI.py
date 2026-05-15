'''
GUI:创建图形用户界面
'''

#1导入库
import tkinter as tk
import os
from PIL import Image, ImageTk


def gather_face():
     os.system('python 人脸采集.py')
def recognize_face():
     os.system('python 识别签到.py')
def show_excel():
     excel_path = r"D:\face_recognize\人脸签到表.xls"
     os.startfile(excel_path)
def train_mode():
     os.system('python 模型训练.py')
def exit_system():
     win.destroy()

#2设置窗口
win=tk.Tk()   #创建Windows窗口
win.title('人脸识别签到系统')
win.geometry('1294x800+200+50')      #宽*高
win.configure(background='#CD919E')  #六位十六进制
win.resizable(True,True)   #水平竖直方向拉伸

#设置显示内容
lab=tk.Label(win,text='人脸识别签到系统',bg='#CD919E',fg='black',font=('楷体',23,'bold'))

#lab.pack()   #简单布局排列
lab.grid(padx=18,pady=10)   #网格布局
#lab.place(relx=0.1,rely=0.1)  #精确布局

# picture=Image.open('2.jpg')
# image=ImageTk.PhotoImage(picture)
# lab1=tk.Label(win,image=image,text='picture1',compound='bottom',bg='#CD919E',fg='black')
#
# #lab.pack()   #简单布局排列
# lab1.grid(padx=18,pady=10)   #网格布局      插入图片

# but=tk.Button(win,text='按钮',command=ANAX)
# but.grid(padx=180,pady=100)     按钮

but1=tk.Button(win,text='采集人脸',bg='#e6397c',font='宋体',fg='#1a1a1d',command=gather_face)
but2=tk.Button(win,text='训练模型',font='宋体',bg='#e6397c',fg='#1a1a1d',command=train_mode)
but3=tk.Button(win,text='签到',bg='#e6397c',font='宋体',fg='#1a1a1d',command=recognize_face)
but4=tk.Button(win,text='打开签到表',font='宋体',bg='#e6397c',fg='#1a1a1d',command=show_excel)
but5=tk.Button(win,text='退出',font='宋体',bg='#e6397c',fg='#1a1a1d',command=exit_system)

but1.grid(padx=18,pady=10)
but2.grid(padx=18,pady=10)
but3.grid(padx=18,pady=10)
but4.grid(padx=18,pady=10)
but5.grid(padx=18,pady=10)


win.mainloop()