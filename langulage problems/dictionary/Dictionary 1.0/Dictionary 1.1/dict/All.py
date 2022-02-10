def All():
    f=open("dictionary.txt", "r")
    for line in f:
        print(line)
    f.close() 