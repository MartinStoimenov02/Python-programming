'''
напишете програма, която намира максимална редица от последователни еднакви елементи в списък и ги отпечатва
примерен вход: [2,1,1,2,3,3,2,2,2,1]
изход: 2,2,2
'''
lst=[]
n=int(input("n="))
for i in range(0, n):
    a=int(input("["+str(i+1)+"]:"))
    lst.append(a)

z=1
y=1
for i in range (1, n):
    if lst[i-1]==lst[i]:
        z=z+1
    else:
        z=1
    if z>y:
        x=lst[i]
        y=z

print(str(x)*y)