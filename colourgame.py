#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk 
# import pymysql
import pandas as pd
import random
import requests
import io
import cv2 as cv
import numpy
import math
import urllib.request as request
import tkinter.messagebox as messagebox
import time


# In[2]:


def callback():
    messagebox.showwarning('warning','Please finish the game, thank you!')
def StartMove(event):
    global first_x,first_y,clickID
    allID=canvas.find_closest(event.x,event.y)  
    if len(allID) > 0:
        clickID=allID[0]
        first_x,first_y = event.x,event.y    
def StopMove(event):
    global first_x,first_y,clickID
    canvas.move(clickID,event.x-first_x,event.y-first_y)
    clickID=-1    
def OnMotion(event):
    global first_x,first_y,clickID
    if clickID!=-1:
        canvas.move(clickID,event.x-first_x,event.y-first_y)
        first_x,first_y = event.x,event.y
def closeintro():
    root.attributes("-disabled", 0)
    intro.destroy()


# In[3]:


def intro():
    root.attributes("-disabled", 1)
    global intro
    intro = tk.Toplevel()
    intro.protocol('WM_DELETE_WINDOW', closeintro)
    intro.title('introduction')
    intro.geometry(alignstr) 
    canvas = tk.Canvas(intro, width=w,height=h,bd=0, highlightthickness=0)
    canvas.create_image(410, 262.5,image=photo)
    canvas.pack()
    text1 = '''
    This is a game about colour recognition and perception, 
    
    The result is obtained by distinguishing whether the 
    colours of blocks with very similar colours are exactly the same.
    '''
    lb = tk.Label(intro, text=text1,
            image=photo,
            width=w,               
            height=h,
            font='20',
            compound='center',
            borderwidth=0
            )
    lb.pack()
    canvas.create_window(410, 263, width=w, height=h,window=lb)
    intro.resizable(0, 0)
    intro.mainloop()


# In[4]:


def gamemain():
    global num
    num=0
    canvas.delete("all")
    
    text1 = '''
    Which one is darker?
    '''
    text2 = '''
    Please select the correct answer：
    '''
#     text3 = '''
#     Are the colors in the first and last images exactly the same?
#     '''
    text4 = '''
    Which circle is darker(the first circle or the second circle)?
    '''
    text5 = '''
    You can compare colours by moving the graph.Such as moving 
    two circles together. Which circle is darker?
    '''
    text6 = '''
    The next page will have a jigsaw puzzle to put the 4x4 small pictures in 
    the correct positions. The positions of the two pictures can be changed by 
    clicking on the two pictures in turn. Please click 'next' if you are ready.
    Please click 'finish' if you are done with the jigsaw puzzle.
    Below is the complete image. 
    '''
    text7='''
    Please move the block from light to dark.
    Tips: You can move the block to compare.
    If you have finished the game, Please click 'next'.
    '''
#     text8='''
#     Please enter numbers to sort from light to dark:
#     '''
    lb1 = tk.Label(root, text=text1,font='13')
    lb1.pack()
    lb2 = tk.Label(root, text=text2,font='13')
    lb2.pack()    
#     lb3 = tk.Label(root, text=text3,font='13')
#     lb3.pack()
    lb4 = tk.Label(root, text=text4,font='13')
    lb4.pack()
    lb5 = tk.Label(root, text=text5,font='13')
    lb5.pack()
    lb6 = tk.Label(root, text=text6,font='10')
    lb6.pack()
    lb7 = tk.Label(root, text=text7,font='13')
    lb7.pack()
#     lb8 = tk.Label(root, text=text8,font='13')
#     lb8.pack()
    
#     ent = tk.Entry(root)  # show='*'密文
#     ent.pack()
    
    url = 'https://doc-snapshots.qt.io/qt5-5.15/images/LinearGradient_maskSource1.png'
    image_bytes = requests.get(url).content
    data_stream = io.BytesIO(image_bytes)
    im = Image.open(data_stream)   
    photo = ImageTk.PhotoImage(im)
    
    comboxlist=ttk.Combobox(root,textvariable=tk.StringVar())
    comboxlist['values']=("First","Second","Same")
    comboxlist['state'] = 'readonly'
    comboxlist.pack()
    
    
    canvas.create_rectangle(170,130,360,380,fill='#b39559',outline='#b39559',tags='r33')
    canvas.create_rectangle(460,130,650,380,fill='#b8995c',outline='#b8995c',tags='r34')
    canvas.create_window(410, 80, width=600, height=50,window=lb1,tags='lb1')
    canvas.create_window(350, 430, width=600, height=50,window=lb2,tags='lb2')
    canvas.create_window(600, 430, width=70, height=30,window=comboxlist,tags='co')
    def gamenext():
        btn_next.configure(state="disabled")
        global num
        num=num+1
        if num==3: 
            canvas.delete("r1")
            canvas.delete("r2")
            canvas.create_rectangle(110,130,360,380,fill='#b39559',outline='#b39559',tags='r3')
            canvas.create_rectangle(460,130,710,380,fill='#b39559',outline='#b39559',tags='r4')
            comboxlist.configure(state="normal")
#         elif num==8:
#             canvas.delete("r7")
#             canvas.delete("r8")
#             canvas.create_rectangle(110,130,360,380,fill='#b37d12',outline='#b37d12',tags='r5')
#             canvas.create_rectangle(460,130,710,380,fill='#b88112',outline='#b88112',tags='r6')
#             comboxlist.configure(state="normal")
        elif num==7:
            
            canvas.delete("r111")
            canvas.delete("r211")
            canvas.delete("r212")
            canvas.create_rectangle(110,130,360,380,fill='#b39559',outline='#b39559',tags='r7')
            canvas.create_rectangle(460,130,710,380,fill='#b8995c',outline='#b8995c',tags='r8')
            comboxlist.configure(state="normal")
            
        elif num==1:
            canvas.delete("r33")
            canvas.delete("r34")
            canvas.create_rectangle(0,130,250,380,fill='#b39559',outline='#b39559',tags='r21')
            canvas.create_rectangle(570,130,820,380,fill='#b8995c',outline='#b8995c',tags='r22')
            comboxlist.configure(state="normal")
        elif num==8:
            canvas.delete("r7")
            canvas.delete("r8")
            canvas.create_rectangle(160,130,410,380,fill='#b39559',outline='#b39559',tags='r23')
            canvas.create_rectangle(410,130,660,380,fill='#b8995c',outline='#b8995c',tags='r24')
            comboxlist.configure(state="normal")
        
            
        elif num==4:
            canvas.delete("r3")
            canvas.delete("r4")
            canvas.create_rectangle(359.8,140,360,370,fill='#b39559',outline='#b39559',tags='r31')
            canvas.create_rectangle(460,140,460.2,370,fill='#b8995c',outline='#b8995c',tags='r32')
            comboxlist.configure(state="normal")
        elif num==2:
            canvas.delete("r21")
            canvas.delete("r22")
            canvas.create_rectangle(110,130,360,380,fill='#b3ada1',outline='#b3ada1',tags='r1')
            canvas.create_rectangle(460,130,710,380,fill='#b8b1a5',outline='#b8b1a5',tags='r2')
            comboxlist.configure(state="normal")
        elif num==5:
            canvas.delete("r31")
            canvas.delete("r32")
            canvas.create_rectangle(80,130,360,380,fill='#b39559',outline='#b39559',tags='r35')
            canvas.create_rectangle(460,130,740,380,fill='#b8995c',outline='#b8995c',tags='r36')
            comboxlist.configure(state="normal")
#         elif num==9:
#             canvas.delete("r23")
#             canvas.delete("r24")
#             canvas.create_rectangle(290,190,530,390,fill='#b0aa9e',outline='#b0aa9e',tags='r2122')
#             canvas.create_rectangle(110,110,360,360,fill='#b3ada1',outline='#b3ada1',tags='r1111')
#             canvas.create_rectangle(460,110,710,360,fill='#b8b1a5',outline='#b8b1a5',tags='r2111')
#             comboxlist.configure(state="normal")
        elif num==6:
            canvas.delete("r35")
            canvas.delete("r36")
            canvas.create_rectangle(290,190,530,390,fill='#b5afa3',outline='#b5afa3',tags='r212')
            canvas.create_rectangle(110,110,360,360,fill='#b3ada1',outline='#b3ada1',tags='r111')
            canvas.create_rectangle(460,110,710,360,fill='#b8b1a5',outline='#b8b1a5',tags='r211')
            comboxlist.configure(state="normal")
            
        elif num==9:
#             canvas.delete("r1111")
#             canvas.delete("r2111")
#             canvas.delete("r2122")
            canvas.delete("r23")
            canvas.delete("r24")
            canvas.create_window(410, 80, width=700, height=50,window=lb4)
            canvas.create_rectangle(90,110,370,390,fill='#959595',outline='#959595',tags='r41')
            canvas.create_rectangle(450,110,730,390,fill='#bdbdbd',outline='#bdbdbd',tags='r43')
            canvas.create_oval(180,200,280,300,fill='#A9A9A9',outline='#A9A9A9',tags='r42')
            canvas.create_oval(540,200,640,300,fill='#A9A9A9',outline='#A9A9A9',tags='r44')
            comboxlist.configure(state="normal")
        elif num==10:
            canvas.create_window(410, 70, width=700, height=50,window=lb5)
            canvas.bind("<ButtonPress-1>",StartMove)
            canvas.bind("<ButtonRelease-1>",StopMove)
            canvas.bind("<B1-Motion>", OnMotion)
            comboxlist.configure(state="normal")     
        elif num==11:
            global t1
            t1=time.time()
            canvas.delete("r41")
            canvas.delete("r42")
            canvas.delete("r43")
            canvas.delete("r44")
            canvas.delete("co")
            canvas.delete("lb2")
            canvas.create_window(410, 75, width=700, height=70,window=lb7,tags='lb7')
#             canvas.create_window(250, 430, width=600, height=50,window=lb8,tags='lb8')
            global aa
            global bb
            global cc
            global dd
            global ee
            aa=canvas.create_rectangle(20,190,160,330,fill='#8f8f8f',outline='#8f8f8f',tags='r51')
            bb=canvas.create_rectangle(180,190,320,330,fill='#808080',outline='#808080',tags='r52')
            cc=canvas.create_rectangle(340,190,480,330,fill='#949494',outline='#949494',tags='r53')
            dd=canvas.create_rectangle(500,190,640,330,fill='#8a8a8a',outline='#8a8a8a',tags='r54')
            ee=canvas.create_rectangle(660,190,800,330,fill='#858585',outline='#858585',tags='r55')
#             canvas.create_window(600, 430, width=130, height=30,window=ent,tags='en')
#             print(canvas.coords(aa),canvas.coords(bb),canvas.coords(cc),canvas.coords(dd),canvas.coords(ee))
#             canvas.bind("<ButtonPress-1>",StartMove)
#             canvas.bind("<ButtonRelease-1>",StopMove)
#             canvas.bind("<B1-Motion>", OnMotion)
            btn_next.configure(state="normal")
        
        elif num==12:
            t2=time.time()
            t3=int(t2-t1)
            tx='You got the right answer in '+str(t3)+' seconds.'
#             resultsall[11]=ent.get()
            
            if (canvas.coords(cc)[0]<canvas.coords(aa)[0]<canvas.coords(dd)[0]<canvas.coords(ee)[0]<canvas.coords(bb)[0]):
                resultsall[11]=str(t3)
                tk.messagebox.showinfo('Congratulation',tx)
                
            else:
                resultsall[11]='F'
                tk.messagebox.showinfo('Sorry','We are sorry you got the wrong answer.')
                
#             print(canvas.coords(aa)[0],canvas.coords(bb)[0],canvas.coords(cc)[0],canvas.coords(dd)[0],canvas.coords(ee)[0])
            btn_next.configure(state="normal")
        elif num==13:
            canvas.delete("r51")
            canvas.delete("r52")
            canvas.delete("r53")
            canvas.delete("r54")
            canvas.delete("r55")
            canvas.delete("r56")
            canvas.delete("r57")
            canvas.delete("lb7")
#             canvas.delete("lb8")
            canvas.create_image(410, 320,image=photo)
            canvas.create_window(407, 80, width=780, height=150,window=lb6) 
            canvas.create_window(750, 485, width=100, height=50,window=btn_finish)
            btn_finish.configure(state="disabled")
            btn_next.configure(state="normal")
        elif num==14:
            game3()
            btn_finish.configure(state="normal")
#             sql1="UPDATE score set a=%s,b=%s,c=%s,d=%s,e=%s,f=%s,g=%s,h=%s,i=%s,j=%s,k=%s WHERE id=%s"
#             val1=(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],ids)
#             sql_add(sql1,val1)
            
            
    def gamefinish():
        root.destroy()
        sendemail(resultsall)
    btn_next = tk.Button(root,
        text='next',     
        compound='center', 
        font='Simhei 20 bold',
        borderwidth=0,
        command=gamenext) 
    btn_next.pack() 
    canvas.create_window(750, 430, width=100, height=50,window=btn_next)
    
    btn_finish = tk.Button(root,
        text='finish',     
        compound='center', 
        font='Simhei 20 bold',
        borderwidth=0,
        command=gamefinish) 
    btn_finish.pack() 
    
    btn_next.configure(state="disabled")
    def nextpage(*args):
        resultsall[num]=comboxlist.get()
        comboxlist.configure(state="disabled")
        btn_next.configure(state="normal")
    
    comboxlist.bind("<<ComboboxSelected>>",nextpage)


# In[5]:


def game3():
    response = request.urlopen('https://doc-snapshots.qt.io/qt5-5.15/images/LinearGradient_maskSource1.png')
    img_array = numpy.array(bytearray(response.read()), dtype=numpy.uint8)
    src = cv.imdecode(img_array, -1)
    h = src.shape[0]
    w = src.shape[1]
    c = src.shape[2]
    row = 4
    col = 4
    offset_h = h//row
    offset_w = w//col
    global firstClick
    firstClick = False
    clickIdx = [0,0]
    tileList = []
    def calPicIdx(x, y):
        i = y//(offset_h)
        j = math.ceil((x%w)//offset_w)
        idx = i*row+j
        return int(idx)
    def onMouse(event, x, y, flag ,params):
        if event==cv.EVENT_LBUTTONDOWN:
            idx = calPicIdx(x, y)
            global firstClick
            firstClick = not firstClick
            if firstClick:
                clickIdx[0] = idx
            else:
                clickIdx[1] = idx
                tileList[clickIdx[0]], tileList[clickIdx[1]] = tileList[clickIdx[1]], tileList[clickIdx[0]]
                for i in range(0, row):
                    for j in range (0, col):
                        dst[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1] = tileList[i*row+j]
                cv.imshow("game", dst)
                difference = cv.subtract(dst, src2)
                result = not numpy.any(difference) #if difference is all zeros it will return False
                if result==True:
                    resultsall[12]='T'
#                     sql="UPDATE score set k=%s WHERE id=%s"
#                     val=(1,ids)
#                     sql_add(sql,val)
    tile = numpy.zeros((offset_h-1, offset_w-1, c),numpy.uint8)
    for i in range(0, row):
        for j in range (0, col):
            tile = src[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1]
            tileList.append(tile)
    for i in range(len(tileList)-1,0,-1):
        randomIdx = random.randint(0,i-1)
        tileList[i], tileList[randomIdx] = tileList[randomIdx], tileList[i]
    dst = numpy.zeros((h, w, c), numpy.uint8)
    for i in range(0, row):
        for j in range (0, col):
            dst[i*offset_h:(i+1)*offset_h-1, j*offset_w:(j+1)*offset_w-1] = tileList[i*row+j]
    cv.namedWindow("game")
    cv.setMouseCallback("game", onMouse)
    cv.imshow("game", dst)
    src2 = src.copy()
    for i in range(1, row):
        src2[i*offset_h-1:i*offset_h]= numpy.zeros((1,w,3), numpy.uint8)
        for j in range(1, col):
            src2[0:h,j*offset_w-1:j*offset_w]= numpy.zeros((h,1,3), numpy.uint8)
    cv.waitKey(0)


# In[6]:


# def sql_addid():
#     conn = pymysql.connect(host='172.16.2.235', user='jozy',password='123456789',
#                        database='results')
#     mycursor = conn.cursor()
#     sql_1 = "select * from score"
#     data = pd.read_sql(sql_1, conn)
#     sql = "INSERT INTO score (id) VALUES (%s)"
#     val = (len(data)+1)
#     mycursor.execute(sql, val)
#     conn.commit()
#     conn.close()
#     return len(data)+1


# In[7]:


# def sql_add(sql,val):
#     conn = pymysql.connect(host='172.16.2.235', user='jozy',password='123456789',
#                        database='results')
#     mycursor = conn.cursor()
#     mycursor.execute(sql, val)
#     conn.commit()
#     conn.close()


# In[8]:


import smtplib
from email.mime.text import MIMEText
def sendemail(cont):
    mail_host = "smtp.163.com"  
    mail_user = "colourgame2022"
    mail_pass = "KXATNCTPLTFUFQIJ"
 
    sender = 'colourgame2022@163.com'
    receivers = ['colourgame2022@163.com']  # 接收人邮箱
    content = ",".join(cont)
    title = 'colour game results'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
#     print("mail has been send successfully.")


# In[9]:


root = tk.Tk()
s_w = root.winfo_screenwidth()
s_h = root.winfo_screenheight()
root.title('colour perception game')
w=820
h=525
resultsall=['nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan','nan', 'nan','nan','nan','nan','F']
clickID=-1
alignstr = '%dx%d+%d+%d' % (w, h, (s_w-w)/2, (s_h-h)/2)
root.geometry(alignstr)
url = 'https://www.seekpng.com/png/detail/89-893430_white-flare-png-freeuse-monochrome.png'
image_bytes = requests.get(url).content
data_stream = io.BytesIO(image_bytes)
im = Image.open(data_stream)
canvas = tk.Canvas(root, width=w,height=h,bd=0, highlightthickness=0)    
photo = ImageTk.PhotoImage(im)
canvas.create_image(410, 262.5,image=photo)
canvas.pack()
im1=ImageTk.PhotoImage(im.crop((100,238,300,288)))
im2=ImageTk.PhotoImage(im.crop((500,238,700,288)))

btn_intro = tk.Button(root,
    text='introduction',     
    image=im1,
    compound='center', 
    font='Simhei 20 bold',
    borderwidth=0,
    command=intro)
btn_intro.pack()   
canvas.create_window(200, 263, width=200, height=50,window=btn_intro)
btn_start = tk.Button(root,
    text='start',     
    image=im2,
    compound='center', 
    font='Simhei 25 bold',
    borderwidth=0,
    command=gamemain)    
btn_start.pack()   
canvas.create_window(600, 263, width=200, height=50,window=btn_start)
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()


# In[ ]:




