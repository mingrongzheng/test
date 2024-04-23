import turtle as tt
import random as ra
import time as ti
import pygame
from pygame.locals import *
import os
from tkinter import font, messagebox
import keyboard
n=1
tt.tracer(1,0)
tpencolor='deeppink,darkorange,brown,fuchsia,olive,aqua,red,green,yellow,blue,purple,salmon,sandybrown,skyblue,plum,coral,blueviolet,darkgoldenrod'
colors=tpencolor.split(',')
isonclick=True
scr=tt.Screen()
fenshu=[tt.Turtle(),-1,1]
fenshu[0].ht()
fenshu[0].up()
fenshu[0].sety(290)
fenshu[0].down()
onclicknum=1
onclickTurtle=tt.Turtle()
onclickTurtle.ht()
turtles=[]
def run_script1():  
    print("正在打开排名表")
    os.system('python pm.py')
trigger_key1 = 'ctrl + p'
keyboard.add_hotkey(trigger_key1, run_script1)
def run_script2():
    global fenshu
    file_path='yh.txt'
    user=os.environ.get("MY_VARIABLE")
    data_to_insert=str(fenshu[1])
    with open('yh.txt', 'r') as file:
            lines = file.readlines() 
            for i, line in enumerate(lines):
             if user in line: 
                line = line.strip()
                columns = line.strip().split('\t')
                if len(columns) >= 2:
                    column1 = columns[0]
                    column2 = columns[1]
                if column1 == user:
                    lines[i] = line.rstrip('\n') + '\t' + data_to_insert + '\n'
                with open(file_path, 'w') as file:
                        file.writelines(lines)
            print('分数上传成功')
trigger_key2 = 'u'
keyboard.add_hotkey(trigger_key2, run_script2)
def run_script3():  
    global fenshu  
    file_path = 'yh.txt'  
    user = os.environ.get("MY_VARIABLE")  
    data_to_insert = str(fenshu[1])  
    with open(file_path, 'r') as file:  
        lines = file.readlines()  
        for i, line in enumerate(lines):  
            if user in line:  
                line = line.strip()  
                columns = line.split('\t')  
                if len(columns) >= 2:  
                    column1 = columns[0]  
                    column2 = columns[1]  
                    if column1 == user and len(columns) > 2:    
                        columns.pop()  
                        new_line = '\t'.join(columns) + '\n'  
                        lines[i] = new_line 
                        print('删除分数成功') 
                        with open(file_path, 'w') as file:  
                            file.writelines(lines)  
                    else:
                        print("操作失败,暂无历史分数")
trigger_key3 = 'd'
keyboard.add_hotkey(trigger_key3, run_script3)
def fenshus():
    global fenshu
    global fs
    fenshu[1]=fenshu[1]+fenshu[2]
    fenshu[0].undo()
    fenshu[0].write('欢迎!'+os.environ.get("MY_VARIABLE")+'.你目前的得分为:'+str(fenshu[1])+'分，目前是第'+ str(n) +'关',align='center',font=('宋体',20))
    # fenshu[0].write('欢迎!你目前的得分为:'+str(fenshu[1])+'分，目前是第'+ str(n) +'关',align='center',font=('宋体',20)) 
fenshus()
def creategame(lve):
    global turtles
    global colors
    if len(turtles)!=0:
        for i in turtles:
            i['tpen'].clear()
        del turtles[0:len(turtles)]
    x=-25-55*lve
    y=25+55*lve
    tpenid=0
    colorsid=0
    for i in range(lve*2+1):
        for j in range(lve*2+1):
            tpen=tt.Turtle()
            tpen.ht()
            tpen.speed(0)
            tpencolor='silver'
            if tpenid%2==0 and tpenid!=0:
                colorsid=colorsid+1
            tpenfillcolor=colors[colorsid%len(colors)]
            tpenxy=(x+i*55,y-j*55)
            tpenisshow=True
            tpenid=tpenid+1
            tpenType={'tpen':tpen,'tpencolor':tpencolor,'tpenfillcolor':tpenfillcolor,'tpenxy':tpenxy,'tpenisshow':tpenisshow,'tpenid':tpenid}
            turtles.append(tpenType)
def suiji(turtles):
    for i in turtles:
        colors=i['tpenfillcolor']
        suiji=ra.randint(0,len(turtles)-1)
        i['tpenfillcolor']=turtles[suiji]['tpenfillcolor']
        turtles[suiji]['tpenfillcolor']=colors
def maingame(turtles):
    for i in range(len(turtles)):
        if turtles[i]['tpenisshow']==False:
            continue
        maingameid(i)
def maingameid(turtleid):
    turtles[turtleid]['tpen'].color(turtles[turtleid]['tpencolor'])
    turtles[turtleid]['tpen'].fillcolor(turtles[turtleid]['tpencolor'])
    turtles[turtleid]['tpen'].up()
    turtles[turtleid]['tpen'].goto(turtles[turtleid]['tpenxy'])
    turtles[turtleid]['tpen'].down()
    turtles[turtleid]['tpen'].begin_fill()
    for j in range(4):
        turtles[turtleid]['tpen'].fd(50)
        turtles[turtleid]['tpen'].right(90)
    turtles[turtleid]['tpen'].end_fill()
def maingameids(turtleid):
    turtles[turtleid]['tpen'].color(turtles[turtleid]['tpenfillcolor'])
    turtles[turtleid]['tpen'].fillcolor(turtles[turtleid]['tpenfillcolor'])
    turtles[turtleid]['tpen'].up()
    turtles[turtleid]['tpen'].goto(turtles[turtleid]['tpenxy'])
    turtles[turtleid]['tpen'].down()
    turtles[turtleid]['tpen'].begin_fill()
    for j in range(4):
        turtles[turtleid]['tpen'].fd(50)
        turtles[turtleid]['tpen'].right(90)
    turtles[turtleid]['tpen'].end_fill()
def showcolor(turtles):
    for i in range(len(turtles)):
        if turtles[i]['tpenisshow']==False:
            continue
        maingameids(i)
def maingameidx(turtleid):
    turtles[turtleid]['tpen'].color(turtles[turtleid]['tpenfillcolor'])
    turtles[turtleid]['tpen'].up()
    turtles[turtleid]['tpen'].goto(turtles[turtleid]['tpenxy'])
    turtles[turtleid]['tpen'].down()
    for j in range(4):
        turtles[turtleid]['tpen'].fd(50)
        turtles[turtleid]['tpen'].right(90)
def showpencolor(turtles):
    for i in range(len(turtles)):
        if turtles[i]['tpenisshow']==False:
            continue
        maingameidx(i)
def isY():
    global turtles
    global n
    count=0
    for i in turtles:
        if i['tpenisshow']==True:
            count+=1
        if count>=2:
            break
    if count<=1:
        n=n+1
        global fenshu
        fenshu[2]=fenshu[2]+1
        creategame(n)
        suiji(turtles)
        showcolor(turtles)
        ti.sleep(3)
        maingame(turtles)
    tt.ontimer(isY,200)
isck=0
def onclickTurtle(x,y):
    global isonclick
    global isck
    if isonclick==False:
        return
    isonclick=False
    global onclicknum
    global onclickTurtle
    global turtles
    global n
    for i in range(len(turtles)):
        if turtles[i]['tpenisshow']==True and turtles[i]['tpen'].pos()[0]<=x and x<=turtles[i]['tpen'].pos()[0]+50\
              and turtles[i]['tpen'].pos()[1]>=y and y>=turtles[i]['tpen'].pos()[1]-50:
            turtles[i]['tpen'].color(turtles[i]['tpencolor'])
            turtles[i]['tpen'].fillcolor(turtles[i]['tpenfillcolor'])
            turtles[i]['tpen'].begin_fill()
            for z in range(4):
                turtles[i]['tpen'].fd(50)
                turtles[i]['tpen'].right(90)
            turtles[i]['tpen'].end_fill()
            if onclicknum%2==0 and onclicknum != 0:
                if turtles[i]['tpen'].fillcolor()==turtles[onclickTurtle]['tpen'].fillcolor()\
                      and turtles[i]['tpenid']!=turtles[onclickTurtle]['tpenid']:
                    ti.sleep(0.4)
                    turtles[i]['tpenisshow']=False
                    turtles[i]['tpen'].clear()
                    turtles[onclickTurtle]['tpenisshow']=False
                    turtles[onclickTurtle]['tpen'].clear()
                    fenshus()
                    if isck==0:
                        maingame(turtles)
                    isck=1
                else:
                    ti.sleep(0.4)
                    maingameid(i)
                    maingameid(onclickTurtle)
                    if isck>=5:
                        showpencolor(turtles)
                        isck=0
                    elif isck==0:
                        maingame(turtles)
                        isck=1
                    else:
                        isck+=1
            else:
                onclickTurtle=i
            onclicknum=onclicknum+1
            break
    isonclick=True
creategame(n)
suiji(turtles)
showcolor(turtles)
ti.sleep(5)
maingame(turtles)
scr.onclick(onclickTurtle)
isY()
tt.mainloop()