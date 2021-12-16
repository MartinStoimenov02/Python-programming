f1=open('file1.txt', 'a')
n=int(input("num:"))
for i in range(1, n+1):
    word=input("["+str(i)+"]:")
    f1.write(word)
    f1.write('\n')
f1.close()

fi=open('file1.txt', 'r')
f2=open('file2.txt', 'a')
for line in fi:
    if line[0]=='a' or line[0]=='e' or line[0]=='i' or line[0]=='o' or line[0]=='u':
        f2.write(line)
    
    if line[0]=='а' or line[0]=='ъ' or line[0]=='о' or line[0]=='у' or line[0]=='е' or line[0]=='и':
        f2.write(line)
    
fi.close()
f2.close()