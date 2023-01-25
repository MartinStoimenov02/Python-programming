a=1
while a>0:
    print("your choice:")
    print("for 'word->code' press 1;")
    print("for 'code->word' press 2;")
    c=int(input("your choice:"))
    if c==1:
        str=input("sentence: ")
        for n in str:
            t=ord(n)
            print(t, end=' ')
    elif c==2:
        code = input('code:')
        print("\n")
        list = code.split()
        for i in range(len(list)):
            list[i] = int(list[i])
        ASCII_string = "".join([chr(value) for value in list])
        print(ASCII_string)
    else:
        print("ERROR!")
    print('\n')