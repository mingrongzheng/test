import tkinter as tk
from tkinter import *  
from tkinter import messagebox         
import os   
import subprocess    
import time as ti
root = tk.Tk()    
root.title("登录界面")    
root.geometry("300x300")    
def center_window(window,width,height):
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    x=(screen_width-width)//2
    y=(screen_height-height)//2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(root,280,120)
def run_cmd_command():    
    python_exe_path = "python.exe"    
    py_file_path = "enroll.py"    
    cmd_command = f'{python_exe_path} {py_file_path}'    
    subprocess.run(cmd_command, shell=True)
def run_script():  
    os.system('python mygame.py')
def clear_text():      
    lb2.delete(0, 'end')    
    lb4.delete(0, 'end')    
def check_user(account, password):        
    if len(account) not in range(6, 19) or len(password) not in range(6, 19):  
        messagebox.showinfo("提示","账号和密码长度都要在6到18个字符之间")        
    else:        
        open_file(account, password)   
def open_file(account, password):    
    if account + '\t' + password  not in open('yh.txt', 'r').read():    
        messagebox.showinfo("提示","账号不存在，请注册或输入其他账号")     
    else:         
        with open('yh.txt', 'r') as file:  
            for line in file:  
                line = line.strip()
                columns = line.strip().split('\t')
                if len(columns) >= 2:
                    column1 = columns[0]
                    column2 = columns[1]
                if column1 == account and column2 == password:  
                    messagebox.showinfo("提示", "登录成功！即将开始游戏")
                    os.environ["MY_VARIABLE"] =  lb2.get()
                    root.destroy()
                    run_script()
lb1 = tk.Label(root, text='账号', height=2, width=5)    
lb2 = tk.Entry(root, width=30)   
lb3 = tk.Label(root, text='密码', height=2, width=5)    
lb4 = tk.Entry(root, text='', width=30, show='*')
an1 = tk.Button(root, text='登录', height=1, width=5, command=lambda: check_user(lb2.get(), lb4.get())).place(x=60, y=80)
an2 = tk.Button(root, text='清空', height=1, width=5, command=lambda: clear_text()).place(x=120, y=80)   
an3 = tk.Button(root, text='注册', height=1, width=5, command=run_cmd_command).place(x=180, y=80)
lb1.grid(row=0, column=0)    
lb2.grid(row=0, column=1)    
lb3.grid(row=1, column=0)    
lb4.grid(row=1, column=1)    
root.mainloop()