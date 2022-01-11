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
        
    def add(self, obj):
        for i in self.lst:
            if i[0]==obj.id:
                print("this id is existing!")
                return
        l=[]
        l.append(obj.id)   
        l.append(obj.dest) 
        l.append(obj.fl) 
        l.append(obj.pr) 
        self.lst.append(l)
        
    def Prnt(self):
        return self.lst
    
    def Reduce(self):
        for i in self.lst:
            if i[3]>200:
                i[3]=i[3]-(i[3]*0.1)

tr=TravelGroup()    
while True:
    try:
        num=input("ID(for end, type 'end'):")
        if num=='end':
            break
        d=input("destination:")
        f=input("flight:")
        p=float(input("price:"))
        p=round(p, 2)
        obj=Travel(num, d, f, p)
        tr.add(obj)
        if p<0:
            raise MyError("please input a valid price!")
    except MyError as error:
        print(error)
    except:
        print("Oops.. Something wrong... Please try again!")
    
print(tr.Prnt())
tr.Reduce()
print(tr.Prnt())