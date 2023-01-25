import random
import time
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import Quest
import pygame

def Start():
    global jok, otk, zak, price
    price=''
    otk=0
    jok=4
    zak=0
    txt.config(text = "Играта съдържа 10 въпроса. За всеки въпрос има няколко възможни отговори, от които само един е верен. Ако бъде избран грешен отговор играта приключва и спечелената сума се дели на две. Играчът има право да се откаже по всяко време и така да запази спечелената до тук сума. Играчът има право да заключи една сигурна сума, която при грешно даден отговор, ще се запази. В играта има 3 жокера: '50/50', 'информация' и 'пропускане на въпрос'. Максималната възможна сума за спечелване е 1400 лв: по 100 на всеки правилно отговорен въпрос и по 100 за всеки неизползван жокер(+заключена сума)!", font=('Arial', 20))    
    jock4.config(text="START!", command=lst)
    jock4.pack()
    jock4.place(x=20, y=430)
    click.place_forget()
    click1.place_forget()
    click2.place_forget()
    click3.place_forget()
    jock1['state']='disable'
    jock2['state']='disable'
    jock3['state']='disable'
    for i in lsum:
        i['state']='disable'
  
def lst():
    global ls
    global br
    global jok
    br=0
    jok=4
    ls=[]
    label.pack()
    label.pack_forget()
    label1.pack()
    label1.pack_forget()
    jock1['state']='normal'
    jock2['state']='normal'
    jock3['state']='normal'
    jock4.config(text="отказ", command=Otk)
    for i in lsum:
        i['state']='normal'
    while len(ls)!=10:
        r=random.randint(0,30)
        if r not in ls: ls.append(r)
    Questions()
    
def Questions():
    pygame.mixer.music.load("sounds/quest.mp3")
    pygame.mixer.music.play(loops=0)
    
    global l, otg, s, info, price
    lsum[br-1].config(fg="#ffb030", bg="#0b063d")
    if lsum[br-1]['text']==price:
        lsum[br-1].config(fg="#ffb030", bg="#ff1f1f")
    for i in ls:
        Quest.Quest(i)
        s=Quest.S()
        l=Quest.L()
        otg=Quest.Otg()
        info=Quest.Info()
        QuAns(s, l, otg, info)
    if len(ls)!=0:
        ls.pop()
    else:
          Count()
             
def QuAns(s, l, otg, info):
    global price
    random.shuffle(l) 
    txt.config(text=s, font=('Arial', 25))
    next.pack()
    next.pack_forget()
    lock.pack()
    lock.pack_forget()
    label2.pack()
    label2.pack_forget()
    
    click.config(text=l[0], command=lambda: Check(l[0], otg))
    click.pack()
    click.place(x=230, y=250)
    click['state']='normal'

    click1.config(text=l[1], command=lambda: Check(l[1], otg))
    click1.pack()
    click1.place(x=650, y=250)
    click1['state']='normal'

    click2.config(text=l[2], command=lambda: Check(l[2], otg))
    click2.pack()
    click2.place(x=230, y=400)
    click2['state']='normal'

    click3.config(text=l[3], command=lambda: Check(l[3], otg))
    click3.pack()
    click3.place(x=650, y=400)
    click3['state']='normal'
    lsum[br].config(fg="#0b063d", bg="#ffb030")  
    if lsum[br]['text']==price:
        lsum[br].config(fg="#ffb030", bg="#ff1f1f")
        
    for i in lclick:
        if i['text']==otg:
            i.config(activebackground="#49a617")
        elif i['text']!=otg:
            i.config(activebackground="#ff1f1f")
    
def Check(ans, otg):
    global br, otk
    if ans==otg:
        br+=1
        lsum[br-1]['state']='disable'
        pygame.mixer.music.load("sounds/correct.mp3")
        pygame.mixer.music.play(loops=0)
        time.sleep(1)
        TrueAns()
    else:
        otk=0
        pygame.mixer.music.load("sounds/wrong.mp3")
        pygame.mixer.music.play(loops=0)         
        time.sleep(1)
        Count()

def Count():
    pygame.mixer.music.load("sounds/coins.mp3")
    pygame.mixer.music.play(loops=0)
    global zak, price
    if br==10:
        txt.config(text="Джакпот! Верни отговори: "+str(br)+'\n'+'Спечели: '+str(br*100+jok*100)+' лв.', font=('Arial', 25))
        lsum[br-1].config(fg="#ffb030", bg="#0b063d")
        label1.pack()
        label1.place(x=230, y=270)
    elif otk==1:
        txt.config(text="Отказахте се от играта! Верни отговори: "+str(br)+'\n'+'Спечели: '+str((br*100))+' лв.', font=('Arial', 25))
        lsum[br-1].config(fg="#ffb030", bg="#0b063d")
        label1.pack()
        label1.place(x=230, y=270)    
    elif zak==1 and int(price)/100<=br:
        txt.config(text="Играта завърши! Верни отговори: "+str(br)+'\n'+'Спечели заключената сума: '+price+' лв.', font=('Arial', 25))
        lsum[br-1].config(fg="#ffb030", bg="#0b063d")
        label1.pack()
        label1.place(x=230, y=270)
    else:
        txt.config(text="За съжаление сбърка... Верни отговори: "+str(br)+'\n'+'Спечели: '+str((br*100)/2)+' лв.', font=('Arial', 25))
        lsum[br].config(fg="#ffb030", bg="#0b063d")
        label.pack()
        label.place(x=230, y=270)
    
    jock4.config(text="Нова игра?", command=lst)
    jock4.pack()
    jock4.place(x=20, y=430)
    next.pack()
    next.pack_forget()
    lock.pack()
    lock.pack_forget()
    click.place_forget()
    click1.place_forget()
    click2.place_forget()
    click3.place_forget()
    jock1['state']='disable'
    jock2['state']='disable'
    jock3['state']='disable'
    for i in lsum:
        i['state']='disable'
        i.config(fg="#ffb030", bg="#0b063d")
    lock['state']='normal'
    zak=0
    price=''

def TrueAns():
    pygame.mixer.music.load("sounds/ans.mp3")
    pygame.mixer.music.play(loops=0)
    click.place_forget()
    click1.place_forget()
    click2.place_forget()
    click3.place_forget()
    label2.pack()
    label2.place(x=20, y=20)
    txt.config(text=info, font=('Arial', 20))
    if br==10:
        next.config(text="Завърши!", command=Questions)
        lock['state']='disable'
    else:
        next.config(text="Следващ", command=Questions)
    next.pack()
    next.place(x=250, y=430)
    lock.pack()
    lock.place(x=650, y=430)
        
def Fifty():
    pygame.mixer.music.load("sounds/jock.mp3")
    pygame.mixer.music.play(loops=0)
    global jok, fif
    fif=1
    jok=jok-1
    broqch=0
    random.shuffle(lclick)
    for i in lclick:
        if broqch==2:
            break
        if i['text']!=otg:
            i.config(text="")
            i['state']='disable'
            broqch+=1 
    jock1['state']='disable'

def Skipy():
    pygame.mixer.music.load("sounds/jock.mp3")
    pygame.mixer.music.play(loops=0)
    global jok, br
    jok=jok-1
    lsum[br].config(fg="#ffb030", bg="#0b063d")
    br+=1
    lsum[br-1]['state']='disable'
    jock2['state']='disable'
    Questions()
    
def Texty():
    pygame.mixer.music.load("sounds/jock.mp3")
    pygame.mixer.music.play(loops=0)
    global jok, info
    jok=jok-1
    jock3['state']='disable'
    messagebox.showinfo('Информация', info)

def Otk():
    pygame.mixer.music.load("sounds/lose.mp3")
    pygame.mixer.music.play(loops=0)
    time.sleep(3)
    global otk
    otk=1
    Count()
    
def Lock():
    pygame.mixer.music.load("sounds/jock.mp3")
    pygame.mixer.music.play(loops=0)
    global zak, price, jok
    zak=1
    jok=jok-1
    price=lsum[br]['text']
    lsum[br].config(fg="#ffb030", bg="#ff1f1f")
    lock['state']='disable'


screen=Tk()
screen.iconbitmap('img/logo.ico')
screen.configure(bg='#302080')
screen.title("Българската техника на 20-ти век")
screen.state('zoomed') 
screen.minsize(1100, 750)

pygame.mixer.init()

pygame.mixer.music.load("sounds/start.mp3")
pygame.mixer.music.play(loops=0)

txt=tk.Label(text="", fg="#ffb030", bg="#302080", wraplengt=850)
txt.pack()
txt.place(x=230, y=20)

click=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=300, height=3, width=25, activebackground='white', font=('Arial', 20))
click.pack_forget()

click1=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=300, height=3, width=25, activebackground='white', font=('Arial', 20))
click1.pack_forget()

click2=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=300, height=3, width=25, activebackground='white', font=('Arial', 20))
click2.pack_forget()

click3=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=300, height=3, width=25, activebackground='white', font=('Arial', 20))
click3.pack_forget()

lclick=[click, click1, click2, click3]

jock1=tk.Button(text="50/50", fg="#ffb030", bg="#0b063d", wraplengt=120, height=2, width=10, font=('Arial', 20), command=Fifty)
jock1.pack()
jock1.place(x=20, y=20)

jock2=tk.Button(text="пропусни", fg="#ffb030", bg="#0b063d", wraplengt=120, height=2, width=10, font=('Arial', 20), command=Skipy)
jock2.pack()
jock2.place(x=20, y=120)

jock3=tk.Button(text="текст", fg="#ffb030", bg="#0b063d", wraplengt=120, height=2, width=10, font=('Arial', 20), command=Texty)
jock3.pack()
jock3.place(x=20, y=220)

jock4=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=120, height=2, width=10, font=('Arial', 20))
jock4.pack()
jock4.place(x=20, y=430)

sum=tk.Label(text="100", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum.pack(anchor="s", side='left', pady=0, padx=20)

sum1=tk.Label(text="200", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum1.pack(anchor="s", side='left', pady=0, padx=20)

sum2=tk.Label(text="300", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum2.pack(anchor="s", side='left', pady=0, padx=20)

sum3=tk.Label(text="400", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum3.pack(anchor="s", side='left', pady=0, padx=20)

sum4=tk.Label(text="500", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum4.pack(anchor="s", side='left', pady=0, padx=20)

sum5=tk.Label(text="600", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum5.pack(anchor="s", side='left', pady=0, padx=20)

sum6=tk.Label(text="700", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum6.pack(anchor="s", side='left', pady=0, padx=20)

sum7=tk.Label(text="800", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum7.pack(anchor="s", side='left', pady=0, padx=20)

sum8=tk.Label(text="900", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum8.pack(anchor="s", side='left', pady=0, padx=20)

sum9=tk.Label(text="1000", fg="#ffb030", wraplength=1, bg="#0b063d", height=5, width=3, font=('Arial', 25))
sum9.pack(anchor="s", side='left', pady=0, padx=20)

lsum=[sum, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9]

img = ImageTk.PhotoImage(Image.open("img/sad.png"))
label = tk.Label(image=img, height=225, width=720)

img1 = ImageTk.PhotoImage(Image.open("img/money.png"))
label1 = tk.Label(image=img1, height=200, width=820)

img2 = ImageTk.PhotoImage(Image.open("img/mark.png"))
label2 = tk.Label(image=img2, height=370, width=200)

next=tk.Button(text="", fg="#ffb030", bg="#0b063d", wraplengt=300, height=2, width=20, font=('Arial', 20))
next.pack_forget()

lock=tk.Button(text="Заключи сума", fg="#ffb030", bg="#0b063d", wraplengt=300, height=2, width=20, font=('Arial', 20), command=Lock)
lock.pack_forget()

Start()

screen.mainloop()