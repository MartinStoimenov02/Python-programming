import random
def Ans(ls, st, ot):
    print(st)
    random.shuffle(ls)
    ind=0
    for k in ls:
        ind+=1
        print(f"{ind}) {k}")
    ans=int(input("answear:"))
    if ans==(l.index(ot))+1:
        print("True!")
    else:
        print("False!")
        return "end"
    
list=[]
j=0
while len(list)!=4:
    r=random.randint(0,3)
    if r not in list: list.append(r)
print(list)
for i in list:
    
    if i==0:
        s="В кой град и коя година е създаден българският завод 'РЕСПРОМ'?"
        l=["Търново, 1960 г.", "Правец, 1972 г.", "Пловдив, 1962 г.", "Варна, 1968 г."]
        otg="Търново, 1960 г."
        if Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==1:
        s="Какво произвежда българската фирма 'БАЛКАНТОН'?"
        l=["Грамофони", "Мизукални носители", "Усилватели", "Телевизори"]
        otg="Мизукални носители"
        if Ans(l, s, otg)=="end":
            break
        else:
            j+=1

    if i==2:
        s="В заводите на коя българска компания и през коя година, започва производството на радиокасетофон 'ОКТАВА'?"
        l=["Велико Търново, 1960 г.", "Перла, 1960 г.", "Велико Търново, 1975 г.", "Балкантон, 1975 г."]
        otg="Велико Търново, 1975 г."
        if Ans(l, s, otg)=="end":
            break
        else:
            j+=1

    if i==3:
        s="Кой е първият български телевизор и от коя година е?"
        l=["Голдстар, 1945 г.", "Велико Търново, 1975 г.", "Орион, 1958 г.", "Опера, 1960 г."]
        otg="Опера, 1960 г."
        if Ans(l, s, otg)=="end":
            break
        else:
            j+=1
    
    if i==4:
        print("По модел на кой модел чуждестранни компютри е направен 'ПРАВЕЦ 8С?")
        print("A) Apple II\nB) Apple I\nC) Commodore 64\nD) Друг")
        ans=input("answear:")
        if ans=="A":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==5:
        print("През 1985 г.в дн. ТУ, София се произвежда първия компютър, служещ за обучение ЕМК. Какво ознава съкращението?")
        print("A) Едноличен малък компютър\nB) Едноплатков микрокомпютър \nC) Електро-магнитен компютър\nD) Евтин малък компютър")
        ans=input("answear:")
        if ans=="B":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==6:
        print("Коя българска фирма, произвеждаща от 20-ти век готварски печки, продължава и до днес?")
        print("A) Перла \nB) Беко\nC) Раховец \nD) Зануси")
        ans=input("answear:")
        if ans=="C":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==7:
        print("Елпром Варна произвежда първият български бойлер ЕБО. През коя година?")
        print("A) 1968 г.\nB) 1964 г.\nC) 1958 г.\nD) 1960 г. ")
        ans=input("answear:")
        if ans=="D":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==8:
        print("През 1965 г. Елпром Варна произвежда 'ЛЪЧ'. Какво представлява?")
        print("A) Отоплителна печка\nB) Бойлер\nC) Готварска печка\nD) Друго")
        ans=input("answear:")
        if ans=="A":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==9:
        print("През на 70-те югославско предприятие дава лиценз на българия за производство на пералня 'ПЕРЛА'. В кой завод?")
        print("A) Респром, Търново\nB) Елпром, Варна\nC) Правец\nD) Друг")
        ans=input("answear:")
        if ans=="B":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==10:
        print("През 1965 г. е създаден първия български калкулатор. Кой е той?")
        print("A) Елка-1300\nB) Касио\nC) Елка-6521\nD) Шарп")
        ans=input("answear:")
        if ans=="C":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==11:
        print("Правец 82 е направен по копие на?")
        print("A) Apple II\nB) Commodore 64\nC) Друг\nD) Apple I")
        ans=input("answear:")
        if ans=="D":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
    if i==12:
        print("Какво значи съкращението ИМКО?")
        print("A) Индивидуален Микро-компютър\nB) Иван Марангозов копирал оригинала\nC) Индустриален международен конкурс по оптика\nD) Индивидуална машина за копиране")
        ans=input("answear:")
        if ans=="A":
            print("True!")
            j=j+1
        else:
            print("False!")
            break
        
print(f"your true answears: {j}")