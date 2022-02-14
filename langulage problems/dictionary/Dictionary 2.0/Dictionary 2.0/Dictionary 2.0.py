import tkinter as tk
def Translate():
    z=0
    tekst=''
    word=name_storage.get()
    if len(name_storage.get()) == 0:
        txt.config(text = "Textbox is empty! Please input a word!")
        return
    f=open("dictionary.txt", "r")
    txt.config(text = " ")
    for line in f:
        if word in line:
            z=1
            tekst=tekst+line
    f.close()
    if z!=0:
        txt.config(text = tekst) 
    if z==0:
        txt.config(text = "this word doesn't exist in dictionary! \n If you know the word translation, please add it! \n", font="bold")
    name.delete(0, 'end')

def Add():
    global storage, but, inp
    if len(name_storage.get()) == 0:
        txt.config(text = "Textbox is empty! Please input a word!")
        return
    storage=tk.StringVar()
    inp=tk.Entry(textvariable=storage)
    inp.pack()
    inp.place(x=250, y=40)
    txt.config(text = "Write translation of the word in the new box! \n Then press the button 'Add!!!'")
    but=tk.Button(text="Add!!!", fg="red", bg="yellow", height=3, width=10, command=butone)
    but.place(x=210, y=425)
    

def butone():
    if len(storage.get())==0:
        txt.config(text = "Textbox is empty! \n Please input translation!")
        return
    t=name_storage.get()+' - '+storage.get()+'\n'
    t1=storage.get()+' - '+name_storage.get()+'\n'
    fil=open("dictionary.txt", "r")
    for line in fil:
        if t==line or t1==line:
            fil.close()
            txt.config(text = "this word already exist!")
            inp.destroy()
            but.destroy()
            name.delete(0, 'end')
            return
    fil.close()
    f=open("dictionary.txt", "a")
    word=name_storage.get()
    translate=storage.get()
    f.write(word+' - '+translate+'\n')
    f.close()
    txt.config(text = "your word was written!")
    inp.destroy()
    but.destroy()
    name.delete(0, 'end')

def del_word():
    z=0
    if len(name_storage.get()) == 0:
        txt.config(text = "Textbox is empty! Please input a word!")
        return
    word=name_storage.get()
    fil=open("dictionary.txt", "r")
    for line in fil:
        if word in line:
            z=1
    fil.close()
    if z==0:
        txt.config(text = "this word doesn't exist in dictionary!")
        return
    else:
        f=open("dictionary.txt", "r")
        d=f.readlines()
        f.close()
        f1=open("dictionary.txt", "w")
        for line in d:
            if word not in line:
                f1.write(line)
        f1.close()
        txt.config(text = "your word was deleted succsesfully!")
        name.delete(0, 'end')
    
    
screen=tk.Tk()
screen.iconbitmap('logo.ico')
screen.configure(bg='light grey')
screen.title("BG/EN Dictionary")
screen.geometry("500x500")

title=tk.Label(text="Hello, this is BG/EN Dictionary!", font=("bold", 20), fg="red", bg="yellow")
title.pack()

txt=tk.Label(text="", fg="red", bg="light grey", font=("bold", 15))
txt.pack()
txt.place(x=10, y=60)

click=tk.Button(text="translate", fg="red", bg="yellow", height=3, width=9, command=Translate)
click.place(x=10, y=425)

click=tk.Button(text="Add word", fg="red", bg="yellow", height=3, width=10, command=Add)
click.place(x=210, y=425)

click=tk.Button(text="Delete word", fg="red", bg="yellow", height=3, width=9, command=del_word)
click.place(x=410, y=425)

title1=tk.Label(text="Enter BG/EN word:", fg="red", bg="yellow")
title1.pack()
title1.place(x=10, y=40)
name_storage=tk.StringVar()
name=tk.Entry(textvariable=name_storage)
name.pack()
name.place(x=125, y=40)

screen.mainloop()