def chetni(lst):
    l=[]
    for i in range(0, len(lst)):
        if lst[i]%2!=0:
            l.append(lst[i])
    return l

n=int(input("n="))
li=[]
for j in range (0,n):
    a=int(input(str(j+1)+":"))
    li.append(a)
print(chetni(li))