import tkinter as tk  
from tkinter import *
from tkinter import messagebox  
import sys  
def end_program():  
    sys.exit()   
def validate_account_length(account, password):      
    if len(account) not in range(6, 19) or len(password) not in range(6, 19):      
        print("账号和密码长度都要在6到18个字符之间")      
    else:      
        open_file(account, password)   
def clear_text():  
    lb2.delete(0, 'end')
    lb4.delete(0, 'end')
    lb6.delete(0, 'end')   
def open_file(account, password):      
    if any(char in '*/' for char in account) or any(char in '*/' for char in password):      
        print("账号和密码都不能包含*/这类字符")      
    elif account + '\t' + password in open('yh.txt', 'r').read():
        print("账号已存在，请输入其他账号")
    elif lb4.get()!=lb6.get():
        print("密码不一致")
    else:  
        with open('yh.txt', 'a+') as f:      
                f.write(account + '\t' + password + '\n')        
        messagebox.showinfo("提示", "注册成功！")
root = tk.Tk()      
root.title("注册界面")      
root.geometry("300x200")      
lb1 = tk.Label(root, text="账号", height=2, width=10)    
lb2 = tk.Entry(root, width=20)    
lb3 = tk.Label(root, text="密码", height=2, width=10)    
lb4 = tk.Entry(root, width=20)
lb5 = tk.Label(root, text="确认密码", height=2, width=10)    
lb6 = tk.Entry(root, width=20)     
Button(root, text="提交", command=lambda: validate_account_length(lb2.get(), lb4.get()), height=1, width=5).place(x=40, y=120)    
Button(root, text="退出注册", command=lambda:end_program(),height=1, width=7).place(x=100, y=120)     
Button(root, text="清空", command=lambda:clear_text(),height=1, width=5).place(x=170, y=120)   
lb1.grid(row=0, column=0)    
lb2.grid(row=0, column=1)    
lb3.grid(row=1, column=0)   
lb4.grid(row=1, column=1)    
lb5.grid(row=2, column=0)
lb6.grid(row=2, column=1)      
root.mainloop()