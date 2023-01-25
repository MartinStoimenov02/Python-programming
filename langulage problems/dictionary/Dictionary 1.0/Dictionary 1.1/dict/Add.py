def Add():
    word=input("write the word: ")
    translate=input("write translation of the word: ")
    if len(word)==0 or len(translate)==0:
        print("Textboxes are empty! Please input a word and translate!")
        return
    t=word+' - '+translate+'\n'
    t1=translate+' - '+word+'\n'
    fil=open("dictionary.txt", "r")
    for line in fil:
        if t==line or t1==line:
            fil.close()
            print("this word already exist!")
            return
    fil.close()
    f=open("dictionary.txt", "a")
    f.write(word+' - '+translate+'\n')
    f.close()
    print("your word was written!")