def Translate():
    z=0
    word=input("search word (BG/EN):")
    if len(word)==0:
        print("Textbox is empty! Please input a word!")
        return
    f=open("dictionary.txt", "r")
    for line in f:
        if word in line:
            z=1
            print(line)
    f.close()
    if z==0:
        print("this word doesn't exist in dictionary! If you know the word translation, please add it (command 3)!")
