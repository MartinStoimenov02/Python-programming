def Delete():
    
    z=0
    word=input("write the word to delete: ")
    if len(word) == 0:
        print("Textbox is empty! Please input a word!")
        return
    fil=open("dictionary.txt", "r")
    for line in fil:
        if word in line:
            z=1
    fil.close()
    if z==0:
        print("this word doesn't exist in dictionary!")
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
        print("your word was deleted succsesfully!")