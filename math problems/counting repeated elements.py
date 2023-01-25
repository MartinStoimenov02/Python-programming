n=int(input("n="))
list=[]
for i in range(1,n+1):
    a=int(input("a["+str(i)+"]="))
    list.append(a)
print(list)
for i in range(1,n+1):
    a=list.count(list[i-1])
    if a>1:
        print("в редицата има повтарящи се елементи!")
        break
if a==1:
    print("в редицата няма повтарящи се елементи!")
