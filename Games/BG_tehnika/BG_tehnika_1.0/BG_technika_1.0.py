import random
class BGT:
    def __init__(self):
        pass
    
    def Ans(self, ls, st, ot):
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
bg=BGT()
while len(list)!=19:
    r=random.randint(0,18)
    if r not in list: list.append(r)
print(list)
for i in list:
    
    if i==0:
        s="В кой град и коя година е създаден българският завод 'РЕСПРОМ'('Битова електроника')?"
        l=["Търново, 1960 г.", "Правец, 1972 г.", "Пловдив, 1962 г.", "Варна, 1968 г."]
        otg="Търново, 1960 г."
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==1:
        s="Какво произвежда българската фирма 'БАЛКАНТОН'?"
        l=["Грамофони", "Мизукални носители", "Усилватели", "Телевизори"]
        otg="Мизукални носители"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1

    if i==2:
        s="В заводите на коя българска компания и през коя година, започва производството на радиокасетофон 'ОКТАВА'?"
        l=["Велико Търново, 1960 г.", "Перла, 1960 г.", "Велико Търново, 1975 г.", "Балкантон, 1975 г."]
        otg="Велико Търново, 1975 г."
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1

    if i==3:
        s="Кой е първият български телевизор и от коя година е?"
        l=["Голдстар, 1945 г.", "Велико Търново, 1975 г.", "Орион, 1958 г.", "Опера, 1960 г."]
        otg="Опера, 1960 г."
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
    
    if i==4:
        s="По модел на кой модел чуждестранни компютри е направен българският 'ПРАВЕЦ 8С?"
        l=["Apple II", "Apple I", "Commodore 64", "Друг"]
        otg="Apple II"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==5:
        s="През 1985 г.в дн. ТУ, София се произвежда първия български компютър, служещ за обучение ЕМК. Какво ознава съкращението?"
        l=["Едноличен малък компютър", "Едноплатков микрокомпютър", "Електро-магнитен компютър", "Евтин малък компютър"]
        otg="Едноплатков микрокомпютър"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==6:
        s="Коя българска фирма, произвеждаща от 20-ти век готварски печки, продължава и до днес?"
        l=["Перла","Беко","Раховец","Зануси"]
        otg="Раховец"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==7:
        s="Елпром Варна произвежда първият български бойлер ЕБО. През коя година?"
        l=["1968 г.","1964 г.","1958 г.","1960 г."]
        otg="1960 г."
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==8:
        s="През 1965 г. Елпром Варна произвежда 'ЛЪЧ'. Какво представлява?"
        l=["Отоплителна печка","Бойлер","Готварска печка","Друго"]
        otg="Отоплителна печка"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==9:
        s="През 70-те години на 20ти век югославското предприятие 'Електронска индустриjа' дава лиценз на българия за производство на пералня 'ПЕРЛА'. В кой завод?"
        l=["Респром, Търново","Елпром, Варна","Правец","Друг"]
        otg="Елпром, Варна"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==10:
        s="През 1965 г. е създаден първия български калкулатор. Кой е той?"
        l=["Елка-1300","Касио","Елка-6521","Шарп"]
        otg="Елка-6521"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==11:
        s="Правец 82 е направен по копие на?"
        l=["Apple II","Commodore 64","Друг","Apple I"]
        otg="Apple I"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==12:
        s="Какво значи съкращението ИМКО?"
        l=["Индивидуален Микро-компютър","Иван Марангозов копирал оригинала","Индустриален международен конкурс по оптика","Индивидуална машина за копиране"]
        otg="Индивидуален Микро-компютър"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
            
    if i==13:
        s="През втората половина на 20-ти век в Пловдив се произвежда първият български електробус ЕЛМОБУС`78. През коя година?"
        l=["1978 г.","1999 г.","1950 г.","2001 г."]
        otg="1978 г."
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
            
    if i==14:
        s="През 1964 г. се произвежда електроуред 'Мечта'. Какво представлява той и в кой завод се произвежда?"
        l=["готварска печка, Елпром - Варна","хладилник, Елпром - Варна","телевизор, Респром - Велико Търново","компютър, Правец"]
        otg="готварска печка, Елпром - Варна"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
            
    if i==15:
        s="През 1962 г. България произвежда хладилник 'Мраз'. В кой завод?"
        l=["Антон Иванов, София","Елпром, Варна","Респром, Велико Търново","друг"]
        otg="Антон Иванов, София"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
            
    if i==16:
        s="През 1960 г. Елпром, Варна започва производството на електроуред, служещ за загряването на вода в съд, от канче, до големи казани. Кой е този електроуред?"
        l=["Бързовар","Бойлер","Открит котлон","готварска печка"]
        otg="Бързовар"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
            
    if i==17:
        s="През 1972 г., вероятно в Института по хладилна и климатична техника, е разработен климатик КСА. Какво означава съкращението?"
        l=["автономен стаен климатизатор","автономна климатична система","климатична система за автомобил","климатична система - Казанлък"]
        otg="автономен стаен климатизатор"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
    if i==18:
        s="През 1958 г. Елпром, Варна произвежда ПЕА-1. Какво представлява?"
        l=["акумулираща печка","електрическа помпа за автомобил","електрическа антена за покрив","готварска печка"]
        otg="акумулираща печка"
        if bg.Ans(l, s, otg)=="end":
            break
        else:
            j+=1
        
print(f"your true answears: {j}")