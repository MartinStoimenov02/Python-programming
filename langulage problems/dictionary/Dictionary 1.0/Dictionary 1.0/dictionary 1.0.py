cmnd='a'
z=0
while cmnd!='0':
    print('\n'+"YOUR DICTIONARY"+2*'\n'+"your choice:"+'\n'+"1. search word (BG/EN)"+'\n'+"2. add new word"+'\n'+"3. Delete word"+'\n'+"4. show all words in dictionary")
    cmnd=input("your choice(1-4, for end tab '0'): ")
    if cmnd=='1':
        word=input("search word (BG/EN):")
        f=open("dictionary.txt", "r")
        for line in f:
            if word in line:
                z=1
                print(line)
        f.close()
        if z==0:
            print("this word doesn't exist in dictionary! If you know the word translation, please add it (command 3)!")
    
    elif cmnd=='2':
        f=open("dictionary.txt", "a")
        word=input("write the word: ")
        translate=input("write translation of the word: ")
        f.write(word+' - '+translate+'\n')
        f.close()
        print("your word was written!")
    
    elif cmnd=='3':
        word=input("write the word to delete: ")
        f=open("dictionary.txt", "r")
        d=f.readlines()
        f.close()
        f1=open("dictionary.txt", "w")
        for line in d:
            if word not in line:
                f1.write(line)
        f1.close()
        print("your word was deleted succsesfully!")
    
    elif cmnd=='4':
        f=open("dictionary.txt", "r")
        for line in f:
            print(line)
        f.close() 