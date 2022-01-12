class MyError(Exception):
    pass

class Travel:
    def __init__(self, ID, Destination, Flight, Price):
        self.id=ID
        self.dest=Destination
        self.fl=Flight
        self.pr=Price

class TravelGroup:
    def __init__(self):
        self.lst=[]
        self.f=open('travel.txt', 'a+')
    
    def add(self, obj):
        self.l=[]
        for i in self.lst:
            if i[0]==obj.id:
                print("this ID already exist!")
                return
        self.l.append(obj.id)
        self.l.append(obj.dest)
        self.l.append(obj.fl)
        self.l.append(obj.pr)
        self.lst.append(self.l)
        self.f.write(str(self.l))
    
    def Prnt(self):
        print(self.lst)
        
    def Reduce(self):
        for i in self.lst:
            if i[3]>200:
                i[3]=i[3]-(i[3]*0.1)
                
    def Close(self):
        self.f.close()
        
tr=TravelGroup()
while True:
    try:
        num=input("ID:")
        if num=='end':
            break
        d=input("destination:")
        f=input("Flight:")
        p=float(input("Price:"))
        p=round(p, 2)
        if p<0:
            raise MyError("Please inpput a valid price!")
        obj=Travel(num, d, f, p)
        tr.add(obj)
    except MyError as error:
        print(error)
    except:
        print("Ooops... Something wrong... Try again!")
tr.Prnt()
tr.Reduce()
tr.Prnt()
tr.Close()