import tkinter as tk
def Translate():
    z=0
    l=[]
    tekst=''
    word=name_storage.get()
    if len(name_storage.get()) == 0:
        txt.config(text = "Textbox is empty! Please input a word!")
        return
    f=open("dictionary.txt", "r")
    txt.config(text = " ")
    for line in f:
        if word in line:
            z=z+1
            tekst=tekst+line
            l.append(line)
    f.close()
    if z!=0:
        if z<15:
            txt.config(text = tekst) 
        else:
            LST()
            for i in l:
                lst.insert('end', i)
            sort_list()
            txt.config(text = "Too much translates! You need a listbox!")
    if z==0:
        txt.config(text = "this word doesn't exist in dictionary! \n If you know the word translation, please add it! \n")
    name.delete(0, 'end')

def Add():
    global storage, but, inp
    if len(name_storage.get()) == 0:
        txt.config(text = "Textbox is empty! Please input a word!")
        return
    click['state']='disable'
    click2['state']='disable'
    click3['state']='disable'
    name['state']='disable'
    storage=tk.StringVar()
    inp=tk.Entry(textvariable=storage, fg='red', font=('Arial', 25))
    inp.pack()
    inp.place(x=300, y=80, height=45, width=450)
    txt.place(x=10, y=140)
    txt.config(text = "Write translation of the word in the new box! \n Then press the button 'Add!!!'")
    click1.config(text="Add!!!", command=butone)
    
def butone():
    click['state']='normal'
    click1.config(text="Add word", command=Add)
    click2['state']='normal'
    click3['state']='normal'
    name['state']='normal'
    txt.place(x=10, y=100)
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
        name.delete(0, 'end')
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

def LST():
    global lst
    lst = tk.Listbox(height = 30, width = 82, bg = "grey",activestyle = 'dotbox', font = "Helvetica", fg = "yellow")
    lst.pack()
    lst.place(x=10, y=140)
    name.delete(0, 'end')
    click['state']='disable'
    click1['state']='disable'
    click2['state']='disable'
    name['state']='disable'
    click3.config(text="Back", command=Back)

def sort_list():
    temp_list = list(lst.get(0, tk.END))
    temp_list.sort(key=str.lower)
    # delete contents of present listbox
    lst.delete(0, tk.END)
    # load listbox with sorted data
    for item in temp_list:
        lst.insert(tk.END, item)

def All():
    word=name_storage.get()
    if len(word) == 0:
        txt.config(text = "Input Letter (A, a  - Z, z) in Textbox,\n then press the button again!\nFor all type 'all'!")
        return
    elif word=='All' or word=='all':
        LST()
        name.delete(0, 'end')
        txt.config(text = "All words in Dictionary:")
        f=open("dictionary.txt", "r")
        for line in f:
            lst.insert('end', line)
        f.close()
        sort_list()
        return
    elif len(name_storage.get()) != 1:
        name.delete(0, 'end')
        txt.config(text = "Please input only one letter! \n for all words type 'all'")
        return  
    LST()
    name.delete(0, 'end')
    txt.config(text = "The words with "+word+":")
    f=open("dictionary.txt", "r")
    for line in f:
        if line[0]==word:
            lst.insert('end', line)
    f.close()
    sort_list()

def Back():
    lst.destroy()
    name.delete(0, 'end')
    txt.config(text = " ")
    click['state']='normal'
    click1['state']='normal'
    click2['state']='normal'
    name['state']='normal'
    click3.config(text="view all", command=All)
    
screen=tk.Tk()
screen.iconbitmap('logo.ico')
screen.configure(bg='light grey')
screen.title("BG/EN Dictionary")
screen.state('zoomed') 
screen.minsize(1000, 750)

txt=tk.Label(text="", fg="red", bg="light grey", font=('Arial', 25))
txt.pack()
txt.place(x=10, y=90)

click=tk.Button(text="translate", fg="red", bg="dark grey", height=3, width=10, font=('Arial', 25), command=Translate)
click.pack(anchor='e', pady=20, padx=20)

click1=tk.Button(text="Add word", fg="red", bg="dark grey", height=3, width=10, font=('Arial', 25), command=Add)
click1.pack(anchor='e', pady=20, padx=20)

click2=tk.Button(text="Delete word", fg="red", bg="dark grey", height=3, width=10, font=('Arial', 25), command=del_word)
click2.pack(anchor='e', pady=20, padx=20)

click3=tk.Button(text="view all", fg="red", bg="dark grey", height=3, width=10, font=('Arial', 25), command=All)
click3.pack(anchor='e', pady=20, padx=20)

title1=tk.Label(text="Enter BG/EN word:", fg="red", bg="light grey", font=('Arial', 25))
title1.pack()
title1.place(x=10, y=20)

title2=tk.Label(text="(use only small letters!)", fg="red", bg="light grey", font=('Arial', 15))
title2.pack()
title2.place(x=25, y=60)

name_storage=tk.StringVar()
name=tk.Entry(textvariable=name_storage, fg='red', font=('Arial', 25))
name.pack()
name.place(x=300, y=20, height=45, width=450)

screen.mainloop()