import random
import time
import tkinter as tk

def Start():
    txt.config(text = "Играта съдържа 10 въпроса. За всеки въпрос има няколко възможни отговори, от които само един е верен. Ако бъде избран грешен отговор играта приключва.")
    but.config(text="START!", command=lst)
    but.pack()
    but.place(x=270, y=200)
    click.place_forget()
    click1.place_forget()
    click2.place_forget()
    click3.place_forget()
  
def lst():
    global ls
    global br
    br=0
    ls=[]
    while len(ls)!=10:
        r=random.randint(0,17)
        if r not in ls: ls.append(r)
    Questions()
    
def Questions():
    for i in ls:
        if i==0:
            s="В кой град и коя година е създаден българският завод 'РЕСПРОМ'('Битова електроника')?"
            l=["Търново, 1960 г.", "Правец, 1972 г.", "Пловдив, 1962 г.", "Варна, 1968 г."]
            otg="Търново, 1960 г."
            info="Предприятието е създадено през 1960 г. като Завод за малки радиоприемници (ЗМР), а впоследствие – Завод за транзисторни приемници (ЗТР) във Велико Търново. Строителството и изграждането на комплекса се извършват за период около три години. „Старият радиозавод“ се намира в местността „Дервеня“, по пътя от града към село Самоводене. Първоначално постъпилите на работа работници са 34."
            QuAns(s, l, otg, info)
                
        if i==1:
            s="Какво произвежда българската фирма 'БАЛКАНТОН'?"
            l=["Грамофони", "Мизукални носители", "Усилватели", "Телевизори"]
            otg="Мизукални носители"
            info="„Балкантон“ е българска звукозаписна компания, създадена под това име в София през 1952 г. Монополист на българския пазар през периода на социалистическото управление на страната от 40-те години на 20 век до 1989 г. Приватизирана през 1999 г. при правителството на ОДС. "
            QuAns(s, l, otg, info)
            

        if i==2:
            s="В заводите на коя българска компания и през коя година, започва производството на радиокасетофон 'ОКТАВА'?"
            l=["Велико Търново, 1960 г.", "Перла, 1960 г.", "Велико Търново, 1975 г.", "Балкантон, 1975 г."]
            otg="Велико Търново, 1975 г."
            info="Октава е популярен български радиокасетофон. Произвежда се от 1975 г. в Завода за радиоприемници Велико Търново. Радиокасетофонът „Октава“ е предназначен за прослушване на радиоразпръсквателни станции в обхвата на ДВ и СВ, а с помощта на вградения касетен магнетофон може да се прослушват записи, да се правят директно записи от вградения радиоприемник и записи от външен източник — микрофон, грамофон, радиоприемник или магнетофон."
            QuAns(s, l, otg, info)
             

        if i==3:
            s="Кой е първият български телевизор и от коя година е?"
            l=["Голдстар, 1945 г.", "Велико Търново, 1975 г.", "Орион, 1958 г.", "Опера, 1960 г."]
            otg="Опера, 1960 г."
            info="Първия български телевизор е Опера 1, от 1960 г. Кинескопа е западен АW43-80, в повечето случаи  производство на Тунгсрам. Външно оформлението е силно повлияно от унгарския телевизор Орион 53Т816 – дори несиметричните вентилационни отвори на задния капак са запазени."
            QuAns(s, l, otg, info)
             
            
        if i==4:
            s="През 1958 г. Елпром, Варна произвежда ПЕА-1. Какво представлява?"
            l=["акумулираща печка","електрическа помпа за автомобил","електрическа антена за покрив","готварска печка"]
            otg="акумулираща печка"
            info="Първата българска акумулираща печка, произведена през 1958 г. в завод Елпром Варна, известна с означението ПЕА-1, което значи ,,печка електрическа акумулираща, 1-ва поред разработка на завода“."
            QuAns(s, l, otg, info)
             
                
        if i==5:
            s="През 1985 г.в дн. ТУ, София се произвежда първия български компютър, служещ за обучение ЕМК. Какво ознава съкращението?"
            l=["Едноличен малък компютър", "Едноплатков микрокомпютър", "Електро-магнитен компютър", "Евтин малък компютър"]
            otg="Едноплатков микрокомпютър"
            info="Наред с компютрите и периферията за широка употреба – различните серии на Правеците, ИЗОТ-ите и т.н. – обикновено се забравят българските компютри, предназначени за обучение. Едно такова място е Висшият машинно-електротехнически институт ,,Ленин“ (дн. Технически университет София), където през 80-те години в лаборатория ,,Микро­процесори и микрокомпютри“ са проектирани, и изработени поне 15 – 18 Едноплаткови микро-компютри, предназначени за обучение в техникумите и ВУЗ-овете."
            QuAns(s, l, otg, info)
             
            
        if i==6:
            s="Коя българска фирма, произвеждаща от 20-ти век готварски печки, продължава и до днес?"
            l=["Перла","Беко","Раховец","Зануси"]
            otg="Раховец"
            info="Раховец е българска готварска печка, произвеждана в Горна Оряховица. След кратко прекъсване през 1995 г., раховец отново възстановява производството си."
            QuAns(s, l, otg, info)
             
                
        if i==7:
            s="Елпром Варна произвежда първият български бойлер ЕБО. През коя година?"
            l=["1968 г.","1964 г.","1958 г.","1960 г."]
            otg="1960 г."
            info="ЕБО е произвеждан от първата половина на 60-те г. в завод Елпром Варна. Той е с обем 200 литра и се нарича ЕБО-200 (от ,,електрически бойлер обикновен“). Използван е за обществени цели -  почивни станции, болници, ресторанти, хотели, а и в селското стопанство."
            QuAns(s, l, otg, info)
             
                
        if i==8:
            s="През 1965 г. Елпром Варна произвежда 'ЛЪЧ'. Какво представлява?"
            l=["Отоплителна печка","Бойлер","Готварска печка","Друго"]
            otg="Отоплителна печка"
            info="'ЛЪЧ' е най-разпространеният домашен отоплителен уред в последния половин век. Влиза в производство през 1965 г. и е произвеждан в завод Елпром Варна."
            QuAns(s, l, otg, info)
             
                
        if i==9:
            s="През 70-те години на 20ти век югославското предприятие 'Електронска индустриjа' дава лиценз на българия за производство на пералня 'ПЕРЛА'. В кой завод?"
            l=["Респром, Търново","Елпром, Варна","Правец","Друг"]
            otg="Елпром, Варна"
            info="В началото на 70-те години югославското предприятие 'Електронска индустриjа' - Ниш, което вече произвежда собствени модели автоматични перални 'Перла', дава лиценз за производството им на заводите за електродомакински уреди Татрамат в Попрад, тогавашна Чехословакия, и на българския завод 'Елпром' във Варна."
            QuAns(s, l, otg, info)
             
                
        if i==10:
            s="През 1965 г. е създаден първия български калкулатор. Кой е той?"
            l=["Елка-1300","Касио","Елка-6521","Шарп"]
            otg="Елка-6521"
            info="Елка е марка български електронни калкулатори и касови апарати. Първият модел на калкулатора – Елка-6521 е създаден през 1965 г. в Института по математика към БАН. Това е първият електронен калкулатор създаден в България."
            QuAns(s, l, otg, info)
             
                
        if i==11:
            s="Правец 82 е направен по копие на?"
            l=["Apple II","Commodore 64","Друг","Apple I"]
            otg="Apple II"
            info="През 1980 г. в ИТКР е създаден ИМКО-1, първият български персонален компютър. Името на научната разработка на Иван Марангозов идва от Индивидуален МикроКОмпютър. Следва разработката на ИМКО-2, който е преименуван на „Правец-82“ и през 1983 г. започва серийното му производство в Приборостроителния завод в Правец, по-късно разширен и превърнат в Комбинат по микропроцесорна техника – Правец. Правец 82 следва компютърната архитектура на Apple II и двете системи са съвместими."
            QuAns(s, l, otg, info)
             
                
        if i==12:
            s="Какво значи съкращението ИМКО?"
            l=["Индивидуален Микро-компютър","Иван Марангозов копирал оригинала","Индустриален международен конкурс по оптика","Индивидуална машина за копиране"]
            otg="Индивидуален Микро-компютър"
            info="През 1980 г. в ИТКР е създаден ИМКО-1, първият български персонален компютър. Името на научната разработка на Иван Марангозов идва от Индивидуален МикроКОмпютър. "
            QuAns(s, l, otg, info)
             
                    
        if i==13:
            s="През втората половина на 20-ти век в Пловдив се произвежда първият български електробус ЕЛМОБУС`78. През коя година?"
            l=["1978 г.","1980 г.","1970 г.","1987 г."]
            otg="1978 г."
            info=",,Двата основни проблема на нашето време – енергийната криза и замърсяването на околната среда – възродиха идеята за чистия електрически двигател и накараха специалистите да видят в електромобила оптимален градски транспорт.“ - този текст се разпространява във вестниците още преди половин век. През 1978 г. в Националния преглед на движението ТНТМ на Пловдивския панаир дебютира първият български електробус. Превозното средство използва типичната позната каросерия от микробус Чавдар 5С, но в средата, между емблемата на Балканкар и левия фар, се вижда издигнат многозначителен надпис: ЕЛМОБУС`78. Електробусът е боядисан в бяло и светлочервено."
            QuAns(s, l, otg, info)
             
                    
        if i==14:
            s="През 1964 г. се произвежда електроуред 'Мечта'. Какво представлява той и в кой завод се произвежда?"
            l=["готварска печка, Елпром - Варна","хладилник, Елпром - Варна","телевизор, Респром - Велико Търново","компютър, Правец"]
            otg="готварска печка, Елпром - Варна"
            info="Историята на печки 'Мечта' започва през 1964 или 65 г., а първата Мечта е създадена на основата на печка Чайка. Производител е завод Елпром Варна, а тя има моделен номер 71202. Гаранцията на тази печка е била 1 година, а в действителност още могат да се срещнат такива работещи! За разлика от Чайката, първият модел от новата серия представлява голяма крачка напред, защото има голяма фурна и три нагревателни плочи (котлони) вместо две. По-голяма е и камерата за затопляне на ястия, която се намира под фурната."
            QuAns(s, l, otg, info)
             
                    
        if i==15:
            s="През 1962 г. България произвежда хладилник 'Мраз'. В кой завод?"
            l=["Антон Иванов, София","Елпром, Варна","Респром, Велико Търново","друг"]
            otg="Антон Иванов, София"
            info="Домашният хладилник 'Мраз' е пуснат в производство през 1962 г. от Хладилния завод Антон Иванов, София. Предназначен е за запаз­ване на бързоразвалящи се хранителни продукти при до­машни условия и за добиване в малки коли­чества на бучки чист лед."
            QuAns(s, l, otg, info)
             
                    
        if i==16:
            s="През 1960 г. Елпром, Варна започва производството на електроуред, служещ за загряването на вода в съд, от канче, до големи казани. Кой е този електроуред?"
            l=["Бързовар","Бойлер","Открит котлон","готварска печка"]
            otg="Бързовар"
            info="Производството на този вид бързовари у нас започва около 1960 г. в завод Елпром Варна. Първоначално са изработвани 4 модела – те имат мощност от 600 до 3000 вата и са пускани в две версии – за 150 и 220 волта напрежение."
            QuAns(s, l, otg, info)
             
                    
        if i==17:
            s="През 1972 г., вероятно в Института по хладилна и климатична техника, е разработен климатик КСА. Какво означава съкращението?"
            l=["автономен стаен климатизатор","автономна климатична система","климатична система за автомобил","климатична система - Казанлък"]
            otg="автономен стаен климатизатор"
            info="Първият български ДОМАШЕН климатик е бил разработен у нас през 1972 г., в Института по хладилна и климатична техника и е произвеждан в Завода за климатична техника ,,Клокотница“ в Димитровград. Нарича се КСА 1.6 (от ,,климатизатор стаен автономен“) и има четири функции – охлаждане, филтриране, частично изсушаване и вентилиране на въздуха. Може да поддържа температура на въздуха в помещението между 21 и 28 градуса. Компресорът и вентилаторът на КСА-то са почти безшумни."
            QuAns(s, l, otg, info)
    if len(ls)!=0:
        ls.pop()
    else:
          Count()
             

def QuAns(s, l, otg, info):
    random.shuffle(l) 
    txt.config(text=s)
    
    click.config(text=l[0], command=lambda: Check(l[0], otg))
    click.pack()
    click.place(x=50, y=200)

    click1.config(text=l[1], command=lambda: Check(l[1], otg))
    click1.pack()
    click1.place(x=500, y=200)

    click2.config(text=l[2], command=lambda: Check(l[2], otg))
    click2.pack()
    click2.place(x=50, y=350)

    click3.config(text=l[3], command=lambda: Check(l[3], otg))
    click3.pack()
    click3.place(x=500, y=350)
    
    but.place_forget()
    
def Check(ans, otg):
    global br
    if ans==otg:
        br+=1
        Questions()
    else:
        Count()

def Count():
    if br==10:
        txt.config(text="Спечели! Верни отговори: "+str(br))
    else:
        txt.config(text="За съжаление сбърка... Верни отговори: "+str(br))
    but.config(text="Нова игра?", command=lst)
    but.pack()
    but.place(x=30, y=100)
    click.place_forget()
    click1.place_forget()
    click2.place_forget()
    click3.place_forget()

screen=tk.Tk()
screen.iconbitmap('img/logo.ico')
screen.configure(bg='#cfe6ff')
screen.title("Българската техника на 20-ти век")
#screen.state('zoomed') 
screen.geometry("950x500") 
screen.minsize(950, 500)

txt=tk.Label(text="", fg="#1b5da8", bg="#cfe6ff", wraplengt=900, font=('Arial', 25))
txt.pack()
txt.place(x=30, y=30)

click=tk.Button(text="", fg="#cfe6ff", bg="#1b5da8", wraplengt=300, height=3, width=25, font=('Arial', 20))
click.pack_forget()

click1=tk.Button(text="", fg="#cfe6ff", bg="#1b5da8", wraplengt=300, height=3, width=25, font=('Arial', 20))
click1.pack_forget()

click2=tk.Button(text="", fg="#cfe6ff", bg="#1b5da8", wraplengt=300, height=3, width=25, font=('Arial', 20))
click2.pack_forget()

click3=tk.Button(text="", fg="#cfe6ff", bg="#1b5da8", wraplengt=300, height=3, width=25, font=('Arial', 20))
click3.pack_forget()

but=tk.Button(text="", fg="#cfe6ff", bg="#1b5da8", wraplengt=300, height=3, width=25, font=('Arial', 20))
but.pack_forget()

Start()

screen.mainloop()