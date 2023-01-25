def coder(str):
    for n in str:
        t=ord(n)
        print(t, end=' ')

def decoder(code):
    print("\n")
    list = code.split()
    for i in range(len(list)):
        list[i] = int(list[i])
    ASCII_string = "".join([chr(value) for value in list])
    print(ASCII_string)        

a=1
while a>0:
    print("your choice:")
    print("for 'word->code' press 1;")
    print("for 'code->word' press 2;")
    c=int(input("your choice:"))
    if c==1:
        s=input("sentence: ")
        coder(s)
    elif c==2:
        dc = input('code:')
        decoder(dc)
    else:
        print("ERROR!")
    print('\n')