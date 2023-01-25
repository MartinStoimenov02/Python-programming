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
        self.f=open("travel.txt", 'a')
    
    def add(self, obj):
        self.f.write(obj.id+"   "+obj.dest+'   '+obj.fl+'   '+str(obj.pr)+'\n')
        
    def Reduce(self):
        if obj.pr>200:
            obj.pr=obj.pr-(obj.pr*0.1)
            self.f.write("discount 10%: "+obj.id+"   "+obj.dest+'   '+obj.fl+'   '+str(obj.pr)+'\n')        
    
    def Close(self):
        self.f.close()
        
    def Print(self):
        fil=open('travel.txt', 'r')
        fil.seek(0,0)
        print(fil.read())
        fil.close()        

tr=TravelGroup()
while True:
    try:
        num=input("ID:")
        if num=='end':
            break
        d=input("Destination:")
        f=input("Flight:")
        p=float(input("Price:"))
        p=round(p,2)
        if p<0:
            raise MyError()
        obj=Travel(num, d, f, p)
        tr.add(obj)
        tr.Reduce()
    except (MyError, ValueError):
        print("Input a valid price!")
    except:
        print("Ooops... Something wrong... Try again!")
tr.Close()
tr.Print()