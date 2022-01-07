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

s1=set(lst)
h=1
for i in s1:
    x=lst.count(i)
    if x>h:
        h=x
        c=i
    
print("{0} pieces of {1}".format(h, c))